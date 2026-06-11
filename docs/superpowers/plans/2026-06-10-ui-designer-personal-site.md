# UI Designer Personal Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a static, case-led personal portfolio site for UI designer Zhou Yueqi using the approved problem-process-result and product-system direction.

**Architecture:** A single static page will hold all portfolio content in semantic sections. Styling lives in one focused CSS file with responsive grids, accessible contrast, and reduced-motion support. A small Python smoke test validates content, links, and required CSS contracts without adding a package manager.

**Tech Stack:** HTML5, CSS3, Python 3 standard library tests, local static server for visual QA.

---

## File Structure

- Create: `index.html`
  - Owns semantic content, navigation anchors, case study structure, contact links, and all resume-derived copy.
- Create: `styles.css`
  - Owns product-system visual direction, responsive layout, typography, interaction states, and reduced-motion rules.
- Create: `tests/site_smoke.py`
  - Owns fast static checks for required sections, contact links, project copy, CSS variables, responsive rules, and reduced-motion support.

No `script.js` is planned. The approved interaction scope can be handled with anchors and CSS hover/focus states.

---

### Task 1: Add Static Smoke Tests

**Files:**
- Create: `tests/site_smoke.py`

- [ ] **Step 1: Create failing smoke tests**

Create `tests/site_smoke.py` with this complete content:

