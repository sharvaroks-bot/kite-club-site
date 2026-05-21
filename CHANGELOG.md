# CHANGELOG — Kite Club Koh Phangan Website

---

## [v3.17.0] — 2026-05-21 (current)

### Critical fix
- Removed ALL rescue boat claims from 13 pages — rescue boat does not currently exist. Replaced with: instructor supervision, safety monitoring, beach safety support, launch & landing assistance.

### Wind Center page — /seasons/ enhanced
- Cinematic hero (90vh, wind-in H1, 4-stat overlay: 18-28 kts / Jan-Apr / 90% / Jun-Sep)
- "What to Ride Today?" 3-column decision guide (6-12 kts / 12-18 kts / 18+ kts)
- Spots by Season section: Thong Sala, Baan Tai, Chaloklum (depth, wind dir, season, skill)
- Local knowledge timing block (NE vs SW morning window)
- Windy.com + Windguru forecast links

### Homepage additions
- "Ride Today / Today in Koh Phangan" section — 3 sport tiles with season status badge
- 2 new FAQ entries: "How long to learn kitesurfing?" + "Is Koh Phangan good for beginners?"
- Schema: fixed grammar bug; added 2 new FAQPage entries for AI-search

### New page — /compare/ (sport comparison)
- Kitesurfing vs Wing Foil vs Windsurfing vs E-Foil
- 4 sport cards with full specs (wind, learning time, speed, fitness, price)
- 12-criteria comparison table
- "Choose Your Sport if…" guide (4 decision boxes)
- FAQPage schema with 5 questions

### /locations/ — GEO authority expansion
- 3 spot cards: Thong Sala (beginner, NE, Jan-Apr), Baan Tai (intermediate, SW, Jun-Sep), Chaloklum (advanced, both seasons)
- Spot data: depth, wind direction, peak season, skill level, downwind run
- Ferry & getting-here section: Bangkok, Koh Samui, pier-to-school walk
- Updated title + meta description

### /sitemap.xml updated
- Added /compare/ (priority 0.8)

---

## [Unreleased] — in progress

### Added
- `SEO_AUDIT.md` — full audit of old site vs new site
- `COMPETITOR_ANALYSIS.md` — deep analysis of 5 competitors
- `MIGRATION_MAP.md` — full URL migration strategy for 53+ indexed URLs
- `_redirects` — Netlify 301 redirect file for all old WordPress URLs
- `TODO.md` — prioritised implementation plan

---

## [v3.7.0] — 2026-05-20

### Lesson Pages — WhatsApp pre-fill CTAs (17 pages)
- All lesson pages: `wa.me/66967203910` → `wa.me/66967203910?text=COURSE_MSG`
- Course-specific messages with name, duration, and price pre-filled
- Affects: all kitesurfing, wing foil, windsurfing, efoil lesson pages

### Lesson Pages — No-Wind Rescheduling Badge (13 pages)
- Added `✓ No wind = rescheduled at no extra charge` badge before booking buttons
- Applied to all wind-dependent lessons (kitesurfing, wing foil, windsurfing)
- Skipped: efoil pages (motor-powered, no wind dependency)

### Lesson Listing Pages — AggregateRating Schema (4 pages)
- Added `AggregateRating` (5.0 / 47 reviews) to @graph on:
  - `/kitesurfing/lessons/`, `/wing-foil/lessons/`, `/windsurfing/lessons/`, `/efoil/lessons/`

### New Pages
- `/seasons/index.html` — wind calendar targeting "koh phangan kite season"
  - Schema: EducationalOrganization + BreadcrumbList + FAQPage
  - Sections: 3 season cards, 12-month activity table, FAQ, CTA
- `/kitesurfing/thong-sala/index.html` — micro-GEO targeting "kitesurfing thong sala beach"
  - Schema: EducationalOrganization + BreadcrumbList + FAQPage + Place (GeoCoordinates)
  - Sections: hero, stat boxes, about-spot, course cards, FAQ, CTA

### New Blog Posts (7)
- `guide-kitesurfing-thailand.html` — Complete guide to kitesurfing in Thailand
- `kitesurfing-for-kids.html` — Family guide, kids kitesurfing age 12+
- `kitesurfing-vs-wing-foil.html` — Comparison for beginners
- `what-equipment-is-included.html` — Full equipment breakdown
- `kitesurf-rental-koh-phangan.html` — Rental guide for independent riders
- `wing-foil-guide-thailand.html` — Wing foil complete guide
- `efoil-guide-koh-phangan.html` — E-foil experience guide

### sitemap.xml
- Updated to 66 URLs (added /seasons/, /kitesurfing/thong-sala/, 7 blog posts)

---

## [v3.6.0] — 2026-05-20

