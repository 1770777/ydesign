from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
STYLES = ROOT / "styles.css"
SCRIPT = ROOT / "script.js"
RESUME_DATA = ROOT / "assets/downloads/resume-data.js"
CNAME = ROOT / "CNAME"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.start_tags = []
        self.links = []
        self.text_parts = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.start_tags.append((tag, attrs_dict))
        if tag == "a":
            self.links.append(attrs_dict)

    def handle_data(self, data):
        text = data.strip()
        if text:
            self.text_parts.append(text)


def parse_site():
    parser = SiteParser()
    parser.feed(INDEX.read_text(encoding="utf-8"))
    return parser


class PortfolioSiteSmokeTest(unittest.TestCase):
    def test_required_files_exist(self):
        self.assertTrue(INDEX.exists(), "index.html should exist")
        self.assertTrue(STYLES.exists(), "styles.css should exist")
        self.assertTrue(CNAME.exists(), "CNAME should exist for custom domain hosting")
        self.assertEqual(CNAME.read_text(encoding="utf-8").strip(), "ydesign.bbroot.com")

    def test_page_has_semantic_landmarks_and_sections(self):
        parser = parse_site()
        tags = [tag for tag, _attrs in parser.start_tags]
        for tag in ["header", "main", "section", "footer"]:
            self.assertIn(tag, tags)

        tags_by_id = {
            attrs.get("id"): tag
            for tag, attrs in parser.start_tags
            if attrs.get("id")
        }
        self.assertEqual(tags_by_id.get("top"), "header")

        content_ids = {
            "cases",
            "lead-case",
            "selected-cases",
            "experience",
            "toolkit",
            "contact",
        }
        content_tags = {"section", "article", "div", "footer"}
        for section_id in content_ids:
            self.assertIn(tags_by_id.get(section_id), content_tags)

    def test_page_links_to_site_stylesheet(self):
        parser = parse_site()
        has_stylesheet = any(
            tag == "link"
            and attrs.get("rel") == "stylesheet"
            and attrs.get("href") == "styles.css"
            for tag, attrs in parser.start_tags
        )
        self.assertTrue(has_stylesheet)

    def test_page_links_to_motion_script(self):
        parser = parse_site()
        has_script = any(
            tag == "script"
            and attrs.get("src") == "script.js"
            and "defer" in attrs
            for tag, attrs in parser.start_tags
        )
        self.assertTrue(has_script)

    def test_content_matches_approved_portfolio_direction(self):
        text = "\n".join(parse_site().text_parts)
        required_phrases = [
            "大头",
            "UI Designer",
            "复杂服务",
            "清晰体验",
            "建信财险 APP",
            "信美相互 APP",
            "拉风漫画 APP",
            "官网与品牌视觉",
            "问题",
            "过程",
            "结果",
            "PM / Dev Collaboration",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, text)

    def test_contact_links_are_actionable(self):
        links = parse_site().links
        hrefs = {link.get("href") for link in links}
        self.assertIn("mailto:18801378561@163.com", hrefs)
        self.assertIn("tel:18801378561", hrefs)
        self.assertIn("#cases", hrefs)
        self.assertIn("#contact", hrefs)
        self.assertIn("assets/downloads/resume.md", hrefs)

        resume_links = [
            link for link in links
            if link.get("href") == "assets/downloads/resume.md"
        ]
        self.assertTrue(resume_links)
        self.assertTrue(all(link.get("download") for link in resume_links))
        self.assertTrue((ROOT / "assets/downloads/resume.md").exists())
        self.assertTrue(RESUME_DATA.exists())

    def test_resume_download_uses_blob_fallback_for_local_files(self):
        html = INDEX.read_text(encoding="utf-8")
        script = SCRIPT.read_text(encoding="utf-8")
        data_script = RESUME_DATA.read_text(encoding="utf-8")

        self.assertIn("assets/downloads/resume-data.js", html)
        self.assertIn("resume-download", html)
        self.assertIn("resumeDownloadPayload", data_script)
        self.assertIn("base64ToBlob", script)
        self.assertIn("URL.createObjectURL", script)

    def test_css_supports_responsive_accessible_system_style(self):
        css = STYLES.read_text(encoding="utf-8")
        required_patterns = [
            r":root",
            r"--ink:",
            r"--surface:",
            r"--accent:",
            r"@media\s+\(max-width:\s*760px\)",
            r"@media\s+\(prefers-reduced-motion:\s*reduce\)",
            r":focus-visible",
            r"scroll-behavior",
        ]
        for pattern in required_patterns:
            self.assertRegex(css, pattern)

    def test_motion_system_supports_scroll_reveals(self):
        css = STYLES.read_text(encoding="utf-8")
        script = (ROOT / "script.js").read_text(encoding="utf-8")
        for pattern in [
            r"@keyframes\s+heroTitleRise",
            r"@keyframes\s+orbitDrift",
            r"\.js-enabled\s+\.reveal",
            r"\.reveal\.is-visible",
            r"--ease-out-quint:",
        ]:
            self.assertRegex(css, pattern)

        self.assertIn("IntersectionObserver", script)
        self.assertIn("prefers-reduced-motion: reduce", script)
        self.assertIn("revealHashTarget", script)
        self.assertIn("hashchange", script)

    def test_no_resume_only_fields_are_visible(self):
        text = "\n".join(parse_site().text_parts)
        blocked_phrases = ["25 岁", "期望薪资", "目前状况", "离职"]
        for phrase in blocked_phrases:
            self.assertNotIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
