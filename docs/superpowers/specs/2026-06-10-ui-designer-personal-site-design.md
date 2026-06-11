# UI Designer Personal Site Design

## Summary

Build a personal portfolio site for Zhou Yueqi, a UI designer whose resume emphasizes mobile app UI, web UI, brand/operation visuals, and collaboration with product and development teams.

The site should not be a direct web version of the PDF resume. It should be a case-led portfolio for design leads who need to quickly judge product thinking, visual execution, process maturity, and delivery reliability.

## Source Material

- Resume PDF: `/Users/Yan17/Desktop/1331.pdf`
- Candidate: Zhou Yueqi
- Target role: UI Designer
- Experience: 3+ years in UI, web, mobile app, graphic, and brand visual design
- Education: Beijing Geely University, Art Design, Bachelor, 2011.09-2015.06
- Core tools mentioned: Sketch, Photoshop, Illustrator, After Effects, Axure, XMind, PXCook, C4D

## Audience

Primary audience: design leads and hiring managers who review UI portfolios.

They should be able to answer three questions quickly:

1. Has this designer worked on real product surfaces, not only static visuals?
2. Can she explain design decisions through problem, process, and result?
3. Can she collaborate with PMs and developers to ship usable interfaces?

Secondary audience: HR or recruiters who need basic role fit, contact details, and career history.

## Positioning

Primary positioning statement:

> Designing clear, usable mobile and web experiences for complex services.

Chinese display copy direction:

> 把复杂服务设计成清晰可用的移动与网页体验

The tone should communicate maturity, clarity, and product sensibility. It should avoid feeling like a decorative resume template.

## Approved Direction

The approved concept combines:

- Site type: case-led portfolio
- Audience: design leads
- Homepage structure: problem-process-result case narrative
- Visual tone: product system, rational, clear

## Content Strategy

Use the resume as raw material, then rewrite for web.

Keep:

- Name
- UI Designer role
- Core design capabilities
- Representative projects
- Work history
- Education
- Contact details

De-emphasize or omit from primary UI:

- Age
- Expected salary
- Current employment status
- Generic long self-evaluation bullets that repeat the same capability

These fields can be excluded entirely unless the user later requests a traditional resume section.

## Representative Projects

### 1. CCB Life / Jianxin Property Insurance App

Resume source name: 建信财险 APP

Use as the lead case because it has the strongest product-service context.

Case framing:

- Problem: insurance services are dense, procedural, and easy for users to abandon when flows are unclear.
- Process: translate requirements into iOS and Android UI, balance usability with refined visual design, discuss key product improvements, refine high-fidelity flows, and collect feedback.
- Result: a more structured mobile insurance service covering online insurance purchase, policy service, and health management.

### 2. Trust Mutual / Xinmei Mutual App

Resume source name: 信美相互 APP

Case framing:

- Problem: traditional insurance needed a clearer internet-facing product experience.
- Process: collaborate with PMs, analyze user habits, create visual style from interaction prototypes, define app visual rules, and deliver high-fidelity screens.
- Result: clearer insurance flow, customized product presentation, and a more understandable application experience.

### 3. Lafeng Comics App

Resume source name: 拉风漫画 APP

Case framing:

- Problem: a community app for young comics users needed approachable mobile UI and iconography.
- Process: design visual and interaction layers from prototypes, create screens and icons, support frontend/backend engineers with sliced assets and revisions.
- Result: a complete mobile interface direction for a community and creation platform.

### 4. Web And Brand Visual Work

Resume source names: 拉斯维斯官网 PC 端, 疯狂小狗官网 PC 端, advertising and brand work

Case framing:

- Problem: brand and marketing surfaces need consistent visual communication across website, social media, posters, brochures, and campaign materials.
- Process: create website layouts, promotional visuals, DM flyers, posters, brochures, and brand assets based on planning goals.
- Result: broader visual design capability beyond app UI, useful for cross-platform product teams.

## Homepage Information Architecture

### 1. Hero

Purpose: make the candidate's product design positioning clear in the first viewport.

Content:

- Name: 周月琪
- Role: UI Designer
- Positioning line: 把复杂服务设计成清晰可用的移动与网页体验
- Supporting copy: 3 年+ UI / Web / 移动端设计经验，参与保险服务 App、社区产品、官网与品牌视觉设计，从用户流程、视觉规范到开发交付推进界面落地。
- Primary CTA: 查看精选案例
- Secondary CTA: 联系我

Avoid large generic slogans.

### 2. Capability Strip

