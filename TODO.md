# TODO — Kite Club Koh Phangan Website
**Created:** 2026-05-20 | **Phase:** Post-audit implementation

---

## 🔴 CRITICAL — Do Before Migration (Pre-Launch)

### SEO Migration (blocking)
- [x] Create `_redirects` file (Netlify) — 53 blog post URLs + 3 page URL changes
- [ ] Verify `netlify.toml` has NO catch-all SPA redirect (known bug)
- [ ] Verify `.nojekyll` exists at repo root (GitHub Pages)
- [ ] Audit sitemap.xml — add all new pages, remove old WordPress URLs
- [ ] Verify all canonical tags point to `https://kiteclubkohphangan.com/` (not github.io)
- [ ] Verify hreflang on all pages points to production domain
- [ ] Confirm og:url tags use production domain on all pages

### Price Discrepancy (blocking)
- [ ] VERIFY WITH CLIENT: Discovery Course price — 3,500 THB (new site) vs 4,000 THB (old site)
- [ ] VERIFY WITH CLIENT: Independent Rider — 18,000 THB (new) vs 14,000 THB (old)
- [ ] Update all prices consistently across ALL pages after verification
- [ ] Update schema Offer prices to match

### Internal Link Audit (blocking)
- [ ] Search all pages for links to `/windsurfing-2/` → update to `/windsurfing/`
- [ ] Search all pages for links to `/supboard-rental/` → update to `/sup-rental/`
- [ ] Search all pages for links to `/membership-storage/` → update to `/storage/`
- [ ] Verify footer links on all 46 pages use correct slugs

---

## 🟠 HIGH PRIORITY — First 2 Weeks

