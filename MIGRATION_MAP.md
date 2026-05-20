# SEO MIGRATION MAP — Kite Club Koh Phangan
**Date:** 2026-05-20
**From:** kiteclubkohphangan.com (WordPress)
**To:** kiteclubkohphangan.com (Static HTML)

---

## CRITICAL PRINCIPLE
> Every old indexed URL must either:
> (A) Stay exactly the same on the new site, OR
> (B) Have a 301 redirect to the closest semantic match

**Never leave an indexed URL as a 404.**

---

## PART 1 — PAGE URL MIGRATION

### Direct Matches (same URL, no redirect needed)
| Old URL | New URL | Status |
|---------|---------|--------|
| / | / | ✅ Same |
| /wing-foil/ | /wing-foil/ | ✅ Same |
| /kayaking/ | /kayaking/ | ✅ Same |
| /contacts/ | /contacts/ | ✅ Same |
| /school/ | /school/ | ✅ Same |
| /efoil/ | /efoil/ | ✅ Same |
| /kite-safari/ | /kite-safari/ | ✅ Same |
| /locations/ | /locations/ | ✅ Same |
| /blog/ | /blog/ | ✅ Same |

### URL Slug Changes (301 redirects REQUIRED)
| Old URL | New URL | Reason |
|---------|---------|--------|
| /windsurfing-2/ | /windsurfing/ | Fixed slug |
| /supboard-rental/ | /sup-rental/ | Shortened slug |
| /membership-storage/ | /storage/ | Simplified slug |

### New Pages (no redirect needed, just crawl)
| New URL | Notes |
|---------|-------|
| /kitesurfing/ | New — not on old site |
| /kitesurfing/lessons/ | New — was inside /school/ |
| /kitesurfing/lessons/discovery-course/ | New |
| /kitesurfing/lessons/full-beginner-course/ | New |
| /kitesurfing/lessons/independent-course/ | New |
| /kitesurfing/lessons/refresh-lesson/ | New |
| /kitesurfing/lessons/pro-lesson/ | New |
| /kitesurfing/lessons/hydrofoil-lesson/ | New |
| /windsurfing/ | New (was /windsurfing-2/) |
| /windsurfing/lessons/ | New |
| /windsurfing/lessons/discovery-lesson/ | New |
| /windsurfing/lessons/beginner-course/ | New |
| /windsurfing/lessons/refresh-lesson/ | New |
| /wing-foil/lessons/ | New |
| /wing-foil/lessons/intro-lesson/ | New |
| /wing-foil/lessons/beginner-course/ | New |
| /wing-foil/lessons/advanced-course/ | New |
| /efoil/lessons/ | New |
| /efoil/lessons/intro-lesson/ | New |
| /efoil/lessons/efoil-lesson/ | New |
| /about/ | New |
| /rental/ | New |
| /sup-rental/ | New (was /supboard-rental/) |
| /storage/ | New (was /membership-storage/) |
| /courses/ | New |
| /school/kitesurfing/ | New |
| /school/wing-foil/ | New |
| /school/windsurfing/ | New |
| /school/efoil/ | New |

---

## PART 2 — BLOG POST MIGRATION (CRITICAL)

### Structure Change
- **Old:** `/post-title/` (WordPress root-level)
- **New:** `/blog/posts/post-title.html` (flat file)

### Blog Posts — Direct Matches (old post → new file)

| Old URL | New File | Match Quality |
|---------|----------|---------------|
| /from-kite-to-wing-why-experienced-kitesurfers-are-switching-to-wing-foil/ | /blog/posts/kite-to-wing.html | ✅ Strong |
| /family-holidays-why-wing-foiling-and-kitesurfing-are-the-perfect-combo-for-active-groups/ | /blog/posts/family-holidays.html | ✅ Strong |
| /top-10-common-mistakes-when-transitioning-from-kitesurfing-to-wing-foil/ | /blog/posts/top-10-mistakes.html | ✅ Strong |
| /kitesurfing-vs-wing-foiling-which-one-should-you-learn-first-on-koh-phangan/ | /blog/posts/first-kite-lesson.html | ⚠️ Loose |
| /wing-foil-vs-efoil-which-is-right-for-you/ | /blog/posts/efoil-vs-wing.html | ✅ Strong |
| /wind-seasons-on-koh-phangan-the-complete-calendar-for-kitesurfing-and-wing-foil-riders/ | /blog/posts/wind-season-2026.html | ✅ Strong |