```python
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
STYLES = ROOT / "styles.css"


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

    def test_page_has_semantic_landmarks_and_sections(self):
        parser = parse_site()
        tags = [tag for tag, _attrs in parser.start_tags]
        for tag in ["header", "main", "section", "footer"]:
            self.assertIn(tag, tags)

        ids = {attrs.get("id") for _tag, attrs in parser.start_tags}
        expected_ids = {
            "top",
            "cases",
            "lead-case",
            "selected-cases",
            "experience",
            "toolkit",
            "contact",
        }
        self.assertTrue(expected_ids.issubset(ids))

    def test_content_matches_approved_portfolio_direction(self):
        text = "\n".join(parse_site().text_parts)
        required_phrases = [
            "周月琪",
            "UI Designer",
            "把复杂服务设计成清晰可用的移动与网页体验",
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

    def test_no_resume_only_fields_are_visible(self):
        text = "\n".join(parse_site().text_parts)
        blocked_phrases = ["25 岁", "期望薪资", "目前状况", "离职"]
        for phrase in blocked_phrases:
            self.assertNotIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail before implementation**

Run:

```bash
python3 -m unittest tests.site_smoke -v
```

Expected: FAIL or ERROR because `index.html` and `styles.css` do not exist yet.

- [ ] **Step 3: Commit the failing tests**

Run:

```bash
git add tests/site_smoke.py
git commit -m "test: add portfolio site smoke checks"
```

Expected: commit succeeds with `tests/site_smoke.py` staged.

---

### Task 2: Build Semantic Portfolio HTML

**Files:**
- Create: `index.html`
- Test: `tests/site_smoke.py`

- [ ] **Step 1: Create the static page HTML**

Create `index.html` with this complete content:

```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta
      name="description"
      content="周月琪 UI Designer portfolio: mobile app, web UI, visual system, and product delivery case studies."
    />
    <title>周月琪 | UI Designer</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <header class="site-header" id="top">
      <a class="brand" href="#top" aria-label="回到顶部">
        <span class="brand-mark">ZY</span>
        <span>
          <strong>周月琪</strong>
          <small>UI Designer</small>
        </span>
      </a>
      <nav class="site-nav" aria-label="主导航">
        <a href="#cases">案例</a>
        <a href="#experience">经历</a>
        <a href="#toolkit">工具</a>
        <a href="#contact">联系</a>
      </nav>
    </header>

    <main>
      <section class="hero" aria-labelledby="hero-title">
        <div class="hero-copy">
          <p class="eyebrow">Mobile UI / Web Design / Visual System</p>
          <h1 id="hero-title">把复杂服务设计成清晰可用的移动与网页体验</h1>
          <p class="hero-intro">
            3 年+ UI / Web / 移动端设计经验，参与保险服务 App、社区产品、官网与品牌视觉设计，
            从用户流程、视觉规范到开发交付推进界面落地。
          </p>
          <div class="hero-actions" aria-label="主要操作">
            <a class="button primary" href="#cases">查看精选案例</a>
            <a class="button secondary" href="#contact">联系我</a>
          </div>
        </div>

        <aside class="hero-panel" aria-label="能力摘要">
          <p class="panel-label">Portfolio Focus</p>
          <h2>问题 · 过程 · 结果</h2>
          <p>
            面向设计负责人，展示真实项目中的需求理解、界面判断、视觉规范和协作交付能力。
          </p>
          <dl class="quick-facts">
            <div>
              <dt>Experience</dt>
              <dd>3 年+ UI / 视觉设计</dd>
            </div>
            <div>
              <dt>Platforms</dt>
              <dd>iOS / Android / Web</dd>
            </div>
            <div>
              <dt>Strength</dt>
              <dd>PM / Dev Collaboration</dd>
            </div>
          </dl>
        </aside>
      </section>

      <section class="capabilities" aria-label="核心能力">
        <span>Mobile UI</span>
        <span>Interaction Flow</span>
        <span>Visual System</span>
        <span>Web Design</span>
        <span>Brand Visual</span>
        <span>PM / Dev Collaboration</span>
      </section>

      <section class="cases" id="cases" aria-labelledby="cases-title">
        <div class="section-heading">
          <p class="eyebrow">Selected Work</p>
          <h2 id="cases-title">精选案例</h2>
          <p>
            每个项目都以设计负责人关心的方式呈现：面对什么问题，如何推进过程，最终形成什么结果。
          </p>
        </div>

        <article class="lead-case" id="lead-case" aria-labelledby="lead-case-title">
          <div class="case-meta">
            <p class="eyebrow">Lead Case / Mobile Insurance</p>
            <h3 id="lead-case-title">建信财险 APP</h3>
            <p>
              中国建设银行子公司建信财产保险有限公司官方 App，覆盖在线投保、保单服务与健康管理等保险服务场景。
            </p>
          </div>

          <div class="case-story">
            <section aria-labelledby="lead-problem">
              <span class="step-number">01</span>
              <h4 id="lead-problem">问题</h4>
              <p>
                保险服务流程长、信息密度高，用户需要在投保、保单与健康服务之间快速理解下一步操作。
              </p>
            </section>
            <section aria-labelledby="lead-process">
              <span class="step-number">02</span>
              <h4 id="lead-process">过程</h4>
              <p>
                根据客户需求与产品研讨，完成 iOS 和 Android 端 UI 设计，平衡易用性与视觉精致度，
                并持续优化高保真界面与用户体验。
              </p>
            </section>
            <section aria-labelledby="lead-result">
              <span class="step-number">03</span>
              <h4 id="lead-result">结果</h4>
              <p>
                输出结构更清晰的移动端保险服务界面，让投保、保单服务和健康管理形成更连贯的产品体验。
              </p>
            </section>
          </div>

          <ol class="process-line" aria-label="设计流程">
            <li>Research</li>
            <li>Prototype</li>
            <li>Visual Design</li>
            <li>Spec</li>
            <li>Delivery</li>
          </ol>
        </article>

        <div class="selected-cases" id="selected-cases">
          <article class="case-card">
            <p class="case-platform">Insurance App</p>
            <h3>信美相互 APP</h3>
            <p>
              将传统保险服务转向互联网产品体验，基于交互原型制定视觉风格、样式与高保真界面。
            </p>
            <ul class="tag-list" aria-label="信美相互 APP 标签">
              <li>App UI</li>
              <li>Visual Rules</li>
              <li>High Fidelity</li>
            </ul>
          </article>

          <article class="case-card">
            <p class="case-platform">Community App</p>
            <h3>拉风漫画 APP</h3>
            <p>
              面向 90 后、00 后漫画社区用户，在原型基础上完成移动端界面、交互层与 Icon 设计。
            </p>
            <ul class="tag-list" aria-label="拉风漫画 APP 标签">
              <li>Mobile UI</li>
              <li>Icons</li>
              <li>Asset Handoff</li>
            </ul>
          </article>

          <article class="case-card">
            <p class="case-platform">Web / Brand</p>
            <h3>官网与品牌视觉</h3>
            <p>
              覆盖 PC 官网、活动物料、公众号视觉、DM 单页、海报与画册，支持品牌传播和运营推广。
            </p>
            <ul class="tag-list" aria-label="官网与品牌视觉标签">
              <li>Web Design</li>
              <li>Campaign</li>
              <li>Brand Visual</li>
            </ul>
          </article>
        </div>
      </section>

      <section class="experience" id="experience" aria-labelledby="experience-title">
        <div class="section-heading">
          <p class="eyebrow">Experience</p>
          <h2 id="experience-title">工作经历</h2>
        </div>

        <div class="timeline">
          <article>
            <time datetime="2016-11">2016.11 - 2018.12</time>
            <div>
              <h3>天津易商阜级科技股份有限公司</h3>
              <p class="role">美术设计师 · 互联网服务业</p>
              <p>
                参与产品前期用户研究和趋势分析，负责官网、终端界面、H5 创意、移动端 UI 与视觉规范输出，
                并协同 PM 与开发推进界面落地。
              </p>
            </div>
          </article>

          <article>
            <time datetime="2015-06">2015.06 - 2016.11</time>
            <div>
              <h3>北京蓝正合融广告有限公司</h3>
              <p class="role">平面设计师 · 广告 / 策划 / 传媒服务业</p>
              <p>
                负责标识系统、画册、宣传资料、展示用品、网站与社交媒体视觉支持，
                配合线下和线上推广活动完成品牌传播设计。
              </p>
            </div>
          </article>
        </div>
      </section>

      <section class="toolkit" id="toolkit" aria-labelledby="toolkit-title">
        <div class="section-heading">
          <p class="eyebrow">Toolkit / Education</p>
          <h2 id="toolkit-title">设计工具与教育背景</h2>
        </div>

        <div class="tool-grid">
          <article>
            <h3>UI / Prototype</h3>
            <p>Sketch, Axure, PXCook</p>
          </article>
          <article>
            <h3>Visual</h3>
            <p>Photoshop, Illustrator, After Effects, C4D</p>
          </article>
          <article>
            <h3>Thinking</h3>
            <p>XMind</p>
          </article>
          <article>
            <h3>Education</h3>
            <p>北京吉利大学 · 艺术设计 · 本科</p>
          </article>
        </div>
      </section>
    </main>

    <footer class="contact" id="contact">
      <div>
        <p class="eyebrow">Contact</p>
        <h2>让作品讨论回到具体问题</h2>
        <p>如果你正在寻找能将产品流程、视觉规范和开发协作串起来的 UI 设计师，可以直接联系。</p>
      </div>
      <address>
        <a href="tel:18801378561">188-0137-8561</a>
        <a href="mailto:18801378561@163.com">18801378561@163.com</a>
      </address>
    </footer>
  </body>
