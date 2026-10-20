# Playbook 2.0, Prompts 4 to 20: build, QA and handoff (Oct 20 2026)

The playbook was written for GHL AI Studio (SSR). This is a static Netlify build: "server rendered" here
means every page is a complete HTML file made at build time, so titles, meta, canonical, Open Graph, JSON-LD,
headings and copy are all in the raw HTML. "Hydration" is not applicable: site.js only adds the menu toggles
and the EN/ES switch, and the site works without it. "Forms" are not applicable: the site is phone only.

## Prompt 4: business data
src/data/site.json holds every shared value: name, d/b/a, category, origin, phone (display and tel),
hours (24/7 automated assistant), disclosures, quote bar, footer, ROC lookup URL, GA4 G-XL16NRYYJS,
Facebook URL (kept from main), navigation, services, guides, areas. No email, address or owner is shown
(INTAKE.md). Old-identity check: no Phoenix name, domain, (623) number or Phoenix GA id remains in src/ or
dist/ (grep).

## Prompt 5: brand system
Tokens in src/static/css/site.css: terracotta #7a3418 header, desert brown headings, call band and footer,
amber #e6a14c buttons, terracotta #a3441f and pool blue #0f6f86 bands with white text, white sections,
visible amber focus ring, reduced-motion support. Logo and favicons from the live site.

## Prompt 6: navigation, header, footer
Header: logo to /, Services, Service Areas and Guides menus from site.json, How It Works, About, FAQ,
Contact, EN/ES toggle, call button. Mobile menu below 1100 px. Footer rows left to right: Services,
Service areas, Guides, Company; disclosure, phone, Facebook icon, copyright and credit. No back-to-top
button. Tested in the browser (scripts/functional_check.js).

## Prompts 7 to 12: pages
Written by nine writer sub-agents from docs/WRITING-GUIDE.md and the verified research files in
docs/research/, each page for its own keyword (SERVICES.md). Home (7), services overview (8), 8 service
pages (9, one at a time per writer), service-areas overview (10), 5 town pages (11, each researched for that
town), about, FAQ, privacy, terms (12).

## Prompt 13: contact
/contact/ is a phone page: call buttons, 24/7 hours, what to say, what happens if the company misses the
call, privacy and terms links. The old `pool-inquiry` Netlify form is gone; check.py fails any `<form>`.
Form tests are not applicable.

## Prompt 14: reviews and social
No reviews, ratings or badges exist and none were added. Facebook (live on main) shows in the top bar and
footer with an accessible label and opens in a new tab; the other social slots stay hidden until URLs exist.

## Prompt 15: media
Every page: a full-width hero (eager, fetchpriority high, preloaded, WebP srcset 480 to 1920) and at least
two lazy in-body figures with alt, width and height; no photo twice on one page. 34 new photos were planned and all have since been added
(docs/image-list.md: file name, size, page, alt, Artistly prompt); until each exists the page shows an
existing photo, never a broken image. No video was supplied, so the home hero is a photo.

## Prompt 16: SEO (raw HTML, every route)
check.py verifies on every built file: unique title and description, canonical on the production origin,
og:title, og:description, og:url, absolute og:image, twitter tags, exactly one H1, one valid JSON-LD block
(Organization, WebSite on home, WebPage, BreadcrumbList, Service on service and town pages, Article on
guides, FAQPage matching the visible FAQs), sitemap.xml lists all 27 indexable routes and not the 404,
robots.txt points to the sitemap, 404 is noindex.

| Route | Title, description, canonical, OG, JSON-LD, one H1 | Status |
|---|---|---|
| all 27 indexable routes (list in docs/playbook/01-03) | checked by check.py | passed |
| /404.html | noindex, no canonical, not in sitemap | passed |
| live HTTP status codes and Netlify redirects | need the live deploy | not verified |

## Prompt 17: remnant sweep
No previous business names, domains, phone numbers, analytics ids, lorem ipsum, TODOs, fake reviews, empty
hrefs, duplicate ids, duplicate metadata or duplicate JSON-LD (check.py, grep). A netlify.toml header rule
left from another build was removed. Intentional placeholders: none (the 34 planned photos were added). Missing client inputs: email (UNKNOWN, not shown), other social URLs, a hero video.

## Prompt 18: responsive and accessibility
scripts/responsive_check.js, Chromium: every page at 1440, 1024, 768 and 390 px, samples at 1920 and 2560:
0 problems (overflow, broken images, hero edge to edge and at most 720 px tall, call button above the fold,
headline on the left rail). Accessibility: skip link, visible focus, keyboard menus with Escape, aria labels
on icon links, labeled language buttons, alt text, logical headings (check.py warns on skipped levels: none),
tables stack as cards on phones, reduced-motion CSS. Screenshots reviewed at 1440 and 390.

## Prompt 19: functional
scripts/functional_check.js: 13 of 13 pass (menus, submenus, FAQ accordion, tel links, skip link, ES
cookie, 404, scroll to top after navigation). Analytics and Translate scripts could not load in the sandbox
(third-party hosts blocked): not verified. Phone routing: not verified.

## Prompt 20: final review and handoff
- Files: see `git log` on `build`; source in src/, built site in dist/, records in docs/.
- Build, rules, SEO, links, old URLs, duplication, grep, browser and functional checks: all passed
  (docs/qa.md). Independent fact-check: done (docs/fact-check.md).
- Not verified: live Netlify behavior (404 status, redirects), Google Analytics and Translate on the real
  domain, the phone line's routing.
- Launch blockers: none. The owner kept the "may be recorded or logged" call wording and chose Texas law
  for the terms (Oct 20 2026).
- Readiness: ready for Maurice's review on the `build` branch. Not deployed and not merged; going live is
  his decision (merge `build` to main, Netlify publishes dist/).