### Blog Posts — No New Equivalent (redirect to /blog/ as fallback)

These 47 old posts have no equivalent in new site yet. **Redirect all to /blog/** until new versions are created:

| Priority | Old URL | Target Redirect | Future Action |
|----------|---------|-----------------|---------------|
| 🔴 | /best-time-to-kitesurf-on-koh-phangan-complete-monthly-wind-weather-guide/ | /blog/ | Create /blog/posts/best-time-koh-phangan.html |
| 🔴 | /best-kiteboarding-spots-in-koh-phangan/ | /blog/ | Create /blog/posts/kitesurf-spots-koh-phangan.html |
| 🔴 | /best-kite-spots-in-koh-phangan-for-beginners-safety-first-beach-rankings/ | /blog/ | Create /blog/posts/beginner-kite-spots.html |
| 🔴 | /the-complete-guide-to-kitesurf-in-koh-phangan-spots-seasons-kitesurfing-schools/ | /blog/ | Create /blog/posts/complete-guide-koh-phangan.html |
| 🔴 | /is-koh-phangan-good-for-learning-kitesurfing-honest-beginners-guide/ | /blog/ | Create /blog/posts/beginner-guide-koh-phangan.html |
| 🔴 | /how-long-does-it-take-to-learn-kitesurfing-or-wing-foiling-in-koh-phangan-honest-timelines-for-beginners/ | /blog/ | Create /blog/posts/how-long-to-learn.html |
| 🔴 | /when-is-the-best-time-for-kitesurfing-in-koh-phangan/ | /blog/ | → /blog/posts/wind-season-2026.html |
| 🔴 | /koh-phangan-vs-koh-samui-for-kitesurfing-which-island-should-you-choose/ | /blog/ | Create /blog/posts/koh-phangan-vs-samui.html |
| 🔴 | /what-to-expect-your-first-kitesurfing-lesson-on-koh-phangan/ | /blog/ | Create /blog/posts/first-lesson-guide.html |
| 🔴 | /what-to-expect-your-first-kitesurfing-lesson-in-koh-phangan/ | /blog/ | → same as above |
| 🟡 | /top-5-reasons-why-koh-phangan-is-the-best-place-for-kitesurfing/ | /blog/ | Create |
| 🟡 | /first-time-on-the-water-should-you-start-with-kitesurfing-or-wing-foiling-on-koh-phangan/ | /blog/ | Create |
| 🟡 | /how-many-days-does-it-actually-take-to-learn-kitesurfing-on-koh-phangan/ | /blog/ | → /blog/posts/wind-season-2026.html |
| 🟡 | /wing-foil-koh-phangan-how-to-start-with-wing-foil-rental-in-thailand/ | /wing-foil/lessons/ | Partial redirect |
| 🟡 | /efoil-board-lessons-koh-phangan-learn-to-fly-above-the-water-in-thailand/ | /efoil/lessons/ | Partial redirect |
| 🟡 | /what-kitesurfing-equipment-you-need-on-koh-phangan-tropical-conditions-guide/ | /blog/ | Create |
| 🟡 | /koh-phangan-for-the-active-wellness-traveller-combining-yoga-kitesurfing-and-wing-foiling-on-the-island/ | /blog/ | Create |
| 🟡 | /why-wing-foiling-is-the-fastest-growing-water-sport-in-the-world/ | /wing-foil/ | |
| 🟡 | /wing-foil-safety-essential-gear-and-tips-for-new-riders/ | /wing-foil/lessons/ | |
| 🟡 | /how-to-choose-your-first-wing-foil-board-on-koh-phangan-size-volume-and-stability/ | /wing-foil/lessons/ | |
| 🟡 | /top-5-common-beginner-mistakes-in-wing-foiling-and-how-to-avoid-them/ | /wing-foil/lessons/ | |
| 🟢 | /best-kitesurfing-beaches-on-koh-phangan-for-beginners/ | /blog/ | Merge with spots guide |
| 🟢 | /best-kitesurfing-beaches-on-koh-phangan/ | /blog/ | Merge |
| 🟢 | /kiteboarding-on-koh-phangan-vs-koh-samui-which-island-is-better/ | /blog/ | Near-duplicate of koh-phangan-vs-koh-samui |
| 🟢 | /kitesurf-koh-phangan-kiteboarding-guide-the-best-spots-in-thailand/ | /blog/ | |
| 🟢 | /best-time-to-visit-kite-club-koh-phangan-wind-conditions-and-seasons-for-kite-surfing/ | /blog/ | |
| 🟢 | /top-kitesurf-school-in-koh-phangan-why-kite-club-rules/ | /about/ | Brand content |
| 🟢 | /why-choose-kite-club-koh-phangan-for-your-first-kite-surfing-lesson/ | /about/ | Brand content |
| 🟢 | /discover-kitesurfing-how-to-choose-the-best-kiteschool-koh-phangan/ | /kitesurfing/lessons/ | |
| 🟢 | /what-makes-kitesurfing-on-koh-phangan-different-from-bali-sri-lanka-or-vietnam/ | /blog/ | |
| 🟢 | /what-makes-the-kitesurf-community-best-on-koh-phangan/ | /about/ | |
| 🟢 | /top-reasons-to-choose-koh-phangan-for-your-next-kitesurf-trip/ | /kitesurfing/ | |
| 🟢 | /an-honest-guide-to-the-best-kitesurfing-on-koh-phangan/ | /blog/ | |
| 🟢 | /a-day-in-the-life-the-real-vibe-of-kitesurfing-on-koh-phangan/ | /blog/ | |
| 🟢 | /why-koh-phangan-is-the-best-place-in-thailand-to-learn-kiteboarding/ | /kitesurfing/ | |
| 🟢 | /the-guide-to-kitesurfing-on-koh-phangan/ | /kitesurfing/ | |
| 🟢 | /where-to-find-the-best-kitesurfing-on-koh-phangan/ | /locations/ | |
| 🟢 | /where-are-the-best-kiteboarding-water-spots-on-koh-phangan/ | /locations/ | |
| 🟢 | /your-first-day-kitesurf-on-the-water-a-step-by-step-guide-to-kitesurfing-on-koh-phangan/ | /kitesurfing/lessons/ | |
| 🟢 | /7-essential-tips-for-your-first-kite-surfing-trip-to-koh-phangan/ | /kitesurfing/lessons/ | |
| 🟢 | /ready-to-stand-up-paddleboarding-the-best-sup-rental-koh-phangan/ | /sup-rental/ | |
| 🟢 | /top-activities-in-thailand-why-kayaking-koh-phangan-to-coral-reefs-is-a-must-do/ | /kayaking/ | |
| 🟢 | /wakeboarding-wakesurfing-koh-phangan-best-spots-lessons-tips/ | /blog/ | Service not offered |
| 🟢 | /10-best-beaches-koh-phangan-a-beach-guide-to-paradise/ | /locations/ | |
| 🟢 | /ride-the-tropical-wind-your-dream-kite-surfing-adventure-in-koh-phangan/ | /kitesurfing/ | |
| 🟢 | /koh-phangan-for-the-active-wellness-traveller-combining-yoga-kitesurfing-and-wing-foiling-on-the-island/ | /blog/ | |

---

## PART 3 — _redirects FILE (Netlify format)

This file must be placed at the root of the repository.

```
# PAGE URL REDIRECTS
/windsurfing-2/     /windsurfing/     301
/supboard-rental/   /sup-rental/      301
/membership-storage/ /storage/        301

# BLOG POST REDIRECTS — Direct matches
/from-kite-to-wing-why-experienced-kitesurfers-are-switching-to-wing-foil/   /blog/posts/kite-to-wing.html   301
/family-holidays-why-wing-foiling-and-kitesurfing-are-the-perfect-combo-for-active-groups/   /blog/posts/family-holidays.html   301
/top-10-common-mistakes-when-transitioning-from-kitesurfing-to-wing-foil/   /blog/posts/top-10-mistakes.html   301
/wing-foil-vs-efoil-which-is-right-for-you/   /blog/posts/efoil-vs-wing.html   301
/wind-seasons-on-koh-phangan-the-complete-calendar-for-kitesurfing-and-wing-foil-riders/   /blog/posts/wind-season-2026.html   301
/kitesurfing-vs-wing-foiling-which-one-should-you-learn-first-on-koh-phangan/   /blog/posts/first-kite-lesson.html   301
/when-is-the-best-time-for-kitesurfing-in-koh-phangan/   /blog/posts/wind-season-2026.html   301
/how-many-days-does-it-actually-take-to-learn-kitesurfing-on-koh-phangan/   /blog/posts/wind-season-2026.html   301

# BLOG POST REDIRECTS — To specific service pages
/wing-foil-koh-phangan-how-to-start-with-wing-foil-rental-in-thailand/   /wing-foil/lessons/   301
/efoil-board-lessons-koh-phangan-learn-to-fly-above-the-water-in-thailand/   /efoil/lessons/   301
/why-wing-foiling-is-the-fastest-growing-water-sport-in-the-world/   /wing-foil/   301
/wing-foil-safety-essential-gear-and-tips-for-new-riders/   /wing-foil/lessons/   301
/how-to-choose-your-first-wing-foil-board-on-koh-phangan-size-volume-and-stability/   /wing-foil/lessons/   301
/top-5-common-beginner-mistakes-in-wing-foiling-and-how-to-avoid-them/   /wing-foil/lessons/   301
/top-kitesurf-school-in-koh-phangan-why-kite-club-rules/   /about/   301
/why-choose-kite-club-koh-phangan-for-your-first-kite-surfing-lesson/   /about/   301
/what-makes-the-kitesurf-community-best-on-koh-phangan/   /about/   301
/discover-kitesurfing-how-to-choose-the-best-kiteschool-koh-phangan/   /kitesurfing/lessons/   301
/top-reasons-to-choose-koh-phangan-for-your-next-kitesurf-trip/   /kitesurfing/   301
/why-koh-phangan-is-the-best-place-in-thailand-to-learn-kiteboarding/   /kitesurfing/   301
/the-guide-to-kitesurfing-on-koh-phangan/   /kitesurfing/   301
/where-to-find-the-best-kitesurfing-on-koh-phangan/   /locations/   301
/where-are-the-best-kiteboarding-water-spots-on-koh-phangan/   /locations/   301
/your-first-day-kitesurf-on-the-water-a-step-by-step-guide-to-kitesurfing-on-koh-phangan/   /kitesurfing/lessons/   301
/7-essential-tips-for-your-first-kite-surfing-trip-to-koh-phangan/   /kitesurfing/lessons/   301
/ready-to-stand-up-paddleboarding-the-best-sup-rental-koh-phangan/   /sup-rental/   301
/top-activities-in-thailand-why-kayaking-koh-phangan-to-coral-reefs-is-a-must-do/   /kayaking/   301
/10-best-beaches-koh-phangan-a-beach-guide-to-paradise/   /locations/   301
/ride-the-tropical-wind-your-dream-kite-surfing-adventure-in-koh-phangan/   /kitesurfing/   301

# BLOG POST REDIRECTS — To /blog/ (fallback)
/best-time-to-kitesurf-on-koh-phangan-complete-monthly-wind-weather-guide/   /blog/   301
/best-kiteboarding-spots-in-koh-phangan/   /blog/   301
/best-kite-spots-in-koh-phangan-for-beginners-safety-first-beach-rankings/   /blog/   301
/the-complete-guide-to-kitesurf-in-koh-phangan-spots-seasons-kitesurfing-schools/   /blog/   301
/is-koh-phangan-good-for-learning-kitesurfing-honest-beginners-guide/   /blog/   301
/how-long-does-it-take-to-learn-kitesurfing-or-wing-foiling-in-koh-phangan-honest-timelines-for-beginners/   /blog/   301
/koh-phangan-vs-koh-samui-for-kitesurfing-which-island-should-you-choose/   /blog/   301
/what-to-expect-your-first-kitesurfing-lesson-on-koh-phangan/   /blog/   301
/what-to-expect-your-first-kitesurfing-lesson-in-koh-phangan/   /blog/   301
/top-5-reasons-why-koh-phangan-is-the-best-place-for-kitesurfing/   /blog/   301
/first-time-on-the-water-should-you-start-with-kitesurfing-or-wing-foiling-on-koh-phangan/   /blog/   301
/what-kitesurfing-equipment-you-need-on-koh-phangan-tropical-conditions-guide/   /blog/   301
/koh-phangan-for-the-active-wellness-traveller-combining-yoga-kitesurfing-and-wing-foiling-on-the-island/   /blog/   301
/best-kitesurfing-beaches-on-koh-phangan-for-beginners/   /blog/   301
/best-kitesurfing-beaches-on-koh-phangan/   /blog/   301
/kiteboarding-on-koh-phangan-vs-koh-samui-which-island-is-better/   /blog/   301
/kitesurf-koh-phangan-kiteboarding-guide-the-best-spots-in-thailand/   /blog/   301
/best-time-to-visit-kite-club-koh-phangan-wind-conditions-and-seasons-for-kite-surfing/   /blog/   301
/what-makes-kitesurfing-on-koh-phangan-different-from-bali-sri-lanka-or-vietnam/   /blog/   301
/an-honest-guide-to-the-best-kitesurfing-on-koh-phangan/   /blog/   301
/a-day-in-the-life-the-real-vibe-of-kitesurfing-on-koh-phangan/   /blog/   301
/wakeboarding-wakesurfing-koh-phangan-best-spots-lessons-tips/   /blog/   301
/why-koh-phangan-is-the-best-place-in-thailand-to-learn-kiteboarding/   /kitesurfing/   301
/koh-phangan-for-the-active-wellness-traveller-combining-yoga-kitesurfing-and-wing-foiling-on-the-island/   /blog/   301
```

---

## PART 4 — INTERNAL LINKING MIGRATION

### Old site internal links that will break (must fix on new site)
| Old Link Target | New Site Page | Fix Required |
|----------------|---------------|-------------|
| /windsurfing-2/ | /windsurfing/ | Update all nav/footer links |
| /supboard-rental/ | /sup-rental/ | Update all internal links |
| /membership-storage/ | /storage/ | Update all internal links |
| /school/ | /school/ (same) | No change needed |

### Verify these internal links are correct on new site
- [ ] All nav links use correct new URLs
- [ ] Footer links use correct new URLs
- [ ] Blog post internal links updated
- [ ] Sitemap.xml updated with all new URLs

---

## PART 5 — SITEMAP MIGRATION

### Old sitemap structure (WordPress auto-generated):
- /post-sitemap.xml
- /page-sitemap.xml
- /team_post-sitemap.xml
- /category-sitemap.xml

### New sitemap (single file):
- /sitemap.xml — must include ALL pages + blog posts
- Must NOT include old WordPress URLs
- Must include all new lesson pages
- Priority: homepage (1.0), service pages (0.8), lesson pages (0.7), blog (0.6)

---

## PART 6 — ROBOTS.TXT MIGRATION

Old site: WordPress default robots.txt
New site: Enhanced robots.txt (already implemented — allow GPTBot, Perplexity, etc.)

Ensure /robots.txt exists and references /sitemap.xml correctly.