</html>
```

- [ ] **Step 2: Run tests and confirm CSS-related failure remains**

Run:

```bash
python3 -m unittest tests.site_smoke -v
```

Expected: tests still fail because `styles.css` does not exist yet.

- [ ] **Step 3: Commit semantic HTML**

Run:

```bash
git add index.html
git commit -m "feat: add portfolio page content"
```

Expected: commit succeeds with only `index.html`.

---

### Task 3: Add Product-System Styling

**Files:**
- Create: `styles.css`
- Test: `tests/site_smoke.py`

- [ ] **Step 1: Create the CSS**

Create `styles.css` with this complete content:

```css
:root {
  color-scheme: light;
  --ink: #122019;
  --muted: #59645d;
  --surface: #f3f0e7;
  --surface-strong: #e5eadf;
  --paper: #fbfaf5;
  --accent: #2d5a43;
  --accent-soft: #cbd8c8;
  --line: rgba(18, 32, 25, 0.18);
  --shadow: 0 24px 70px rgba(18, 32, 25, 0.12);
  --max: 1180px;
  --space-page: clamp(20px, 4vw, 56px);
  --space-section: clamp(64px, 9vw, 128px);
  --font-display: "Avenir Next", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  --font-body: "Source Han Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background:
    radial-gradient(circle at 12% 10%, rgba(203, 216, 200, 0.7), transparent 28rem),
    linear-gradient(135deg, var(--paper), var(--surface));
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.65;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(18, 32, 25, 0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(18, 32, 25, 0.035) 1px, transparent 1px);
  background-size: 44px 44px;
  mask-image: linear-gradient(to bottom, black, transparent 72%);
}

