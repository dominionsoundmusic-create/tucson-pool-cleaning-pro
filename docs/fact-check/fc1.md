# Fact-check fc1 (independent, Oct 20 2026)

Checker fc1 did not write these pages. Method: WebSearch (standard mode, restricted to the official or named domain), plus the verified research bank in docs/research/ and a read of the site code (for privacy-policy claims about analytics and Google Translate). 12 searches used (cap 12).

Validation after edits: `build.py --out /tmp/claude-0/fc1/dist`, `check.py --skip-links --only <url>` = 0 errors on all 9 pages; `similarity.py` against Phoenix = 0 FAIL, max Jaccard 1.3%.

Business-model checks on every page: no "we clean/repair", no claim the line does pool work, vets or vouches for companies, no claim any company is licensed, insured, certified or rated, no named company, no invented prices, reviews or years. All 9 pages pass. One response-time implication was found on the home page and softened (below).

## / (index.html)

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| "Within a minute or two" you are connected or details sent | INTAKE.md | softened | Implied response time; INTAKE gives none. Reworded without a time. |
| July average high about 100 F (1991 to 2020) | weather.gov/twc/TucsonMonthlyNormalExtremes (search) | confirmed | 100.2 F |
| 68 days a year at or above 100 F | same NWS page (search) | confirmed | 1991 to 2020 annual normal 68 |
| Monsoon season June 15 to Sept 30; outflow dust storms | NWS monsoonsafety (research bank) | confirmed | |
| CDC free chlorine at least 2 ppm with stabilizer | cdc.gov home pool page (search) | confirmed | |
| Tucson Water: CAP water recharged in Avra Valley, blended; hardness rises with CAP share; hard water safe; test with a kit | research/water.md (Hard Water page) | confirmed | |
| ADWR: about six feet a year evaporation in Tucson, most in summer | azwater.gov (search) | corrected (source) | Figure is on ADWR's Conservation Technologies page, not the fact sheet; source added, fact sheet relabeled for the cover figure |
| ADWR: cover saves 90 to 95% | ADWR Pools and Spas fact sheet (search) | confirmed | |
| ROC does not require liability insurance | research/licensing-barriers.md (ROC FAQ) | confirmed | |
| TEP or Trico depending on address (south and southeast towns) | research/rules-climate.md | confirmed | |
| Oro Valley runs its own water utility | research/water.md | confirmed | |
| Sources list (9 URLs) | domains and topics | confirmed | One source added (ADWR Conservation Technologies) |

Totals: 12 checked, 10 confirmed, 1 corrected, 1 softened, 0 removed.

## /services/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| ROC contractor search shows active status and recent complaints | research (ROC consumer guide) | confirmed | |
| ROC does not require liability insurance | research (ROC FAQ) | confirmed | |
| CDC: free chlorine at least 1 ppm (2 with stabilizer), pH 7.0 to 7.8 | cdc.gov (search) | confirmed | |
| CDC: never combine pool chemicals; store original containers, dry, locked | research (CDC Pool Chemical Safety) | confirmed | |
| R-6 scope and exclusions (gas lines, electrical past first disconnect, potable plumbing, full plaster or pebble replacement); B-5 for building | research (ROC License Classifications) | confirmed | |
| Pima County green pool / mosquito report line 520-724-7908 | pima.gov/2100/Mosquitoes (search) | confirmed | |
| Pima County and City of Tucson set barrier rules | research (Pima barriers page, City water safety page) | confirmed | |
| Reset GFCI once; if it trips again, leave off | WRITING-GUIDE safety rule | confirmed | Safe-basics guidance |
| Hardened scale usually needs specialized equipment | general | confirmed | General trade knowledge, hedged with "usually" |
| Sources list (10 URLs) | domains and topics | confirmed | |

Totals: 10 checked, 10 confirmed, 0 corrected, 0 softened, 0 removed.

