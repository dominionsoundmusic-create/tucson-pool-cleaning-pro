# Fact-check fc3 (Oct 20 2026)

Independent checker fc3 (did not write these pages). Pages: swimming-pool-repair, pool-leak-repair,
pool-light-repair, pool-pump-repair, pool-pump-not-working. Evidence: WebSearch summaries restricted to the
named publisher's domain (18 searches), plus facts already verified in docs/research/*.md (marked "bank").
Validation: build to /tmp/claude-0/fc3/dist, check.py 0 errors on all five pages, similarity.py no FAIL
(max Jaccard vs Phoenix 0.8%, no shared 8-word runs).

## /swimming-pool-repair/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| HomeAdvisor Tucson pool repair average $371, $148 to $598 | homeadvisor.com search | corrected | Tucson figure not found on any HomeAdvisor Tucson page (attribution was already uncertain in the bank). Replaced with HomeAdvisor national guide (2025 data): average about $725, often $85 to $3,500; source URL swapped to /cost/.../repair-a-swimming-pool/ |
| DIFI: homeowners insurance is for sudden, unexpected losses; worn systems belong to home warranties/service contracts | difi.az.gov search | confirmed | Homeowners page and Home Warranty consumer guide |
| "Damage from poor upkeep / lack of upkeep is generally excluded" (FAQ and body) | difi.az.gov search | softened | DIFI says failures from normal wear and aging are generally not covered; reworded to that |
| Tucson Water suggests a test kit for hardness and following manufacturer guidelines | tucsonaz.gov search | softened | City says "use a pool test kit to measure hardness" and maintain systems per manufacturer; reworded to match (not addressed to pool owners specifically) |
| Tucson groundwater naturally hard; harder as CAP share rises | tucsonaz.gov search + bank | confirmed | |
| City of Tucson backwash: on own property only if absorbed within 24 hours, no flow to neighbor, street or alley | bank (rules-climate.md) | confirmed | Stated correctly |
| Monsoon June 15 to September 30; dust storms near-zero visibility | bank | confirmed | |
| About 68 days a year at or above 100 F | bank | confirmed | |
| DOE: heat pump moves heat rather than making it | energy.gov search (pool heater rulemaking) | confirmed | |
| Southwest Gas 877-860-6020, call 911, leave area, no switches | bank | confirmed | |
| ROC R-6 scope (minor repairs; excludes gas lines, electrical beyond first disconnect, potable plumbing, full plaster/pebble or deck replacement); B-5 | bank | confirmed | |
| ROC R-11 is the residential electrical classification | roc.az.gov search | confirmed | |
| ROC search does not show insurance; only workers' comp required | bank | confirmed | |
| CDC: never mix pool chemicals | bank | confirmed | |
| Generic equipment descriptions (filters, valves, salt cells) | common knowledge | confirmed | No DIY electrical or gas steps; covers stay on |

Totals: 15 checked, 12 confirmed, 1 corrected, 2 softened (3 edits incl. FAQ), 0 removed (1 source replaced).

## /pool-leak-repair/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| ADWR: about six feet a year evaporates in Tucson, mostly summer; cover saves 90 to 95% | bank | confirmed | ~0.2 in/day arithmetic correct |
| 68 days at or above 100 F | bank | confirmed | |
| Tucson Water Zanjero free water efficiency checkup | tucsonaz.gov search | confirmed | |
| Pool water to sanitary sewer via home cleanout preferred | bank | confirmed | |
| Angi leak detection $100 to $1,000, average $300 | angi.com search | confirmed | |
| Angi pressure test $200 to $500; pinpoints leak without disturbing yard | angi.com search | confirmed | |
| Angi excavation $500 to $5,000 | angi.com search | confirmed | |
| Angi describes dye as low-cost check for spots like skimmer | angi.com search | softened | Not found; Angi attribution removed, generic description kept |
| HomeGuide leak repair "$500 to $1,500; $100 to $5,000 in-ground" | homeguide.com search | corrected | HomeGuide: $500 to $1,500 average for in-ground, up to about $5,000 for extensive work |
| HomeGuide liner patch $150 to $300 pro, $20 to $100 kit; kits not always strong enough | homeguide.com search | confirmed | Publisher cell corrected to the liner cost guide |
| HomeGuide liner replacement $2,000 to $7,500 up to 800 sq ft | homeguide.com search | confirmed | |
| ROC R-6 vs B-5 scope | bank | confirmed | |

Totals: 12 checked, 10 confirmed, 1 corrected, 1 softened (plus 1 publisher label fix), 0 removed.