a {
  color: inherit;
}

.site-header,
.hero,
.capabilities,
.cases,
.experience,
.toolkit,
.contact {
  width: min(var(--max), calc(100% - var(--space-page) * 2));
  margin-inline: auto;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 18px 0;
  backdrop-filter: blur(18px);
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}

.brand-mark {
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border: 1px solid var(--ink);
  background: var(--ink);
  color: var(--paper);
  font-weight: 800;
  letter-spacing: 0.06em;
}

.brand strong,
.brand small {
  display: block;
}

.brand strong {
  font-size: 1rem;
}

.brand small,
.eyebrow,
.panel-label,
.case-platform {
  color: var(--muted);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.site-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.site-nav a {
  border: 1px solid transparent;
  padding: 8px 12px;
  color: var(--muted);
  text-decoration: none;
}

.site-nav a:hover,
.site-nav a:focus-visible {
  border-color: var(--line);
  color: var(--ink);
  background: rgba(255, 255, 255, 0.5);
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(320px, 0.85fr);
  gap: clamp(28px, 6vw, 76px);
  align-items: end;
  min-height: calc(100vh - 86px);
  padding: clamp(48px, 8vw, 108px) 0 var(--space-section);
}

.hero-copy h1 {
  max-width: 860px;
  margin: 14px 0 0;
  font-family: var(--font-display);
  font-size: clamp(3rem, 8vw, 7.6rem);
  font-weight: 850;
  letter-spacing: 0;
  line-height: 0.96;
}

.hero-intro {
  max-width: 710px;
  margin: 28px 0 0;
  color: var(--muted);
  font-size: clamp(1rem, 1.5vw, 1.18rem);
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 34px;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  border: 1px solid var(--ink);
  padding: 0 18px;
  text-decoration: none;
  transition: transform 180ms ease, background 180ms ease, color 180ms ease;
}

.button:hover {
  transform: translateY(-2px);
}

.button.primary {
  background: var(--ink);
  color: var(--paper);
}

.button.secondary {
  background: transparent;
}

.hero-panel {
  border: 1px solid var(--line);
  background: rgba(251, 250, 245, 0.72);
  padding: clamp(22px, 3vw, 34px);
  box-shadow: var(--shadow);
}

.hero-panel h2 {
  margin: 8px 0 12px;
  font-size: clamp(1.7rem, 3vw, 2.5rem);
  line-height: 1.05;
}

.quick-facts {
  display: grid;
  gap: 14px;
  margin: 28px 0 0;
}

.quick-facts div {
  border-top: 1px solid var(--line);
  padding-top: 12px;
}

.quick-facts dt {
  color: var(--muted);
  font-size: 0.78rem;
  text-transform: uppercase;
}

.quick-facts dd {
  margin: 3px 0 0;
  font-weight: 750;
}

.capabilities {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding-bottom: var(--space-section);
}

.capabilities span,
.tag-list li {
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.45);
  padding: 8px 11px;
  color: var(--muted);
  font-size: 0.85rem;
}

.section-heading {
  display: grid;
  grid-template-columns: minmax(180px, 0.36fr) minmax(0, 0.64fr);
  gap: 28px;
  margin-bottom: 28px;
}

.section-heading h2 {
  margin: 0;
  font-size: clamp(2.1rem, 4vw, 4.2rem);
  line-height: 1;
}

.section-heading p:last-child {
  margin: 0;
  color: var(--muted);
}

.cases,
.experience,
.toolkit {
  padding: var(--space-section) 0;
  border-top: 1px solid var(--line);
}

.lead-case {
  border: 1px solid var(--ink);
  background: var(--paper);
}