### New Pages — High-Priority SEO pages (Phase 9–11)
- `/kitesurfing/koh-phangan/index.html` — GEO landing page targeting "kitesurfing koh phangan"
  - Schema: EducationalOrganization + BreadcrumbList + FAQPage
  - Sections: video hero, wind season cards (NE/SW), Thong Sala about-band, 3 course cards, 2-column SEO text, FAQ, CTA
- `/best-kitesurf-spots-koh-phangan/index.html` — spots guide targeting "best kitesurf spots koh phangan"
  - Schema: Article + BreadcrumbList + FAQPage
  - Sections: 4-spot comparison perks, Thong Sala about-band, Ban Tai + Chaloklum 2-column, HTML comparison table, FAQ, internal links grid, CTA
- `/best-time-kitesurfing-koh-phangan/index.html` — season guide targeting "best time kitesurfing koh phangan"
  - Schema: Article + BreadcrumbList + FAQPage (4 wind-season questions)
  - Sections: hero, 2-column season cards (NE/SW with stats grids), 12-month wind table with ratings, "Which Season is Right For You?" 3-card panel, 2-column SEO text, FAQ (5 questions), internal links, CTA
- `sitemap.xml` — updated to 48 URLs (3 new pages at priority 0.8–0.85)

---

## [v3.5.0] — 2026-05-20

### kitesurfing/lessons/index.html — 14 UX + SEO improvements
- Title: → "Kitesurfing Lessons Koh Phangan | IKO School & Beginner Courses"
- Meta desc: rewritten with target keywords (Thong Sala, IKO, private & group, prices)
- og:url: fixed (was incorrectly pointing to /school/kitesurfing/)
- Schema: added BreadcrumbList (3 levels) + FAQPage (9 questions) to JSON-LD graph
- H1: → "Kitesurfing Lessons in Koh Phangan"
- Hero paragraph: updated with location + price keyword
- Course grid: added "Beginner Courses" / "Private Coaching" group headings
- Added "Best for:" tag to all 6 course cards
- Added "What's Included" 8-item grid section (kite, board, helmet, radio, instructor, boat, insurance, IKO cert)
- "Result Guaranteed" perk → "Clear Progression" (honest, IKO-method description)
- Added Thong Sala Beach GEO section (stats: 28°C, 15-25kn, Jan-Apr, Flat)
- FAQ expanded: 5 → 9 questions (added: no experience, no wind policy, kids, same-day booking)
- CTA: "Ready to Learn to Kitesurf?" with WhatsApp pre-filled messages
- Reviews: "⭐ Google Reviews — 5.0 · 47 reviews" label
- Added "Also at Kite Club" 6-card internal links section (wing foil, efoil, windsurf, rental, safari, map)
- CSS: new components for cc-group-head, cc-best-for, inc-band, geo-band, also-band

---

## [v3.4.0] — 2026-05-20 (previous session)

### Global — SEO meta coverage
- og:image added to 37 pages
- geo.placename added to 36 pages
- Course schema (ItemList + Course) on 4 lesson listing pages

### Homepage (index.html)
- New title + JSON-LD (LocalBusiness + WebSite + FAQPage)
- og:image + Twitter cards
- geo.placename + hreflang x-default
- H1 → "Learn to Kitesurf in Thailand"
- Removed About band and excess desktop sections
- Mobile cards: replaced autoplay videos with lazy images
- Added visible .seo-block section
- Fixed `<button href="">` → `<a>` tag

### robots.txt
- Added Allow for: GPTBot, Google-Extended, PerplexityBot, ClaudeBot

### sitemap.xml
- lastmod: 2026-05-20 on all 45 URLs
- Priority hierarchy: homepage (1.0), activity pages (0.8), lesson pages (0.7), blog (0.6)

---

## [v3.3.0] — 2026-05-19 (previous session)

### Global — Luxury button effects (all 46 pages)
- btn-p: shimmer effect (::after with skewX -20deg)
- btn-s: fill animation + border glow
- cc-btns equal-size fix: box-sizing:border-box + min-width:0

### Course listing pages (wing-foil/lessons/, windsurfing/lessons/, efoil/lessons/)
- cc-list bullets: fixed &amp; encoding bug
- Button order: btn-s left, btn-p (Book Now) right

### Asset fixes
- Replaced missing live-*.jpg images
- wingfoil-mobile.mp4 → desktop video
- windsurf-*.mp4 → windsurfing-desktop.mp4
- E-foil hero: video → static image

---

## [v3.2.0] — 2026-05-18 (previous session)

### 14 individual course pages
- lesson-copy replaced with structured h3+ul phase content (beach/water session, logistics)
- course-actions buttons: removed flex-wrap:wrap, added flex:1 + text-align:center

---

## [v3.1.0] — 2026-05-17 (initial session)

### Site foundation
- 46 HTML pages created (static export structure)
- Navigation with dropdown menus on all pages
- Light/dark theme toggle on all pages
- WhatsApp floating button on all pages
- Video heroes on activity pages
- Blog page with 6 posts
- Sitemap.xml and robots.txt created