### New Pages to Create
- [ ] `/kitesurfing/koh-phangan/` — GEO landing page (match Kiteflip's #1 strategy)
- [ ] `/best-kitesurf-spots-koh-phangan/` — spots guide (high search intent)
- [ ] `/best-time-kitesurfing-koh-phangan/` — season guide (high search intent)
- [ ] `/faq/` — central FAQ page (AI search optimisation)
- [ ] `/pricing/` — pricing overview page (search intent: "kitesurfing koh phangan price")

### Blog Content Migration (highest value posts)
- [ ] `/blog/posts/best-time-koh-phangan.html` — absorb 3 old "best time" posts
- [ ] `/blog/posts/kitesurf-spots-koh-phangan.html` — absorb 4 old "spots" posts
- [ ] `/blog/posts/beginner-guide-koh-phangan.html` — absorb 3 old "beginner" posts
- [ ] `/blog/posts/complete-guide-koh-phangan.html` — comprehensive pillar post
- [ ] `/blog/posts/koh-phangan-vs-samui.html` — comparison (ranking opportunity)
- [ ] `/blog/posts/how-long-to-learn.html` — "how long does it take" query
- [ ] `/blog/posts/first-lesson-guide.html` — "what to expect" query

### Schema Improvements
- [ ] Add `Review` + `AggregateRating` schema to pages with star reviews
- [ ] Add `LocalBusiness` schema to contacts page
- [ ] Add `FAQPage` schema to /faq/ page
- [ ] Add `Course` schema to all individual lesson pages
- [ ] Verify BreadcrumbList on all lesson pages

---

## 🟡 MEDIUM PRIORITY — First Month

### GEO SEO Pages
- [ ] `/kitesurfing/thong-sala/` — micro-GEO for Thong Sala Beach
- [ ] `/locations/` — expand with interactive map, all 3 season locations
- [ ] `/seasons/` — dedicated wind calendar page (month-by-month)

### Content Improvements
- [ ] Kitesurfing homepage (`/kitesurfing/`) — add "success rate" claim
- [ ] All activity pages — add "season window" info block
- [ ] All school pages — add instructor profiles section
- [ ] Add "no-wind policy" to all lesson pages
- [ ] Add Google Review widget/placeholder to all pages with reviews

### Blog — Fill Content Gaps
- [ ] "Complete guide to kitesurfing in Thailand" — matches Kiteflip's key content
- [ ] "Kitesurfing for kids on Koh Phangan"
- [ ] "Kitesurfing vs wing foil — which should beginners choose"
- [ ] "What equipment is included in lessons"
- [ ] "Kitesurf rental guide Koh Phangan"
- [ ] "Wing foil complete guide Thailand"
- [ ] "E-foil experience Koh Phangan guide"

### Conversion Improvements
- [ ] Add "no-wind = reschedule" guarantee text to all lesson pages
- [ ] Add pre-filled WhatsApp message links (already done on kitesurfing/lessons)
- [ ] Add booking calendar widget placeholder
- [ ] Ensure all CTA buttons use WhatsApp pre-fill on ALL lesson pages

---

## 🟢 LOWER PRIORITY — First 90 Days

### New Service Pages
- [ ] `/kite-safari-egypt/` — Egypt destination (mentioned in brief, currently missing)
- [ ] `/kitesurfing/courses/` — topical overview for kitesurfing courses
- [ ] `/wingfoil/` — alias redirect or landing for /wing-foil/ (search volume on "wingfoil")
- [ ] `/windsurfing/koh-phangan/` — GEO page for windsurfing
- [ ] `/wing-foil/koh-phangan/` — GEO page for wing foil

### Technical SEO
- [ ] Add `<link rel="preload">` for hero videos
- [ ] Convert all images to WebP format
- [ ] Add `loading="lazy"` to ALL images (audit)
- [ ] Add `width` and `height` attributes to all images (prevent CLS)
- [ ] Implement proper `<picture>` elements with AVIF/WebP
- [ ] Add `fetchpriority="high"` to LCP image on each page
- [ ] Minify all HTML files
- [ ] Audit and fix any broken internal links

### GEO & Local SEO
- [ ] Set up Google Business Profile (if not already)
- [ ] Ensure GBP matches website NAP: "+66 96 720 3910", "Thong Sala Beach"
- [ ] Add Google Maps embed to /contacts/ and /locations/
- [ ] Add structured data for events (seasonal lessons)

### AI Search Optimisation
- [ ] Audit all FAQ sections — ensure answers are self-contained (no "as mentioned above")
- [ ] Add `speakable` schema for voice search
- [ ] Create "About the school" entity page with clean factual data
- [ ] Ensure all schema entities link to each other (WebSite → LocalBusiness → Course)

### Content Authority Building
- [ ] Blog: "Why Koh Phangan for kitesurfing" (original research angle)
- [ ] Blog: "Wind data Koh Phangan 2026" (data-driven post)
- [ ] Blog: "IKO vs IWO certification explained"
- [ ] Blog: "Safety on the water: complete guide"
- [ ] Blog: "Kitesurfing for couples Koh Phangan"
- [ ] Blog: "How to choose the right kite size"

### Link Building Strategy
- [ ] Submit to: phanganist.com, kohphangan.com, tourismthailand.org
- [ ] Partner with local yoga retreats (wellness traveller angle)
- [ ] Partner with Koh Phangan travel bloggers
- [ ] Get listed on: Airbnb Experiences, GetYourGuide, Klook

---

## ✅ COMPLETED (this session)

- [x] Comprehensive SEO audit of old site (SEO_AUDIT.md)
- [x] Full competitor analysis — 5 competitors (COMPETITOR_ANALYSIS.md)
- [x] SEO migration map — all 53+ old URLs mapped (MIGRATION_MAP.md)
- [x] _redirects file created (Netlify 301 redirects)
- [x] kitesurfing/lessons/ page: 14 improvements (title, H1, schema, groups, FAQ, GEO, CTA)
- [x] Homepage: SEO rewrite (H1, schema, seo-block, og:image)
- [x] Global: og:image on 37 pages, geo.placename on 36 pages
- [x] Sitemap: lastmod 2026-05-20 + priority hierarchy
- [x] Robots.txt: Allow GPTBot, PerplexityBot, ClaudeBot
- [x] Blog posts: luxury button effects, cc-btns fixes across all pages
- [x] 14 individual course pages: structured h3+ul phase content
- [x] Button order standardised: btn-s left, btn-p right across all pages
- [x] Hero media: desktop/mobile videos fixed across all activity pages