.case-meta {
  display: grid;
  grid-template-columns: minmax(240px, 0.42fr) minmax(0, 0.58fr);
  gap: 24px;
  padding: clamp(24px, 4vw, 42px);
  border-bottom: 1px solid var(--ink);
}

.case-meta h3 {
  margin: 0;
  font-size: clamp(2rem, 4vw, 4.8rem);
  line-height: 0.96;
}

.case-meta p:last-child {
  margin: 0;
  color: var(--muted);
}

.case-story {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.case-story section {
  min-height: 260px;
  padding: clamp(22px, 3vw, 34px);
}

.case-story section + section {
  border-left: 1px solid var(--line);
}

.step-number {
  display: inline-block;
  margin-bottom: 36px;
  color: var(--accent);
  font-weight: 850;
}

.case-story h4 {
  margin: 0 0 12px;
  font-size: 1.55rem;
}

.case-story p,
.case-card p,
.timeline p,
.tool-grid p,
.contact p {
  color: var(--muted);
}

.process-line {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  margin: 0;
  padding: 0;
  list-style: none;
  border-top: 1px solid var(--line);
}

.process-line li {
  padding: 14px;
  font-size: 0.82rem;
  font-weight: 750;
  text-align: center;
}

.process-line li + li {
  border-left: 1px solid var(--line);
}

.selected-cases {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-top: 16px;
}

.case-card,
.tool-grid article {
  border: 1px solid var(--line);
  background: rgba(251, 250, 245, 0.68);
  padding: 22px;
  transition: border-color 180ms ease, transform 180ms ease, background 180ms ease;
}

.case-card:hover {
  border-color: var(--accent);
  background: var(--paper);
  transform: translateY(-3px);
}

.case-card h3,
.tool-grid h3,
.timeline h3 {
  margin: 6px 0 10px;
  font-size: 1.35rem;
  line-height: 1.15;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin: 20px 0 0;
  padding: 0;
  list-style: none;
}

.timeline {
  display: grid;
  gap: 0;
  border-top: 1px solid var(--line);
}

.timeline article {
  display: grid;
  grid-template-columns: minmax(180px, 0.28fr) minmax(0, 0.72fr);
  gap: 28px;
  padding: 26px 0;
  border-bottom: 1px solid var(--line);
}

.timeline time {
  color: var(--accent);
  font-weight: 850;
}

.role {
  margin-top: -4px;
}

.tool-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.contact {
  display: grid;
  grid-template-columns: minmax(0, 0.62fr) minmax(260px, 0.38fr);
  gap: 28px;
  align-items: end;
  padding: var(--space-section) 0 clamp(36px, 6vw, 72px);
  border-top: 1px solid var(--line);
}

.contact h2 {
  margin: 0;
  font-size: clamp(2rem, 4vw, 4.5rem);
  line-height: 1;
}

address {
  display: grid;
  gap: 10px;
  font-style: normal;
}

address a {
  border-bottom: 1px solid var(--line);
  padding-bottom: 10px;
  color: var(--ink);
  font-size: clamp(1rem, 2vw, 1.35rem);
  text-decoration: none;
}

address a:hover {
  color: var(--accent);
}

:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

@media (max-width: 960px) {
  .hero,
  .case-meta,
  .section-heading,
  .contact {
    grid-template-columns: 1fr;
  }

  .hero {
    min-height: auto;
  }

  .case-story,
  .selected-cases,
  .tool-grid {
    grid-template-columns: 1fr 1fr;
  }

  .case-story section:nth-child(3) {
    grid-column: 1 / -1;
    border-left: 0;
    border-top: 1px solid var(--line);
  }
}

@media (max-width: 760px) {
  .site-header {
    position: static;
    align-items: flex-start;
    flex-direction: column;
  }

  .site-nav {
    width: 100%;
    justify-content: space-between;
  }

  .site-nav a {
    padding-inline: 0;
  }

  .hero-copy h1 {
    font-size: clamp(2.7rem, 15vw, 4.4rem);
  }

  .case-story,
  .selected-cases,
  .tool-grid,
  .timeline article,
  .process-line {
    grid-template-columns: 1fr;
  }

  .case-story section + section,
  .case-story section:nth-child(3),
  .process-line li + li {
    border-left: 0;
    border-top: 1px solid var(--line);
  }

  .case-story section {
    min-height: auto;
  }

  .process-line li {
    text-align: left;
  }

  .button {
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

- [ ] **Step 2: Run smoke tests and confirm they pass**

Run:

```bash
python3 -m unittest tests.site_smoke -v
```

Expected: PASS, all 6 tests pass.

- [ ] **Step 3: Commit styling**

Run:

```bash
git add styles.css
git commit -m "feat: style portfolio case study page"
```

Expected: commit succeeds with `styles.css`.

---

### Task 4: Local Browser Verification

**Files:**
- Modify only if visual QA finds a concrete defect: `index.html`, `styles.css`
- Test: `tests/site_smoke.py`

- [ ] **Step 1: Start a local static server**

Run:

```bash
python3 -m http.server 4173
```

Expected: terminal prints a serving message for port `4173`. Keep this session running until verification is complete.

- [ ] **Step 2: Open the page in the in-app browser**

Open:

```text
http://localhost:4173
```

Expected: the page loads and the first viewport shows Zhou Yueqi, the UI Designer role, the positioning line, and the case-study summary panel.

- [ ] **Step 3: Verify desktop layout**

Check at a desktop viewport:

- Header navigation is visible and not overlapping.
- Hero text does not clip.
- Capability chips wrap cleanly.
- Lead case has Problem, Process, and Result modules.
- Selected case cards align as a three-column grid.
- Contact phone and email links are visible.

If a defect is found, fix the smallest affected CSS or HTML section, then rerun:

```bash
python3 -m unittest tests.site_smoke -v
```

Expected: PASS after any adjustment.

- [ ] **Step 4: Verify mobile layout**

Use a mobile-width viewport around `390px`.

Check:

- Header stacks without overlap.
- Hero CTA buttons are full width.
- Lead case modules stack vertically.
- Process line stacks vertically and remains readable.
- Case cards, timeline, toolkit, and contact all fit without horizontal scrolling.

If a defect is found, fix the smallest affected CSS section, then rerun:

```bash
python3 -m unittest tests.site_smoke -v
```

Expected: PASS after any adjustment.

- [ ] **Step 5: Commit visual QA fixes if needed**

If no fixes were needed, skip this step.

If fixes were made, run:

```bash
git add index.html styles.css tests/site_smoke.py
git commit -m "fix: refine responsive portfolio layout"
```

Expected: commit succeeds with only the necessary files.

---

### Task 5: Final Verification And Handoff

**Files:**
- No planned file changes.

- [ ] **Step 1: Run the full smoke test suite**

Run:

```bash
python3 -m unittest tests.site_smoke -v
```

Expected: PASS, all 6 tests pass.

- [ ] **Step 2: Check git status**

Run:

```bash
git status --short
```

Expected: no unstaged implementation changes. Ignored `.superpowers/` and `tmp/` should not appear.

- [ ] **Step 3: Provide delivery summary**

Report:

- Created `index.html`, `styles.css`, and `tests/site_smoke.py`.
- Confirmed smoke tests pass.
- Confirmed desktop and mobile browser layouts were inspected.
- Provide local URL used during verification, usually `http://localhost:4173`.

---

## Self-Review

Spec coverage:

- Case-led portfolio: covered by Tasks 2 and 3.
- Design-lead audience: covered by hero, lead case, selected cases, and capability strip in Task 2.
- Problem-process-result structure: covered by lead case HTML and tests in Tasks 1 and 2.
- Product-system visual direction: covered by CSS variables, grid, labels, and responsive rules in Task 3.
- Contact details: covered by HTML and contact link tests.
- Accessibility and reduced motion: covered by semantic structure, focus styles, and reduced-motion CSS test.
- Responsive verification: covered by Task 4.

Completeness scan:

- No unresolved implementation gaps are intentionally included.

Type and naming consistency:

- Section IDs in `index.html` match tests in `tests/site_smoke.py`.
- CSS file name in `index.html` matches `styles.css`.
- Contact href values match smoke tests.
