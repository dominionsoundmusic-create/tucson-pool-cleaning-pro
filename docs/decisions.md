# Decisions log (Playbook 2.0 rebuild, Oct 20 2026)

Maurice was not available to approve anything during this run (CLAUDE.md: run straight through). Each
decision below was made from INTAKE.md, CLAUDE.md, the keyword data and the live site, and can be reversed.

## Build system and structure
1. **Build system copied from Phoenix Pool Cleaning Pro (main), words not copied.** build.py,
   scripts/check.py, similarity.py, check_old_urls.py, grep_check.py, keyword_plan.py, responsive_check.js,
   the Jinja templates and macros (img, faqs, sources, disclosure and the rest), site.css, site.js, the
   self-hosted Inter woff2 font, the site.json structure and netlify.toml (`publish = "dist"`). The speed
   fix is unchanged: WebP srcset at 480/800/1200/1600/1920, preloaded hero with fetchpriority high,
   woff2 font. Every shared template sentence (how-it-works strip, call band, call box, license note,
   disclosure) was rewritten for Tucson, and scripts/similarity.py compares every Tucson page with every
   Phoenix page (Jaccard limit 15%, and it fails on any shared 8-word run).
2. **Old live site moved to docs/old-site/.** It stays as the reference for every old URL
   (scripts/check_old_urls.py reads it). Its photos moved to src/static/images/ at the same public paths,
   so old image URLs still resolve. Netlify publishes dist/ (committed; no build command).
3. **URLs.** The live site used folder URLs (/about/, /pool-pump-repair/ and so on) plus one flat page,
   /oro-valley-pool-service. Every one is rebuilt at the same path. New core, service and guide pages use
   folder URLs; the four new town pages copy the flat /<town>-pool-service pattern so all five towns match.
   /privacy-policy.html and /terms.html keep their .html URLs.
4. **Redirects (src/static/_redirects, copied to dist/).** Kept every Sep 24 and Sep 25 rule. Re-pointed to
   the closer new page where one now exists: /algae-treatment/ to /green-pool-cleanup/;
   /swimming-pool-service/ to /pool-service/ (a real pool service page now exists; the URL itself stays a
   301 because /pool-service/ is the cleaner page name); retired blog posts on desert heat and dust and on
   how often to clean to /tucson-pool-maintenance-schedule/, on pump failure to /pool-pump-not-working/, on
   weekly service cost to /pool-service-cost/, on summer algae to /my-pool-is-green/, on DIY equipment
   repair to /swimming-pool-repair/. /pool-equipment-repair/ still 301s to /swimming-pool-repair/ (no
   equipment page was built). Added /oro-valley-pool-service/ to the flat page. No real page shadows a rule.
5. **Phone only.** The old Netlify `pool-inquiry` form is retired; /contact/ is a phone page. The old form had
   no action or thank-you URL, so no redirect was needed. check.py fails any `<form>`.
   **Changed Oct 29 2026 (owner's request):** /contact/ now also has one Netlify form, `tucson-pool-contact`
   (name, phone, email, city, need, message), posting to the noindex /contact/thanks/ page. The
   netlify/functions/submission-created.mjs function texts the owner each verified submission. check.py
   allows that single form on /contact/ and fails a form anywhere else. The phone call stays the main CTA.
6. **Phone number in one place.** (520) 372-1083 lives only in src/data/site.json; the call label is built
   from it and pages use `{{ site.business.phone_display }}`.
7. **Kept from main:** GA4 G-XL16NRYYJS with the phone-tap event, and the Facebook URL
   https://www.facebook.com/tucsonpoolcleaningpro (top bar and footer). Other social slots stay empty and
   hidden.

## Design
8. **Colors.** Header bar terracotta #7a3418 (the live brand color); headings, call band and footer in the
   logo's desert brown (#3a2a17, #2a1d0f); amber #e6a14c call buttons with brown text; the first color band
   in brighter terracotta #a3441f and the second in the logo's pool blue #0f6f86, both with white text.
   Sections are white between bands; the FAQ block is white (the Phoenix build tinted it) so a page reads
   hero, white, terracotta, white, blue, white, then the dark call band.
9. **Card rows** changed from an auto-fit grid to centered flex rows: 3 across, 2 at tablet, 1 on phones,
   a short last row centered. The how-it-works strip and three-panel grids follow the same rule.
10. **Footer** changed from columns to rows that run left to right (Services, Service areas, Guides,
    Company), each a label followed by its links.
11. **Logo and favicons** kept from the live site; an apple-touch-icon.png in the same colors was added.

## Pages and keywords (see SERVICES.md and docs/keyword-plan.md)
12. **28 pages:** 10 core, 8 service, 5 guide, 5 town.
13. **Home targets** "swimming pool service tucson" (880) and "pool service tucson" (720), as CLAUDE.md says.
    To avoid two pages competing for the same words, /pool-service/ targets "weekly pool service tucson"
    and explains the ongoing service arrangement, and /pool-cleaning-maintenance/ targets the cleaning
    terms and the hands-on routine.
14. **Service pages:** the five CLAUDE.md requires plus green pool cleanup (seed row; question demand),
    pool leak and line repair ("pool line repair near me" 140 national) and pool light repair ("pool lights
    repair near me" 590 national at SD 9; its target "pool light repair tucson" is not a row in the file).
    No equipment or heater page: the Tucson data has no rows for them, so they are covered on
    /swimming-pool-repair/.
15. **Guides:** one combined cost guide for pool service and pool cleaning (the two cost clusters are the
    same question), "my pool is green", "pool pump stopped working", the Tucson maintenance schedule
    (monsoon and summer heat; it also answers the cold-climate "pool opening" rows honestly), and draining
    or recycling pool water (target "tucson pool water recycling"; it carries the Pima County and City of
    Tucson drain and backwash rules).
16. **Towns:** Oro Valley, Catalina Foothills, Green Valley, Vail and Sahuarita, each with 10 or more
    searches a month (exact rows in SERVICES.md). Marana showed zero and folds into the Tucson pages.

## Facts
17. **No Tucson Water hardness number.** The live site said "220 ppm"; no official Tucson Water figure was
    found (docs/research/water.md), so the number is gone. Pages say what Tucson Water says (the water is
    hard, and hardness rises with the share of Colorado River water) and use the figures that utilities do
    publish (Oro Valley Water Utility 2023 report).
18. **Old claims dropped:** "chemicals included", flat monthly price, same-visit repairs, "300-plus days of
    sun", and every unsourced statement on the live site. Facts were re-verified (docs/research/) before use.

## Writing, fact-check and QA
19. **Pages were written by nine separate writer agents** from docs/WRITING-GUIDE.md and the research files,
    and checked by five different fact-check agents that wrote nothing (docs/fact-check.md).
20. **Every remaining price is a national published range** with the publisher named and "real quotes
    vary". Tucson-specific HomeAdvisor figures were dropped because they could not be found again.
21. **Tile cleaning states no price**: no cost guide publishes a pool tile or calcium removal price.
22. **Shared template text was reworded twice** so that no Tucson page shares an 8-word run with any
    Phoenix page; similarity.py now drops the license note as template text.
23. **Browser QA ignores blocked third-party requests** (Google Analytics, Translate), which the sandbox
    cannot reach; every other console error still counts.
24. **Owner answers (Oct 20 2026):** keep the "may record or log" call wording as is; the terms are
    governed by Texas law. The 34 photos in docs/image-list.md were added on Oct 20 2026.
25. **Texas law clause.** The owner chose Texas law for the terms. That single sentence on /terms.html is
    exempted in check.py and grep_check.py; any other mention of Texas anywhere still fails.