Purpose: give design leads a fast capability scan.

Suggested capability labels:

- Mobile UI
- Interaction Flow
- Visual System
- Web Design
- Brand Visual
- PM / Dev Collaboration

### 3. Lead Case Section

Purpose: demonstrate the problem-process-result model immediately.

Use 建信财险 APP as the lead case. Show it as a large editorial/product-system block with three columns or three stacked modules:

- Problem
- Process
- Result

Include a small process line:

Research / Prototype / Visual Design / Spec / Delivery

### 4. Selected Cases

Purpose: show range without overwhelming the page.

Use compact case cards for:

- 信美相互 APP
- 拉风漫画 APP
- 官网与品牌视觉项目

Each card should show:

- Project name
- Platform
- One-line problem
- Key contribution
- Tags

### 5. Work History

Purpose: provide credibility and chronology without turning the page into a resume dump.

Show:

- 2016.11-2018.12, 天津易商阜级科技股份有限公司, 美术设计师
- 2015.06-2016.11, 北京蓝正合融广告有限公司, 平面设计师

Summarize responsibilities in short, rewritten bullets.

### 6. Design Toolkit And Education

Purpose: support qualifications.

Show tools as concise grouped chips:

- UI / Prototype: Sketch, Axure, PXCook
- Visual: Photoshop, Illustrator, After Effects, C4D
- Thinking: XMind

Education:

- 北京吉利大学, 艺术设计, 本科

### 7. Contact

Purpose: make outreach easy.

Show:

- Phone: 188-0137-8561
- Email: 18801378561@163.com

Do not submit or transmit contact details to any third-party service from the site.

## Visual Direction

Use a product-system visual language:

- Light background, slightly warm or green-tinted neutral
- Deep green or ink-like primary color
- Crisp grid layout
- Modular case blocks
- Clear labels and step markers
- Strong typographic hierarchy
- Minimal decoration

Avoid:

- Purple/blue AI gradients
- Decorative glowing dark mode
- Generic card grids with icons above every title
- Resume-template styling copied from the PDF
- Overly playful portfolio aesthetics

The final page should feel like a mature case study, not a poster.

## Interaction

Keep interactions purposeful and restrained:

- Anchor navigation for sections
- CTA scroll to selected cases
- Hover states on case cards
- Optional subtle entrance motion for case modules
- Respect `prefers-reduced-motion`

No modals are needed.

## Responsive Behavior

Desktop:

- Use a wide grid with asymmetry between hero copy and case summary.
- Lead case can use side-by-side modules.

Tablet:

- Collapse to a two-column or stacked flow.
- Preserve case labels and process steps.

Mobile:

- Prioritize name, role, positioning, and first case.
- Stack modules vertically.
- Keep contact actions visible and tappable.

No critical content should be hidden on mobile.

## Accessibility

Requirements:

- Semantic HTML landmarks: header, main, section, footer
- Real text for all content, not image-only text
- Sufficient contrast for all labels and body text
- Keyboard-focusable links and buttons
- Descriptive link labels
- Reduced-motion support

## Technical Scope

The repository is currently empty except for git metadata and temporary brainstorming files.

The initial implementation can be a static single-page site unless the user requests a framework. A minimal static implementation is enough for this project:

- `index.html`
- `styles.css`
- Optional `script.js` only for small interactions

No backend, CMS, authentication, analytics, form submission, or external data storage is required.

## Testing And Verification

Manual checks:

- Open the site locally in a browser.
- Verify desktop and mobile layouts.
- Confirm no text overlaps or clips.
- Confirm contact links work.
- Confirm reduced-motion behavior does not rely on animation for comprehension.

Automated or scripted checks, if tooling is added:

- HTML validation where available
- Accessibility smoke test
- Basic screenshot inspection on desktop and mobile

## Out Of Scope

- Multi-page CMS
- Blog
- Downloadable PDF generation
- Contact form backend
- External analytics
- Real app screenshots not present in the provided resume
- Reconstructing private project visuals without source assets

## Open Questions

These can be resolved during implementation if needed:

1. Should the site include English labels alongside Chinese copy?
2. Should contact details be shown directly or behind a copy-to-clipboard interaction?
3. Should the implementation remain plain HTML/CSS, or should it use a frontend framework?

## Review Notes

This spec was written after user approval of the design direction. The Superpowers brainstorming workflow requests a subagent spec-review loop, but the current tool policy only allows spawning subagents when the user explicitly asks for subagents. A local self-review should be performed before implementation planning.
