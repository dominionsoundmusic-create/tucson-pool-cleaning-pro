# Playbook 2.0, Prompts 1 to 3: fact brief, architecture, baseline and route plan (Oct 20 2026)

## Prompt 1: client fact brief (from INTAKE.md; INTAKE wins)

| Item | Value | Status |
|---|---|---|
| Official name | Tucson Pool Cleaning Pro, a d/b/a of Dominion Digital Group | Confirmed |
| What it is | A free phone line and website, not a pool company. An automated assistant answers, then transfers the caller to an independent, locally owned Tucson-area pool service company (or passes name, number, area and problem for a call back). The company inspects, quotes, does the work and bills the customer. Companies may pay a referral fee | Confirmed |
| Primary category | Pool service referral line for the Tucson metro area | Confirmed |
| Services | Chosen from the keyword data (SERVICES.md). Not offered: building pools, fencing, landscaping, pest control, public-pool information | Confirmed |
| Service area | Tucson and the Tucson metro in Pima County: Oro Valley, Catalina Foothills, Vail, Sahuarita, Green Valley, Marana. Never anywhere else | Confirmed |
| Address | DO NOT DISPLAY | Confirmed (omitted) |
| Phone | (520) 372-1083, tel:+15203721083, only in src/data/site.json. Never 903-636-7511 | Confirmed |
| Email | UNKNOWN, not displayed | Missing, deferrable |
| Hours | Line answered 24/7 by an automated assistant | Confirmed |
| Year established, owner name | Not displayed | Confirmed (omitted) |
| Primary CTA | Call the phone number (site is phone only; the old `pool-inquiry` Netlify form is retired) | Confirmed |
| Secondary CTA | A real page: /how-it-works/ or a guide or in-page section, never a form | Confirmed |
| Brand | Terracotta #7a3418 and amber #e6a14c family, plus pool blue; header in a real color; mostly white sections with bold bands; existing logo.svg and favicons | Confirmed |
| Top bar / footer | "John 3:16" left, the exact Duplantis quote; footer copyright and Dominion Web Design Pro credit | Confirmed |
| Language | EN / ES Google Translate toggle in the header | Confirmed |
| Social | Facebook https://www.facebook.com/tucsonpoolcleaningpro (already live on main, kept); others empty and hidden | Confirmed |
| Analytics | GA4 G-XL16NRYYJS with phone-tap event (already live on main, kept) | Confirmed |
| Reviews, licenses, team, guarantees | None. Do not invent | Confirmed (none shown) |
| Domain | https://tucsonpoolcleaningpro.com, Netlify, production branch main | Confirmed |
| Photos | images/img-01.jpg, 12 images/tucson-*.jpg, images/pool/*.jpg; new ones listed in docs/image-list.md | Confirmed |

Contradictions: the live site claimed "chemicals included", flat monthly pricing, same-visit repairs and
"220 ppm" hardness without a source. INTAKE.md forbids the first three; the hardness figure is re-verified
or dropped. No launch blockers that need Maurice: the build can be finished from INTAKE.md. Deferred: an
email address, more social profiles, new photos (docs/image-list.md).

## Prompt 2: architecture

The playbook targets a GHL AI Studio SSR project. This repo is a static site on Netlify, so the playbook's
SSR requirements map to: every page is a complete HTML file rendered at build time (titles, meta,
canonical, Open Graph, JSON-LD, headings and body copy are all in the raw HTML; no client rendering).
Build system copied from dominionsoundmusic-create/phoenix-pool-cleaning-pro (main):

- `build.py` (Python 3, Jinja2, PyYAML, Pillow): pages in `src/pages/*.html` with YAML front matter,
  shared data in `src/data/site.json`, templates in `src/templates/` (layouts/base.html, partials for
  header, hero, faq, cta, footer, social icons, and `macros.html`). Output `dist/` plus sitemap.xml,
  robots.txt and docs/image-list.md. WebP copies at 480/800/1200/1600/1920 in a picture srcset, hero
  preloaded with fetchpriority high, self-hosted Inter woff2.
- `netlify.toml`: publish = "dist", no build command (dist/ is committed). `src/static/_redirects` is
  copied to `dist/_redirects`.
- Checks: `scripts/check.py` (rules and SEO), `scripts/similarity.py` (duplication, and against the
  Phoenix build), `scripts/check_old_urls.py`, `scripts/grep_check.py`, `scripts/keyword_plan.py`,
  `scripts/responsive_check.js` (Playwright, Chromium).
- No framework, router or forms. Navigation, services, guides and areas come from site.json.

## Prompt 3: baseline and route matrix

Baseline: the live site (main) was 12 hand-written static pages with no build step; it is kept unchanged in
`docs/old-site/` as the URL reference. Its photos moved to `src/static/images/` at the same public paths.

| Route | Type | Source | In nav | In sitemap | Indexable | Status |
|---|---|---|---|---|---|---|
| / | home | src/pages/index.html | logo | yes | yes | live, rebuilt |
| /services/ | overview | services.html | yes | yes | yes | live, rebuilt |
| /service-areas/ | overview | service-areas.html | yes | yes | yes | new |
| /how-it-works/ | core | how-it-works.html | yes | yes | yes | new |
| /about/ | core | about.html | yes | yes | yes | live, rebuilt |
| /faq/ | core | faq.html | yes | yes | yes | live, rebuilt |
| /contact/ | core (phone page) | contact.html | yes | yes | yes | live, rebuilt |
| /privacy-policy.html | legal | privacy-policy.html (url:) | footer | yes | yes | live, rebuilt |
| /terms.html | legal | terms.html (url:) | footer | yes | yes | live, rebuilt |
| /404.html | 404 | 404.html | no | no | noindex | new |
| /pool-service/ | service | pool-service.html | Services menu | yes | yes | new |
| /pool-cleaning-maintenance/ | service | pool-cleaning-maintenance.html | Services menu | yes | yes | live, rebuilt |
| /swimming-pool-repair/ | service | swimming-pool-repair.html | Services menu | yes | yes | live, rebuilt |
| /pool-pump-repair/ | service | pool-pump-repair.html | Services menu | yes | yes | live, rebuilt |
| /pool-tile-cleaning/ | service | pool-tile-cleaning.html | Services menu | yes | yes | live, rebuilt |
| /green-pool-cleanup/ | service | green-pool-cleanup.html | Services menu | yes | yes | new |
| /pool-leak-repair/ | service | pool-leak-repair.html | Services menu | yes | yes | new |
| /pool-light-repair/ | service | pool-light-repair.html | Services menu | yes | yes | new |
| /pool-service-cost/ | guide | pool-service-cost.html | Guides menu | yes | yes | new |
| /my-pool-is-green/ | guide | my-pool-is-green.html | Guides menu | yes | yes | new |
| /pool-pump-not-working/ | guide | pool-pump-not-working.html | Guides menu | yes | yes | new |
| /tucson-pool-maintenance-schedule/ | guide | tucson-pool-maintenance-schedule.html | Guides menu | yes | yes | new |
| /draining-a-pool-in-tucson/ | guide | draining-a-pool-in-tucson.html | Guides menu | yes | yes | new |
| /oro-valley-pool-service | area | oro-valley-pool-service.html (url:) | Areas menu | yes | yes | live, rebuilt |
| /catalina-foothills-pool-service | area | (url:) | Areas menu | yes | yes | new |
| /vail-pool-service | area | (url:) | Areas menu | yes | yes | new |
| /sahuarita-pool-service | area | (url:) | Areas menu | yes | yes | new |
| /green-valley-pool-service | area | (url:) | Areas menu | yes | yes | new |

All routes are static files. Every old URL and every old _redirects source must resolve (see docs/qa.md).

Stage plan: Prompts 4 to 6 (site.json, brand CSS, header, footer, nav) and the keyword plan, then Prompts 7
to 12 (research fact bank in docs/research/, pages written by separate writer agents from
docs/WRITING-GUIDE.md), Prompts 13 to 15 (phone-only contact, social, media and image list), Prompts 16 and
17 (SEO and remnant sweep), Prompts 18 to 20 (browser QA, functional QA, independent fact-check, handoff).