## /service-areas/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Catalina Foothills about 52,400 people, 2020 Census | census.gov QuickFacts (search) | confirmed | 52,401. Source URL corrected to a live QuickFacts table path |
| Catalina Foothills unincorporated; much of it Tucson Water | research/water.md (safe wording) | confirmed | |
| Oro Valley 2023 about 2/3 groundwater, 1/3 CAP; hardness 36 to 270 ppm | research/water.md | confirmed | |
| Vail Water Company private; CAP water stored, recovered and wheeled by Tucson Water | research/water.md | confirmed | |
| Sahuarita town sells no water; seven providers | research/water.md | confirmed | |
| Green Valley: Community Water Co. largest, groundwater; GVDWID and Farmers Water Co. | research/water.md | confirmed | |
| Marana Water is the town utility; Trico headquartered in Marana; some addresses TEP | research/water.md, rules-climate.md | confirmed | |
| Metro Water District serves parts of the northwest side | research/water.md | confirmed | Casas Adobes as an unincorporated area: common knowledge |
| TEP summer on-peak weekdays 3 to 7 p.m. | research/rules-climate.md | confirmed | Page already says "check your own plan" |
| City/County draining: sewer cleanout, 72 hours after chlorine, backwash on own land | research/rules-climate.md | confirmed | |
| Pima County barrier rules for unincorporated areas | research/licensing-barriers.md | confirmed | |
| Monsoon June 15 to Sept 30 | NWS (research) | confirmed | |
| Tucson Water address map for hardness | research/water.md | confirmed | |
| Sources list (20 URLs) | domains and topics | confirmed | Census URL corrected (counted above) |

Totals: 14 checked, 14 confirmed (1 source URL fixed), 0 corrected facts, 0 softened, 0 removed.

## /how-it-works/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Call flow (assistant, transfer with summary, call back details) | INTAKE.md | confirmed | |
| Southwest Gas leak line 877-860-6020, call 911, do not touch switches | swgas.com Report a Leak (search) | confirmed | |
| R-6 service and minor repairs; B-5 building | research (ROC) | confirmed | |
| ROC search shows status, classification, complaints from last two years, bond | research (ROC consumer guide) | confirmed | |
| ROC toll free 1-877-692-9762 | roc.az.gov (search) | confirmed | |
| No insurance requirement except workers' compensation; search does not show insurance | research (ROC FAQ) | confirmed | |
| Recovery Fund up to $30,000 per claimant after discipline or court order; licensed residential contractors only | research (roc.az.gov/recovery-fund, A.R.S. 32-1132.01) | confirmed | |
| Salt cells scale in hard water | general | confirmed | Common knowledge |
| Sources list (9 URLs) | domains and topics | confirmed | |

Totals: 9 checked, 9 confirmed, 0 corrected, 0 softened, 0 removed.

