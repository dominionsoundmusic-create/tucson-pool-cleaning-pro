# QA record (Oct 20 2026, final run on the `build` branch)

All commands run from the repo root against the production build in dist/.

| Check | Command | Result |
|---|---|---|
| Build | `python3 build.py` | 28 pages built (10 core, 8 service, 5 guide, 5 town); 34 planned photos listed in docs/image-list.md, each page shows an existing photo meanwhile, never a broken image |
| Rules and SEO | `python3 scripts/check.py` | 28 pages checked, **0 errors, 0 warnings** (banned phrases and INTAKE words to avoid, dashes, places outside the Tucson metro, SRP/APS/Maricopa/Phoenix, DIY chemical/gas/electrical wording, forms, eyebrow labels, exact quote bar, footer credit, referral disclosure, handwritten marker in the first 4KB, one H1, unique titles and descriptions, canonical, OG tags, one valid JSON-LD block, 3 to 6 FAQs visible and in FAQPage JSON-LD, hero plus 2 in-body images with lazy loading, alt/width/height, internal links, sitemap, _redirects targets) |
| Old URLs | `python3 scripts/check_old_urls.py` | **75 old URLs checked, 0 would 404** (every sitemap URL, page file, photo and old redirect source on main; table below) |
| CLAUDE.md grep | `python3 scripts/grep_check.py` | **0 hits** for em/en dashes, "we clean", "we repair", "our technicians", "licensed and insured", "free estimate", "same-day", "same day", "500+", "Phoenix", "Scottsdale", "Surprise", "Mesa", "Yuma", "Sierra Vista", "Nogales", "Tubac", "Maricopa", "Houston", "Texas", "(623)", "(903)", "903-636" in visible text, titles, meta and alt text (the Duplantis credit dash is drawn by CSS, not text) |
| Duplication | `python3 scripts/similarity.py --other <phoenix>/dist` | Same-type pairs max **1.5%** (town pairs max 0.8%, service 1.0%, guide 1.0%; limit 15%). Every Tucson page against every Phoenix page: max **1.3%**, 0 pairs above 15%, 0 pages sharing an 8-word run |
| Keywords | `python3 scripts/keyword_plan.py` | 242 keywords: 128 assigned to 22 pages, 114 unused with reasons (docs/keyword-plan.md) |
| Browser layout | `node scripts/responsive_check.js` (Chromium, dist served locally) | 118 page loads (every page at 1440, 1024, 768 and 390 px, samples at 1920 and 2560): **0 problems** (no horizontal overflow, no local JS errors, no broken images, hero edge to edge, hero at most 720 px tall with the call button above the fold, headline on the left rail) |
| Functional | `node scripts/functional_check.js` | **13 of 13 pass**: mobile menu opens and Escape closes it, submenus (click and hover), FAQ accordion, every tel link is tel:+15203721083, first Tab reaches the skip link, ES button sets the googtrans cookie, 404 renders, footer links from scrolled pages land at the top |
| Fact-check | 5 independent sub-agents (none wrote the pages) | 357 claims checked; 14 corrected, 30 softened, 9 removed, plus 1 removal by the lead (docs/fact-check.md) |

Not verified here (needs the live site or Maurice): Netlify's 404 status and redirect behavior in production,
Google Analytics and the Google Translate ES rendering (third-party hosts are blocked in this sandbox; the
browser check ignores only those blocked requests), and the phone line's routing.

## Duplication (Jaccard on 5-word shingles, page copy and FAQ answers; shared template parts excluded)

| Group | Pairs | Max | Mean | Min |
|---|---:|---:|---:|---:|
| area | 10 | 0.8% | 0.5% | 0.2% |
| guide | 10 | 1.0% | 0.4% | 0.2% |
| legal | 1 | 1.5% | 1.5% | 1.5% |
| mixed | 292 | 1.5% | 0.2% | 0.0% |
| page | 10 | 1.1% | 0.5% | 0.0% |
| service | 28 | 1.0% | 0.4% | 0.0% |

Against Phoenix (52 pages, every Tucson page x every Phoenix page): max Jaccard 1.3% (/about/ vs /about/); pairs above the limit: 0; pages sharing an 8-word run: 0

Top 15 pairs:

| Jaccard | Page | Page |
|---:|---|---|
| 1.5% | /about/ | /how-it-works/ |
| 1.5% | /privacy-policy.html | /terms.html |
| 1.3% | /green-pool-cleanup/ | /tucson-pool-maintenance-schedule/ |
| 1.3% | /green-pool-cleanup/ | /my-pool-is-green/ |
| 1.2% | /pool-pump-not-working/ | /pool-pump-repair/ |
| 1.1% | /faq/ | / |
| 1.1% | /faq/ | /swimming-pool-repair/ |
| 1.1% | /faq/ | /pool-cleaning-maintenance/ |
| 1.0% | /pool-service/ | /pool-service-cost/ |
| 1.0% | /my-pool-is-green/ | /tucson-pool-maintenance-schedule/ |
| 1.0% | /green-pool-cleanup/ | /pool-tile-cleaning/ |
| 1.0% | /contact/ | /how-it-works/ |
| 0.9% | /faq/ | /tucson-pool-maintenance-schedule/ |
| 0.8% | /draining-a-pool-in-tucson/ | /pool-tile-cleaning/ |
| 0.8% | /green-valley-pool-service.html | /vail-pool-service.html |

## Old URLs

| Old URL | Result | How |
|---|---|---|
| / | 200 | served by a rebuilt page or file at the same path |
| /about/ | 200 | served by a rebuilt page or file at the same path |
| /algae-treatment/ | 301 | redirect to /green-pool-cleanup/ (rule /algae-treatment/) |
| /blog | 301 | redirect to / (rule /blog) |
| /blog/how-desert-heat-and-dust-affect-pool-chemistry-1785707710790 | 301 | redirect to /tucson-pool-maintenance-schedule/ (rule /blog/how-desert-heat-and-dust-affect-pool-chemistry-1785707710790) |
| /blog/how-desert-heat-and-dust-affect-pool-chemistry-1785707710790.html | 301 | redirect to /tucson-pool-maintenance-schedule/ (rule /blog/how-desert-heat-and-dust-affect-pool-chemistry-1785707710790.html) |
| /blog/how-much-does-weekly-pool-service-cost-in-tucson-1786970663994 | 301 | redirect to /pool-service-cost/ (rule /blog/how-much-does-weekly-pool-service-cost-in-tucson-1786970663994) |
| /blog/how-much-does-weekly-pool-service-cost-in-tucson-1786970663994.html | 301 | redirect to /pool-service-cost/ (rule /blog/how-much-does-weekly-pool-service-cost-in-tucson-1786970663994.html) |
| /blog/how-often-should-a-pool-be-cleaned-in-tucson-1785851663115 | 301 | redirect to /tucson-pool-maintenance-schedule/ (rule /blog/how-often-should-a-pool-be-cleaned-in-tucson-1785851663115) |
| /blog/how-often-should-a-pool-be-cleaned-in-tucson-1785851663115.html | 301 | redirect to /tucson-pool-maintenance-schedule/ (rule /blog/how-often-should-a-pool-be-cleaned-in-tucson-1785851663115.html) |
| /blog/how-often-should-a-pool-be-cleaned-in-tucson-1786366282124 | 301 | redirect to /tucson-pool-maintenance-schedule/ (rule /blog/how-often-should-a-pool-be-cleaned-in-tucson-1786366282124) |
| /blog/how-often-should-a-pool-be-cleaned-in-tucson-1786366282124.html | 301 | redirect to /tucson-pool-maintenance-schedule/ (rule /blog/how-often-should-a-pool-be-cleaned-in-tucson-1786366282124.html) |
| /blog/how-to-keep-algae-out-of-a-pool-in-summer-1785937790708 | 301 | redirect to /my-pool-is-green/ (rule /blog/how-to-keep-algae-out-of-a-pool-in-summer-1785937790708) |
| /blog/how-to-keep-algae-out-of-a-pool-in-summer-1785937790708.html | 301 | redirect to /my-pool-is-green/ (rule /blog/how-to-keep-algae-out-of-a-pool-in-summer-1785937790708.html) |
| /blog/how-to-keep-algae-out-of-a-pool-in-summer-1786024116957 | 301 | redirect to /my-pool-is-green/ (rule /blog/how-to-keep-algae-out-of-a-pool-in-summer-1786024116957) |
| /blog/how-to-keep-algae-out-of-a-pool-in-summer-1786024116957.html | 301 | redirect to /my-pool-is-green/ (rule /blog/how-to-keep-algae-out-of-a-pool-in-summer-1786024116957.html) |
| /blog/pool-chemical-balancing-explained-simply-1786278929729 | 301 | redirect to /pool-cleaning-maintenance/ (rule /blog/pool-chemical-balancing-explained-simply-1786278929729) |
| /blog/pool-chemical-balancing-explained-simply-1786278929729.html | 301 | redirect to /pool-cleaning-maintenance/ (rule /blog/pool-chemical-balancing-explained-simply-1786278929729.html) |
| /blog/pool-equipment-repairs-you-should-never-diy-1786452620892 | 301 | redirect to /swimming-pool-repair/ (rule /blog/pool-equipment-repairs-you-should-never-diy-1786452620892) |
| /blog/pool-equipment-repairs-you-should-never-diy-1786452620892.html | 301 | redirect to /swimming-pool-repair/ (rule /blog/pool-equipment-repairs-you-should-never-diy-1786452620892.html) |
| /blog/saltwater-vs-chlorine-pools-which-is-easier-to-maintain-1786192403888 | 301 | redirect to /pool-cleaning-maintenance/ (rule /blog/saltwater-vs-chlorine-pools-which-is-easier-to-maintain-1786192403888) |
| /blog/saltwater-vs-chlorine-pools-which-is-easier-to-maintain-1786192403888.html | 301 | redirect to /pool-cleaning-maintenance/ (rule /blog/saltwater-vs-chlorine-pools-which-is-easier-to-maintain-1786192403888.html) |
| /blog/signs-your-pool-pump-is-about-to-fail-1786106855752 | 301 | redirect to /pool-pump-not-working/ (rule /blog/signs-your-pool-pump-is-about-to-fail-1786106855752) |
| /blog/signs-your-pool-pump-is-about-to-fail-1786106855752.html | 301 | redirect to /pool-pump-not-working/ (rule /blog/signs-your-pool-pump-is-about-to-fail-1786106855752.html) |
| /contact/ | 200 | served by a rebuilt page or file at the same path |
| /faq/ | 200 | served by a rebuilt page or file at the same path |
| /favicon.ico | 200 | served by a rebuilt page or file at the same path |
| /favicon.svg | 200 | served by a rebuilt page or file at the same path |
| /images/img-01.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/logo.svg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/brush-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/chem-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/dusk-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/equip-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/green-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-1-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-1.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-2-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-2.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-3-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-3.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/repair-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/skim-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/test-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/vac-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-cleaning-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-cleaning-skim.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-cleaning-test.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-pump-bearings.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-pump-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-pump-vs.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-repair-heater.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-repair-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-repair-pump.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-tile-after.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-tile-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/tucson-tile-scale.jpg | 200 | served by a rebuilt page or file at the same path |
| /oro-valley-pool-service | 200 | served by a rebuilt page or file at the same path |
| /oro-valley-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /pool-chemical-balancing/ | 301 | redirect to /pool-cleaning-maintenance/ (rule /pool-chemical-balancing/) |
| /pool-cleaning-maintenance/ | 200 | served by a rebuilt page or file at the same path |
| /pool-cleaning-near-me/ | 301 | redirect to /services/ (rule /pool-cleaning-near-me/) |
| /pool-cleaning-service/ | 301 | redirect to /pool-cleaning-maintenance/ (rule /pool-cleaning-service/) |
| /pool-equipment-repair/ | 301 | redirect to /swimming-pool-repair/ (rule /pool-equipment-repair/) |
| /pool-maintenance/ | 301 | redirect to /pool-cleaning-maintenance/ (rule /pool-maintenance/) |
| /pool-pump-repair/ | 200 | served by a rebuilt page or file at the same path |
| /pool-tile-cleaning/ | 200 | served by a rebuilt page or file at the same path |
| /privacy-policy.html | 200 | served by a rebuilt page or file at the same path |
| /robots.txt | 200 | served by a rebuilt page or file at the same path |
| /services/ | 200 | served by a rebuilt page or file at the same path |
| /sitemap.xml | 200 | served by a rebuilt page or file at the same path |
| /swimming-pool-repair/ | 200 | served by a rebuilt page or file at the same path |
| /swimming-pool-service/ | 301 | redirect to /pool-service/ (rule /swimming-pool-service/) |
| /terms.html | 200 | served by a rebuilt page or file at the same path |
| /weekly-pool-cleaning/ | 301 | redirect to /pool-cleaning-maintenance/ (rule /weekly-pool-cleaning/) |

75 old URLs checked, 0 would 404.