## /pool-light-repair/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| CPSC: NEC has required GFCI for underwater pool lighting since 1968 | bank (cpsc.gov fact sheet) | confirmed | |
| CPSC/Red Cross: older pools biggest concern; test GFCIs at least monthly | bank | confirmed | |
| NFPA electric shock drowning: current disables muscles, swimmer cannot stay afloat | nfpa.org search | confirmed | |
| R-6 excludes electrical beyond first disconnect; R-11 residential electrical | roc.az.gov search + bank | confirmed | |
| NWS July average low about 76 F at Tucson airport | weather.gov search | confirmed | 1991 to 2020 normal 76.3 F |
| Afternoon highs near 100 | bank | confirmed | July normal 100.2 F |
| Monsoon June 15 to Sept 30 | bank | confirmed | |
| Angi light repair $65 to $150; replacement about $625 avg | angi.com search | confirmed | |
| Angi LED $700 to $1,500, incandescent $450 to $650, fiber optic $1,300 to $1,700 | angi.com search | confirmed | Added Angi pool light replacement cost guide to sources |
| Low-voltage lights via listed transformer exist | bank | confirmed | |
| DIY: only switch, schedule, monthly GFCI test, one reset; no fixture or wiring work | rule check | confirmed | Technician steps are described as pro work, not instructions |

Totals: 11 checked, 11 confirmed, 0 corrected, 0 softened, 0 removed (1 source added).

## /pool-pump-repair/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Angi pump repair $100 to $700, many near $350; seal $100 to $250; impeller $120 to $300; motor repair $200 to $500; motor replacement $350 to $700 | angi.com search | confirmed | |
| Angi seals often replaced every two to three years | angi.com search | confirmed | |
| Angi replacement average about $1,300, $700 to $4,000 | angi.com search | confirmed | |
| Variable-speed installed $800 to $2,500 (Angi, HomeAdvisor) | angi.com search + bank | confirmed | |
| Angi pump life 8 to 15 years | angi.com search | confirmed | Another Angi page says 8 to 12; page wording "roughly" is fair |
| Replace when repair passes about half a new pump's price | angi.com search + bank | confirmed | |
| DOE: 1.15 to 5 THP motors made on/after Sept 29 2025 need variable-speed control; 0.5 to under 1.15 THP Sept 28 2027 | bank + energy.gov search | confirmed | |
| April 2026 DOE enforcement policy delays small-motor enforcement for motors made before March 26 2029 | energy.gov search | confirmed | Policy dated April 24 2026 |
| ENERGY STAR: half speed uses about one-eighth the energy | energystar.gov search | confirmed | |
| TEP summer on-peak 3 to 7 p.m. weekdays; pump in morning or midday | bank | confirmed | Page says check current hours |
| TEP has offered pump rebates in the past; ask TEP | bank | confirmed | No current rebate claimed |
| TEP or Trico depending on address | bank | confirmed | |
| 68 days at or above 100 F; monsoon dates | bank | confirmed | |
| Tucson Water hardness rises with CAP share | tucsonaz.gov search | confirmed | |
| R-6 scope; insurance not shown, only workers' comp required | bank | confirmed | |

Totals: 15 checked, 15 confirmed, 0 corrected, 0 softened, 0 removed.

## /pool-pump-not-working/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Hum without spinning = capacitor, jammed impeller, overheating "according to Angi" | angi.com search | softened | Angi attribution not found; kept as general possibilities with no attribution, still "turn it off and call" |
| Running dry overheats and damages pump (Angi) | angi.com search | softened | Angi says a pump drawing air from low water can be damaged; reworded |
| Angi: air leaks the leading reason a pump loses prime | angi.com search | softened | "usual reason", "worn O-rings" to match |
| Angi: water about halfway up the skimmer opening | angi.com search | confirmed | |
| CPSC: test GFCIs at least monthly | bank | confirmed | |
| ADWR six feet a year evaporation | bank | confirmed | |
| NWS July high about 100; 68 days at/above 100 (1991 to 2020) | bank | confirmed | |
| Monsoon June 15 to Sept 30 | bank | confirmed | |
| TEP on-peak 3 to 7 p.m. weekdays; morning/midday; Trico possible | bank | confirmed | |
| R-6 excludes electrical beyond first disconnect | bank | confirmed | |
| CDC never mix chemicals | bank | confirmed | |
| DIY limited to timer, one reset, water level, baskets with pump off, lid look, valves, gauge, clearing debris | rule check | confirmed | No electrical or gas instructions |

Totals: 12 checked, 9 confirmed, 0 corrected, 3 softened, 0 removed.

## Overall
65 claims checked: 57 confirmed, 2 corrected, 6 softened, 0 removed (sources: 1 replaced, 1 added).
Searches used: 18 of 18.