## /about/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| d/b/a of Dominion Digital Group; no owner named | INTAKE.md | confirmed | |
| Referral fee disclosure, 24/7 assistant, no reviews or credentials | INTAKE.md | confirmed | |
| ROC public license database; R-6 = residential pool service and repair | research (ROC) | confirmed | |
| ROC does not require liability insurance (workers' comp aside) | research (ROC FAQ) | confirmed | |
| Monsoon June 15 to Sept 30 (NWS Tucson) | research | confirmed | |
| Tucson Water hardness rises with CAP share (Colorado River) | research | confirmed | |
| "105 degree Saturday" | illustrative | confirmed | Not a statistic |
| Sources list (5 URLs) | domains and topics | confirmed | |

Totals: 8 checked, 8 confirmed, 0 corrected, 0 softened, 0 removed.

## /faq/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Angi: weekly most common, every other week cheaper for lightly used pools | angi.com (search) | softened | Angi says weekly is most common "for active pools"; wording now matches, "cheaper" dropped |
| Angi notes a two week gap leaves more time for buildup | angi.com (search) | softened | Only a city page (outside Arizona) says this; attribution removed, general statement kept |
| Biweekly "lower cost trade that leaves more room for buildup" (body) | angi.com (search) | softened | Reworded to "lighter option for pools that see moderate use" |
| CDC: test free chlorine and pH at least twice a day | cdc.gov (search) | confirmed | |
| NWS: July high about 100, about 68 days at 100 or above | weather.gov (search) | confirmed | |
| Monsoon June 15 to Sept 30 | NWS (research) | confirmed | |
| ADWR six feet a year; cover saves 90 to 95% | azwater.gov (search) | corrected (source) | Conservation Technologies page added as the six-foot source |
| HomeAdvisor Tucson pool cleaning $92 to $288 per visit | research/costs-equipment.md; re-search | confirmed (research bank) | My own two searches did not reproduce the figure; relied on the research bank's verified entry. Recommend a re-check on the live page |
| HomeGuide national $80 to $150 a month | research/costs-equipment.md | confirmed | |
| Tucson Water hardness and CAP share | research | confirmed | |
| City of Tucson: sewer cleanout preferred; backwash soaks in within 24 hours, not onto neighbors, street, alley | research | confirmed | |
| R-6 scope; B-5; ROC silent on cleaning only | research | confirmed | |
| ROC search shows status, classification, complaints, bond; no insurance shown | research | confirmed | |
| CDC chemical safety: never mix, chlorine with acid, original containers, below 95 F | research | confirmed | |
| Southwest Gas 877-860-6020 | swgas.com (search) | confirmed | |
| Pima County 520-724-7908 | pima.gov (search) | confirmed | |
| Arizona law and local codes set fencing and gate rules | research (A.R.S. 36-1681, Pima) | confirmed | |
| ES toggle uses Google Translate | site code (src/static/js/site.js) | confirmed | |
| Sources list (17 URLs) | domains and topics | confirmed | One source added |

Totals: 19 checked, 15 confirmed, 1 corrected, 3 softened, 0 removed.

## /contact/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Phone only, no email or form, 24/7 assistant | INTAKE.md | confirmed | |
| Southwest Gas 877-860-6020 and 911 | swgas.com (search) | confirmed | |
| ROC accepts homeowner complaints online | roc.az.gov/file-complaint (search) | confirmed | Source URL matches |
| Assistant "may record or log" call details | INTAKE.md (not stated) | confirmed (hedged) | INTAKE says details are taken and passed along; "may" keeps it a possibility, not a promise. Maurice should confirm whether calls are recorded |
| Sources list (3 URLs) | domains and topics | confirmed | |

Totals: 5 checked, 5 confirmed, 0 corrected, 0 softened, 0 removed.

## /privacy-policy.html

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Google Analytics 4 is used | src/data/site.json (ga4 id set), base.html | confirmed | |
| Event recorded when a phone link is tapped | base.html gtag `phone_call_click` | confirmed | |
| _ga cookie | Google cookies policy (cited) | confirmed | |
| googtrans cookie set on ES; Translate loads only after choosing ES; EN removes cookie | src/static/js/site.js | confirmed | Matches code exactly |
| No forms, no sign up, no email list | INTAKE.md, templates | confirmed | |
| Call may be recorded; details logged; shared with the connected company | INTAKE.md | confirmed (hedged) | Recording not stated in INTAKE; phrased as "may". Flag for Maurice |
| Telephone, call handling and hosting providers may process data | general | confirmed (hedged) | |
| GA opt-out add-on exists | tools.google.com (cited) | confirmed | |
| No promised retention period, deletion process or contact email | INTAKE.md | confirmed | Policy makes no practice promises beyond what the code and INTAKE support |

Totals: 9 checked, 9 confirmed, 0 corrected, 0 softened, 0 removed.

## /terms.html

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Line is a referral service, not a contractor, holds no license | INTAKE.md | confirmed | |
| Companies may pay referral fees; callers never billed | INTAKE.md | confirmed | |
| Line does not verify licenses or insurance | INTAKE.md | confirmed | |
| Disputes with licensed contractors can go to the ROC | roc.az.gov/file-complaint (search) | confirmed | |
| Safety statements (never mix chemicals, gas smell: leave, 911 and Southwest Gas) | CDC, Southwest Gas (research/search) | confirmed | |
| Governed by Arizona law | INTAKE.md (not stated) | confirmed (business choice) | Not a factual claim; flag for Maurice to approve |

Totals: 6 checked, 6 confirmed, 0 corrected, 0 softened, 0 removed.

## Grand totals

| Page | Checked | Confirmed | Corrected | Softened | Removed |
|---|---|---|---|---|---|
| / | 12 | 10 | 1 | 1 | 0 |
| /services/ | 10 | 10 | 0 | 0 | 0 |
| /service-areas/ | 14 | 14 | 0 | 0 | 0 |
| /how-it-works/ | 9 | 9 | 0 | 0 | 0 |
| /about/ | 8 | 8 | 0 | 0 | 0 |
| /faq/ | 19 | 15 | 1 | 3 | 0 |
| /contact/ | 5 | 5 | 0 | 0 | 0 |
| /privacy-policy.html | 9 | 9 | 0 | 0 | 0 |
| /terms.html | 6 | 6 | 0 | 0 | 0 |
| **Total** | **92** | **86** | **2** | **4** | **0** |

Plus 1 source URL fix (Census QuickFacts path on /service-areas/). Searches used: 12 of 12.

Open items for Maurice (not errors): confirm whether calls to the line are recorded (privacy and contact pages say "may"), and approve the Arizona governing-law line in the terms. The HomeAdvisor Tucson $92 to $288 figure on /faq/ rests on the research bank; a fresh search did not reproduce it, so re-check it on the live HomeAdvisor page before launch.
