# Writing guide for tucsonpoolcleaningpro.com pages (Playbook 2.0 rebuild, Oct 20 2026)

Repo: /home/user/tucson-pool-cleaning-pro (branch `build`). Read these first, in full:
1. `CLAUDE.md` (the hard rules) and `INTAKE.md` (the facts; it wins over everything; read "WHAT THE
   BUSINESS ACTUALLY IS" twice).
2. `SERVICES.md` and `docs/keyword-plan.md` (your page's URL, TARGET keyword and supporting keywords,
   including the Question rows to turn into FAQs).
3. The research fact bank in `docs/research/`: `licensing-barriers.md`, `water.md`, `rules-climate.md`,
   `costs-equipment.md`. These facts were verified from official sources by search; use them, and cite the
   source URL each fact gives. Respect each file's "could NOT verify" list: those claims stay off the site.
4. `src/data/site.json` (names and URLs of services, guides and areas) and `src/templates/macros.html`.
5. STRUCTURE MODELS ONLY: the finished sister site Phoenix Pool Cleaning Pro, built with the same system:
   `/home/user/dominionsoundmusic-create/phoenix-pool-cleaning-pro/src/pages/pump-repair.html` (service),
   `.../pool-service-cost.html` (guide), `.../mesa-pool-service.html` (area). Match their depth, section
   rhythm and component use. NEVER copy their wording, sentences, FAQs, headings or facts (they are about
   Phoenix). `scripts/similarity.py` compares every Tucson page with every Phoenix page and FAILS on any
   shared run of 8 words or a Jaccard above 15%. Write from scratch, in your own sentences.
6. The old Tucson page for your URL in `docs/old-site/` (if any), for research leads only. Its numbers
   ("220 ppm", "300-plus days of sun", "chemicals included", flat monthly price, same-day repair) are
   UNVERIFIED or banned. Never copy or lightly reword its text.

## The business, in one paragraph
Tucson Pool Cleaning Pro is a free phone line and website, NOT a pool company. An automated assistant
answers (520) 372-1083 any hour, asks briefly what is going on with the pool, then transfers the call to an
independent, locally owned Tucson-area pool service company. That company hears a short summary before it
picks up. If it cannot answer, the caller's name, callback number, area and pool problem are passed along for
a call back. The company looks at the pool, quotes, does the work and is paid directly by the customer. The
line never cleans, repairs, quotes or schedules anything, holds no license, never charges the caller, and may
be paid a referral fee by the companies. Write "the pool company you are put through to", "the pool service
company", "a careful pool technician". Never "our technicians", "our trucks", "we clean", "we repair", "we
are licensed/insured", "we'll send someone". Never say the connected companies are licensed, insured,
certified, rated or reviewed. Tell readers to ASK for the company's Arizona ROC license number and look it up
on the ROC contractor search (https://roc.az.gov/contractor-search). Never name any pool company. Avoid
equipment brand names. Never write the phone number by hand: use `{{ site.business.phone_display }}` (tel
link: `tel:{{ site.business.phone_tel }}`).

## Hard rules (scripts/check.py enforces most of them)
- No em dashes or en dashes anywhere (copy, titles, descriptions, FAQs, alt text). Use commas, colons,
  periods or "to" ("95 to 100 degrees"). American spelling. No eyebrow labels or badges.
- Only Tucson-metro places: Tucson, Oro Valley, Catalina Foothills, Marana, Vail, Sahuarita, Green Valley,
  Catalina, Tanque Verde, Picture Rocks, Avra Valley, SaddleBrooke, Rita Ranch, Corona de Tucson and the
  neighborhoods, mountains (Santa Catalina, Rincon, Tucson, Santa Rita mountains), washes and roads of the
  Tucson area. Pima County. NEVER any other Arizona metro or town (no Phoenix, Scottsdale, Mesa, Yuma,
  Sierra Vista, Nogales, Tubac, Casa Grande, Maricopa or Maricopa County, Flagstaff, Lake Havasu), never
  another state or country (no Mexico, no California, no Texas), not even when explaining the Colorado River
  or the monsoon. Say "the Colorado River" and "the Central Arizona Project (CAP)" without naming where the
  canal starts. Never write "the Valley" (a Phoenix term). No SRP or APS (Phoenix utilities); Tucson power is
  Tucson Electric Power (TEP) or Trico Electric Cooperative depending on the address; gas is Southwest Gas.
  Never mention the ROC's street address (it is in Phoenix); use its website and toll-free 1-877-692-9762.
- Never invent licenses, insurance, reviews, ratings, prices, years in business, team members, job counts,
  statistics, response times, guarantees or awards. Public statistics are fine with the source named and
  listed. Prices: only published ranges with the publisher named on the page and a note that real quotes
  vary; never present a price as the line's price.
- Banned (checker fails): "free estimate(s)", "same-day", "same day", "guarantee(d)", "best price",
  "cheapest", "top-rated", "years of experience", "#1", "number one", "licensed and insured", "chemicals
  included", "flat monthly price", "500+", "5-star", "your trusted partner", "one-stop solution", "look no
  further", "unmatched excellence", "we've got you covered", response-time promises ("within 2 hours").
- Safety first, no DIY beyond safe basics:
  - Never give chemical-mixing or dosing instructions (no "add X pounds of shock", no acid washing steps, no
    muriatic acid dilution). Say plainly: never mix pool chemicals with each other (CDC), store them apart,
    dry, shaded and locked, out of children's reach, follow the label, and leave acid work to a professional.
  - No electrical work (motors, wiring, lights, breakers beyond resetting a tripped GFCI or breaker once; a
    breaker that trips again means leave it off and call), no gas work. Pool heater gas smell: leave the area
    right away, do not touch switches, the heater or anything that could spark, and from a safe distance call
    911 and Southwest Gas at 877-860-6020 (docs/research/rules-climate.md).
  - Children: keep them away from an unfenced or uncovered pool, never leave a child unsupervised near water,
    and a green or murky pool is a drowning hazard because the bottom cannot be seen.
  - Safe homeowner checks only: skimmer and pump baskets, the filter pressure gauge reading, the timer or
    automation schedule, water level at the skimmer, visible leaks or drips at the equipment pad, a tripped
    GFCI or breaker (reset once), debris around the equipment, testing water with a home test kit, the bucket
    test for evaporation.
- Every fact that is not common knowledge carries a source in the page's Sources list with a real URL. If
  you cannot verify it, leave it out.

## Key shared facts (verified, see docs/research/ for details and URLs)
- ROC: R-6 Swimming Pool Service and Repair covers servicing and minor repairs on residential pools; it
  excludes gas lines, electrical work beyond the first disconnect, potable water plumbing connections, and
  full replacement of plaster or pebble interiors or decks. B-5 covers building and repairing pools. No
  official statement on whether cleaning only needs a license: say the ROC does not spell it out, ask.
  Contractor search shows license status, classification, complaints and bond. The ROC does not require
  insurance except workers' compensation, so ask for proof of liability insurance directly. Do not state the
  handyman dollar limit.
- Tucson Water: CAP Colorado River water recharged in Avra Valley and blended with groundwater; the city says
  hardness rises as the CAP share rises and that hard water is safe to drink. No official average hardness
  number exists: never state one for Tucson Water.
- Oro Valley Water Utility 2023: about 65% groundwater, 35% CAP; hardness 36 to 270 ppm (2.1 to 15.8 gpg).
- NWS Tucson: monsoon season June 15 to September 30. 1991 to 2020 normals: July average high 100.2 F,
  68 days a year at or above 100 F, 10.61 inches of rain a year.
- ADWR: about six feet of water a year evaporates from an open surface in Tucson; a pool cover saves 90 to
  95% of that.
- Draining (City of Tucson / Pima County RWRD): the sanitary sewer through the home's own cleanout is the
  preferred route, with a hose and a small pump at low-use hours; wait at least 72 hours after the last
  chlorine and bring pH to 7 to 8; backwash may go on your own land only if it soaks in within 24 hours and
  does not reach neighbors, the street or alley; street or wash only as a last resort; never acid-wash water.
- TEP summer on-peak hours: weekdays 3 to 7 p.m.; TEP suggests pool pumps run in the morning or midday.
  TEP and Trico both serve parts of Marana, Sahuarita, Green Valley and Vail (it depends on the address).
- Pima County asks residents to report green, neglected pools (mosquitoes) to 520-724-7908.
- CDC: home pool pH 7.0 to 7.8; free chlorine at least 1 ppm, at least 2 ppm with stabilizer (cyanuric
  acid); never mix chemicals; store in original containers, dry, locked, below 95 F.
- DOE: pool pump motors 1.15 to 5 total horsepower made on or after Sep 29 2025 must be variable speed;
  smaller motors from Sep 28 2027, with an April 2026 enforcement delay to March 26 2029. Nobody must
  replace a pump that works.
- CPSC: the electrical code has required GFCI protection for underwater pool lights since 1968; test GFCIs
  monthly.

## Voice
Plain, specific, warm, Tucson-local. Second person. Short paragraphs, roughly 7th to 8th grade reading level;
explain a technical word the first time (cyanuric acid, total dissolved solids, calcium hardness). Explain
why. No filler, no superlatives, no keyword stuffing. The target keyword appears naturally in the title, H1,
first paragraph, one H2 and the meta description.

## Page file format
`src/pages/<file>.html` with YAML front matter, then `{% block content %}...{% endblock %}`. Folder URLs
need no `url:` (file `src/pages/pool-light-repair.html` becomes /pool-light-repair/). Town pages use the
flat URL: `src/pages/vail-pool-service.html` with `url: "/vail-pool-service"`. Legal pages: `url:
"/privacy-policy.html"`.

```yaml
---
type: service            # service | guide | area | page | about | contact | legal
url: "/vail-pool-service"   # ONLY for flat URLs (town pages, privacy, terms)
title: "..."             # 50 to 65 chars, unique, keyword near the front
description: "..."       # 120 to 160 chars, unique, no dashes
h1: "..."                # one H1, unique
crumb: "Vail"
keyword: "pool service vail az"
city_name: "Vail"        # area pages only
published: "2026-10-20"  # guides only
hero:
  image: vail-pool-hero.jpg      # PLANNED 1920x1080 photo (see Images)
  alt: "..."
  desc: "Artistly prompt for the planned photo."
  fallback: img-01.jpg           # existing photo shown until the planned one exists (given in your brief)
  fallback_alt: "..."            # accurate alt for the fallback photo
  lead: "One or two sentences under the H1."
  secondary_label: "..."         # optional: a real page or an in-page anchor, never a form
  secondary_href: "/..."
schema_service:          # service and area pages
  name: "Free connection to a local pool service company in Vail, Arizona"
  type: "Pool service referral"
cta_title: "..."         # short, specific to the page
faqs:                    # 3 to 6 (never more), phrased the way people ask (use the Question rows)
  - q: "..."
    a: "<p>...</p>"
---
```
Quote YAML strings that contain a colon. Inside FAQ answers use `&amp;` or the word "and" for "&".

## Building blocks (existing classes only; do not edit CSS, templates, build.py, check.py or site.json)
- Reading column: `<section class="prose">...</section>`. Text runs full width between the page rails
  (Maurice's full-width layout); never add wrappers that narrow it.
- Color band: `<section class="band band--tint"><div class="wide">...</div></section>`. The build turns
  the first into a bold terracotta band and the second into a pool-blue band, both with white text. Use ONE
  or TWO per page, with white prose sections between; never two bands in a row; do not end your content with
  a band (the FAQ block and the call band follow automatically).
- Two columns, text and photo: inside `.prose`, `<div class="split"><div>text</div>{{ img(...) }}</div>`.
- `<ol class="steps">` numbered process; `<ul class="checks">` checklist; `<div class="grid-2">` /
  `<div class="grid-3">` of `<div class="panel">` (add `panel--do` / `panel--dont`); `<ul class="facts">` of
  `<li><strong>label</strong>text</li>`; tables in `<div class="table-wrap"><table>` with `<caption
  class="sr">`, `<thead>`, `scope` on th; `<div class="note">` callout, `<div class="note note--orange">`
  warning.
- Macros: `{{ m.how_it_works_short() }}`, `{{ m.disclosure() }}`, `{{ m.license_check() }}`,
  `{{ m.call_box('text') }}`, `{{ m.service_cards(['slug', ...]) }}`, `{{ m.guide_cards(['slug']) }}`,
  `{{ m.area_pills(exclude='vail') }}`, `{{ m.related(['slug','guide:slug','area:slug'], 'Title') }}`,
  `{{ m.sources([{'label': '...', 'url': '...'}, ...]) }}` (always last, inside the last prose section).
  Slugs: services pool-service, pool-cleaning-maintenance, swimming-pool-repair, pool-pump-repair,
  pool-tile-cleaning, green-pool-cleanup, pool-leak-repair, pool-light-repair; guides pool-service-cost,
  my-pool-is-green, pool-pump-not-working, pool-maintenance-schedule, draining-a-pool-tucson; areas
  oro-valley, catalina-foothills, vail, sahuarita, green-valley.
- Links: use the `url` values in site.json exactly: `/pool-service/`, `/pool-cleaning-maintenance/`,
  `/swimming-pool-repair/`, `/pool-pump-repair/`, `/pool-tile-cleaning/`, `/green-pool-cleanup/`,
  `/pool-leak-repair/`, `/pool-light-repair/`, `/pool-service-cost/`, `/my-pool-is-green/`,
  `/pool-pump-not-working/`, `/tucson-pool-maintenance-schedule/`, `/draining-a-pool-in-tucson/`, town pages
  `/oro-valley-pool-service` (no slash), core `/how-it-works/`, `/service-areas/`, `/services/`, `/about/`,
  `/faq/`, `/contact/`. Link to 3+ related pages naturally in the copy.

## Images
Call: `{{ img('file.jpg', 'alt', 1200, 800, desc='prompt', fallback='pool/x.jpg', fallback_alt='...') }}`.
An existing photo used directly needs no desc/fallback: `{{ img('pool/chem-wide.jpg', 'alt', 1200, 500) }}`.
Every content page: a hero plus at least two in-body images; NO photo twice on one page (count the hero or
its fallback, and the card images of any `m.service_cards` you include; site.json shows each service's
card_image). Alt text with a worker must not imply they work for the line.

Existing photos in src/static/images (bright desert backyards or pool close-ups), with sizes:
- `pool/hero-1.jpg` 1920x800 (curved pool, stucco house with covered patio, lounge chairs, desert plants, a
  saguaro, rocky mountains), `pool/hero-2.jpg` 1920x800 (free-form turquoise pool, flagstone deck, boulders,
  covered patio with dining table, palms, cacti, mountains), `pool/hero-3.jpg` 1920x800 (long rectangular
  pool with white lounge chairs, palms, desert trees, boulders, distant mountains), `img-01.jpg` 1344x768
  (aerial of a kidney-shaped pool with a saguaro, agaves, red boulders and open desert beyond the wall).
- 1200x500 wide crops: `pool/hero-1-wide.jpg`, `pool/hero-2-wide.jpg`, `pool/hero-3-wide.jpg` (same scenes),
  `pool/brush-wide.jpg` (hand pushing a blue brush under clear water), `pool/chem-wide.jpg` (two white
  chemical jugs and a test cup on a deck at sunset), `pool/dusk-wide.jpg` (lit pool at dusk, string lights,
  stone patio, cacti), `pool/equip-wide.jpg` (pump and plumbing beside a tall filter tank, stucco wall),
  `pool/green-wide.jpg` (neglected green pool with leaves, block wall), `pool/repair-wide.jpg` (two hands
  turning a wrench on an old pump, workshop), `pool/skim-wide.jpg` (a man in a pool skimming with a leaf net,
  saguaro behind the wall, face not shown), `pool/test-wide.jpg` (hand holding a water sample vial at the
  surface), `pool/vac-wide.jpg` (robotic cleaner on a sunlit pool floor).
- Tucson photos: `tucson-cleaning-hero.jpg` 1344x768 (a man running a pool pole across a clear rectangular
  pool, tan block wall, desert trees), `tucson-cleaning-skim.jpg` 1344x768 (leaves floating on a pool under
  dark storm clouds, a saguaro and desert trees behind the wall: a monsoon scene), `tucson-cleaning-test.jpg`
  1344x768 (gloved hands holding a water test kit with colored vials over a pool), `tucson-pump-bearings.jpg`
  1344x768 (two rusted old pool pump motors on a workbench), `tucson-pump-hero.jpg` 1344x768 (a man in a
  blue shirt kneeling with a wrench at a pool pump on the deck, agave and block wall), `tucson-pump-vs.jpg`
  1344x768 (a modern pool pump with a digital control on a concrete pad, gravel, agave, stucco wall),
  `tucson-repair-heater.jpg` 1536x640 (close view of corroded, scaled pool pipe and fittings),
  `tucson-repair-hero.jpg` 1536x640 (a man kneeling at a pool pump on a deck, saguaro and rocky mountains),
  `tucson-repair-pump.jpg` 1536x640 (gloved hands holding a pump part crusted with white scale),
  `tucson-tile-after.jpg` 1344x768 (clean blue waterline tile), `tucson-tile-hero.jpg` 1536x640 (long
  rectangular pool with lounge chairs, palms and rocky mountains), `tucson-tile-scale.jpg` 1344x768 (thick
  white calcium scale along blue waterline tile).

Planned new photos (Maurice generates them in Artistly later). Each needs a unique descriptive filename, a
`desc=` prompt and a `fallback=` existing photo. Prompt style: start with "Wide cinematic landscape shot,
subject positioned on right third of frame, well lit," then a specific, bright, realistic Tucson-area scene
(Sonoran desert landscaping with gravel, palo verde and mesquite trees, saguaros, prickly pear and agave,
tan or terracotta stucco homes with flat or tile roofs, block walls, the real mountains for that town),
then "realistic photo, no text, no logos, no house numbers, no recognizable faces".
- Hero = PLANNED `<slug>-hero.jpg` (town pages `<town>-pool-hero.jpg`), 1920x1080, with the fallback given in
  your brief. In-body: existing photos; at most ONE planned in-body photo (1200x800, with an existing
  fallback). Town pages: one planned local in-body photo `<town>-<scene>.jpg`.

## Content each page needs
Service and guide pages (Prompt 9): what it is; who it is for; common problems; what a careful pool
technician does and why; what to expect; options; Tucson-specific context (verified only); safe homeowner
checks where relevant; what to ask; related pages; 3 to 6 FAQs; at least one distinctive design treatment
(symptom table, decision panels, timeline, checklist, comparison table); `m.how_it_works_short()` or a short
plain explanation of the line plus `m.disclosure()`; `m.license_check()` where repair work is discussed.
About 1,400 to 2,000 words of page-specific copy. Sources list at the end.

Area pages (Prompt 11): hero; FIRST H2 names the town ("Vail: ..."), with two local paragraphs and a photo
beside them (split); services genuinely relevant there (`m.service_cards([...])`, avoiding images already on
the page); a section titled "Why [Town] homeowners call the line" with FOUR distinct local reasons as
`<div class="grid-2">` of four `<div class="panel"><h3>..</h3><p>..</p></div>`, built only from facts on
that page plus what the line truly does (free, 24/7, transfers to an independent local company, caller pays
the company not the line, the site explains the ROC license check); verified local context researched for
THAT town: its water provider(s), source water and the hardness its own report gives (only if you find it),
its electric provider (TEP or Trico, carefully: "depending on the address"), county; HOA patterns and
housing age (Census or town data), typical lots and pools where a source says so; named neighborhoods or
master-planned communities; its monsoon and dust exposure; the rules on draining pools there (town rules if
it is an incorporated town, Pima County rules if unincorporated); area FAQs; `m.how_it_works_short()`;
nearby areas (`m.area_pills(exclude='<slug>')`); sources. Never claim an office, address, job history,
customer count or travel time. Small towns with little documented history get shorter pages, honestly,
rather than padding.

## Research standard
- Use the fact bank first. For anything page-specific, research on the web BEFORE writing: WebFetch and curl
  are blocked for most hosts; use WebSearch (mode "standard"), restricted with allowed_domains to official
  domains (tucsonaz.gov, pima.gov, orovalleyaz.gov, sahuaritaaz.gov, roc.az.gov, azleg.gov, azwater.gov,
  weather.gov, census.gov, tep.com, trico.coop, swgas.com, energy.gov, cdc.gov, cpsc.gov, epa.gov,
  extension.arizona.edu, arizona.edu, and the utilities' own sites). Cite the official URL whose content the
  search showed. Your search budget is given in your brief; stay within it.
- Every number, date, rule, phone number, fee and named program comes from a source you saw; that source
  goes in the Sources list with its real URL. If you cannot verify it, leave it out.
- Shared facts (CAP water, monsoon dates, ROC): say them in your own words, only where they matter to that
  page, never the same paragraph twice across pages.

## Validation (from the repo root; NEVER a plain `python3 build.py`, it writes dist/ and docs/)
```
python3 build.py --out /tmp/claude-0/<your-name>/dist
python3 scripts/check.py --dist /tmp/claude-0/<your-name>/dist --skip-links --only <your page URL>
python3 scripts/similarity.py --dist /tmp/claude-0/<your-name>/dist --other /home/user/dominionsoundmusic-create/phoenix-pool-cleaning-pro/dist --only <your page URL as similarity prints it>
```
(similarity prints flat pages as `/vail-pool-service.html`, folder pages as `/pool-light-repair/`.)
build.py may print FAILED for other writers' half-finished pages; ignore those, fix your own. Fix every ERROR
and FAIL for your pages. A WARN about word count under 1500 (which includes the template) on a service or
guide page means the page is thin: add substance, not filler (town pages may be shorter if the town has
little documented). Do not edit shared files or anyone else's pages. Do not commit or push.

When done, report: files written, word counts, for area pages a one-sentence factual summary of the town (max
22 words, no dashes, for site.json), any fact you could not verify and left out, and searches used.
