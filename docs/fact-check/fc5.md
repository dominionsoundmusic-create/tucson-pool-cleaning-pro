# Fact-check fc5: town pages (Oct 20 2026)

Checker: fc5 (independent; did not write these pages). Method: WebSearch (standard mode, restricted to the
official or named domain); search result summaries of the cited pages taken as evidence. Facts already in
docs/research/*.md (verified there with URLs) were relied on and checked for correct wording. 20 searches used
(cap 20).

Pages: /oro-valley-pool-service, /catalina-foothills-pool-service, /vail-pool-service, /sahuarita-pool-service,
/green-valley-pool-service, plus the five "areas" summary strings in src/data/site.json.

Validation after edits: `build.py --out /tmp/claude-0/fc5/dist` built 28 pages; `check.py --skip-links --only`
returned 0 errors, 0 warnings for all five URLs; `similarity.py` (full run; `--only` does not match flat town URLs)
showed area pairs max 0.8%, max against Phoenix 1.3%, 0 pages sharing an 8-word run, no FAIL.

## /oro-valley-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Barrier top at least 60 in above grade, outside face | orovalleyaz.gov pool permit page, 2024 ISPSC amendments | confirmed | 2018 amendments raised it from 48 to 60 |
| FAQ: gates shut, latch and "open outward" | 2024 amendments, pool permit page | corrected | Not found in town rules. Now says latching hardware 54 in or higher and doors to the pool area self-closing and self-latching |
| Handbook: gates self-close, open outward, latch 54 in | 2019 Residential Construction Handbook | corrected | Handbook excerpt has no gate rule; 54 in latching and self-closing doors now credited to the 2024 amendments |
| Equipment at least 48 in from barrier or enclosed separately | 2019 handbook | confirmed | Now says it is the 2019 handbook, which predates the current amendments |
| Older town documents show a lower height | 2012 code (4 ft), 2019 handbook (5 ft) | confirmed | |
| Incorporated April 15, 1974 | OV-50 digital timeline | confirmed | |
| Started at about 2.5 sq mi with about 1,200 residents | town history documents | softened | Town sources differ (2.4 or 2.5 sq mi; 800 or nearly 1,200 people). Now credited to "town history documents" |
| 2020 Census population 47,070 | research and Census | confirmed | Matches site.json summary "about 47,000" |
| Rancho Vistoso PAD 1987, 7,626 acres, first neighborhood Del Webb's Sun City Vistoso | Rancho Vistoso PAD PDF | confirmed | |
| Rancho Vistoso is "the largest" planned community | none | softened | Now "one of the biggest" |
| Stone Canyon HOA with CC&Rs; La Reserve PAD | cited town planning PDFs (La Reserve PAD #4 seen in results) | confirmed | Stone Canyon relied on the cited document |
| Catalina State Park about 5,500 acres of foothills, canyons, streams | azstateparks.com | confirmed | Park history page says 5,525 |
| About 65% groundwater, 35% CAP (2023) | research/water.md | confirmed | |
| Hardness 36 to 270 ppm, 2.1 to 15.8 gpg, varies by CAP blend in pressure zone; over 180 very hard; 520-229-5000 | research/water.md | confirmed | |
| Evaporation about six feet a year | research (ADWR) | confirmed | |
| TEP substation near Lambert Ln and First Ave; on-peak 3 to 7 p.m. weekdays; morning or midday pumps | research/rules-climate.md | confirmed | |
| Draining: curbed road, storm drain or wash only off neighbors, no erosion, chlorine under 1 ppm; no unpaved roads or alleys; salt pools to sewer; backwash not to streets or washes, on site only if absorbed | orovalleyaz.gov Drain Your Pool Guidelines and PDF | confirmed | |
| Stormwater Utility 520-229-4850 | orovalleyaz.gov search result | confirmed | |
| 2024 amendments say backwash and drain water must be contained on site | 2024 amendments | removed | Not confirmed, and it contradicts the street drainage conditions. Replaced with a neutral line saying the town's guidelines differ |
| Monsoon June 15 to Sept 30; dust storms most often form north and west of Tucson | research (NWS) | confirmed | |
| Southwest Gas 877-860-6020; CDC chemical storage | research | confirmed | |

Totals: 21 claims checked; 15 confirmed, 3 corrected, 2 softened, 1 removed.

## /catalina-foothills-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Census-designated place; 2020 pop 52,401, 2010 50,796; nearly 42 sq mi of land | census.gov QuickFacts | confirmed | 41.85 sq mi land in 2020 |
| Catalina Foothills Area Plan; Black Wash kept as riparian habitat | pima.gov Special Area Policies | confirmed | |
| Hillside Development Zone "requires grading plans and slope stabilization details" | pima.gov checklist (not searched) | softened | Now just says steep lots come with the county's hillside development checklist |
| Sabino Canyon draws more than a million visitors a year; flash flood warning | fs.usda.gov brochure | confirmed | |
| Bighorn Fire 2020 raised flash flood and mudflow risk; faster, larger than a typical monsoon storm | pima.gov Bighorn Fire Flood Risk | confirmed | |
| Flood district issued post-fire maps and "property notices" for watersheds "including Esperero" | pima.gov | corrected | Results show preliminary floodplain and inundation maps for washes including Finger Rock and Valley View; Esperero and property notices not confirmed |
| Esperero Wash overtops Sunrise Dr more often from fire sediment; two corrugated metal pipes replaced by six concrete box culverts ("replaced") | pima.gov project page and newsletter | corrected | Construction began Jan 5 2026, completion status unconfirmed. Now "began construction in January 2026, swaps two undersized pipes for larger concrete box culverts" |
| Finger Rock Wash flooded in July 2022 after rain on the burn scar | pima.gov | removed | No such event found (only an August 2022 Finger Rock floodplain study) |
| Panel: "Since the Bighorn Fire, foothills washes carry more water and sediment" | pima.gov | softened | Now: the county says the fire raised the risk of faster, larger flows |
| Pima County barrier 48 in outside, bottom 2 in, 4 in sphere, gates outward, self-closing and self-latching | research/licensing-barriers.md | confirmed | |
| Water Resources Element names Tucson Water for the Catalina Foothills planning area | pima.gov 4.2 Water Resources Element | confirmed | Page keeps "check your bill" |
| Tucson Water hardness rises with CAP share, safe to drink, pool test kit | research/water.md | confirmed | |
| Draining rules (sewer cleanout first, 72 h, pH 7 to 8, backwash 24 h, last resort street) | research/rules-climate.md | confirmed | |
| Monsoon dates; Pima County mosquito line 520-724-7908; SW Gas 877-860-6020 | research | confirmed | |
| R-6 covers service and repair; building or replastering under construction licenses | research/licensing-barriers.md | confirmed | |

Totals: 15 claims checked; 10 confirmed, 2 corrected, 2 softened, 1 removed.

## /vail-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Unincorporated CDP; 2020 pop 13,604, 2010 10,208 ("about a third" growth) | census.gov QuickFacts | confirmed | 33.3% |
| 2.95 persons per household, nearly a quarter under 18, about 91% owner occupied | census.gov QuickFacts | confirmed | ACS 2020 to 2024 (23.7%, 91.1%); page says "recent Census survey figures" |
| Colossal Cave Mountain Park in the Rincon foothills | pima.gov (cited, not searched) | confirmed | Low risk, county park page cited |
| Cienega Creek Natural Preserve about 25 miles SE of downtown, year-round flow stretches | pima.gov | confirmed | |
| Specific plans include Vail Valley Ranch (Rancho del Lago) and Rocking K | pima.gov Specific Plans | confirmed | |
| County area policy calls for trails linking the two | pima.gov | removed | Not confirmed; sentence and its Special Area Policies source removed |
| Vail Water: private, CAP wheeled through Tucson Water via Old Vail Reservoir; ACC report 2025: 100% CAP from City of Tucson; Rincon Water Company nearby | research/water.md | confirmed | |
| No published Vail Water hardness | research/water.md | confirmed | |
| TEP Vail substation; Trico Vail/Corona de Tucson board district; TOU 3 to 7 p.m. | research/rules-climate.md | confirmed | |
| Pima County barrier details incl. 1.75 in chain link | research | confirmed | |
| Draining guidelines; septic homes ask Pima County onsite wastewater | research; Oro Valley's guidelines also bar pool water in septic | confirmed | |
| Monsoon dates; SW Gas number | research | confirmed | |

Totals: 12 checked; 11 confirmed, 0 corrected, 0 softened, 1 removed.

## /sahuarita-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Incorporated September 20, 1994; about 1,800 residents then | sahuaritaaz.gov (State of the Town 2019, Get to Know Us) | confirmed | |
| 2020 pop 34,134; 2010 25,259 | census.gov QuickFacts | confirmed | |
| Sahuarito Ranch 1879 to 1886; "little saguaro" | sahuaritaaz.gov history | confirmed | |
| Santa Cruz River and pecan groves | cited 2015 Town news release (not searched) | confirmed | Kept as cited; low risk |
| Rancho Sahuarita planned for 11,680 homes; Quail Creek about 5,000; more units in planning | sahuaritaaz.gov Strategic Plan, 2026 project reports | softened | Plan dates from about 2008; page now says so. Quail Creek Specific Plan 2 (up to 1,850 homes) confirms the expansion |
| About 1 in 5 residents 65+, about 81% owner occupied | census.gov QuickFacts | confirmed | 21.1%, 81.0% |
| Town does not provide water; seven providers named; phone numbers | research/water.md | confirmed | |
| Area relies on groundwater (2018 study session) | research/water.md | confirmed | |
| Wastewater FAQ: private cleanout access cap, control flow so lateral does not overflow, no public manholes or street cleanouts (traffic and safety) | sahuaritaaz.gov FAQ and Guidelines to Empty a Pool | confirmed | |
| Trico Sahuarita district; TEP Santa Rita Connection; TOU hours | research | confirmed | |
| Evaporation, monsoon dates, SW Gas, CDC storage | research | confirmed | |

Totals: 11 checked; 10 confirmed, 0 corrected, 1 softened, 0 removed.

## /green-valley-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Unincorporated; 2020 pop 22,616, 2010 21,391 | census.gov QuickFacts | confirmed | |
| About 80.5% 65 or older; about 86% owner occupied | census.gov QuickFacts | confirmed | 86.2% (2020 to 2024) |
| Mount Wrightson rises more than 7,000 ft above surrounding lowlands | fs.usda.gov Mount Wrightson Wilderness | confirmed | |
| Madera Canyon on the range's north side; reached from I-19 via Continental Road | fs.usda.gov Santa Rita Mountains, picnic area page | confirmed | Madera Canyon drains the north side; exit number relied on the cited trailhead page |
| GVR runs pools and spas at its recreation centers for members | gvrec.org (cited, not searched) | confirmed | Relied on cited GVR pages; low risk |
| Water providers: Community Water Co. (since June 1977, about 22,085 served, pursuing CAP), GVDWID (May 2003, south of Mission Twin Buttes, about 4,400 residential connections), Farmers Water Co (about 4,290 people, about 1,700 connections), Valle Verde del Norte; groundwater | research/water.md | confirmed | |
| No published hardness | research/water.md | confirmed | |
| CDC home pool pH 7.0 to 7.8, FC at least 1 ppm, 2 ppm with stabilizer | research | confirmed | |
| RWRD runs a Green Valley treatment plant; sewer preferred; draining steps | research and cited Pima WRF page | confirmed | WRF page not searched separately |
| TEP or Trico by address; Trico Green Valley district; Santa Rita Connection; Southwest Gas serves Green Valley | research/rules-climate.md | confirmed | |
| Pima County barrier 48 in; mosquito line 520-724-7908 | research | confirmed | |

Totals: 11 checked; 11 confirmed, 0 corrected, 0 softened, 0 removed.

## site.json area summaries

| Summary | Verdict | Note |
|---|---|---|
| oro-valley: 1974, about 47,000, own utility, 60 in barrier, draining guidelines | confirmed | |
| catalina-foothills: about 52,400, flood risk rose after 2020 Bighorn Fire | confirmed | |
| vail: 13,604 in 2020, "served mostly by Vail Water Company's CAP supply" | softened | "Mostly" not verified; now "where Vail Water Company delivers Central Arizona Project water" |
| sahuarita: 1994, Santa Cruz River, Rancho Sahuarita, Quail Creek, seven groundwater providers | confirmed | |
| green-valley: about 80% 65 or older | confirmed | |

## Totals

| Page | Checked | Confirmed | Corrected | Softened | Removed |
|---|---|---|---|---|---|
| Oro Valley | 21 | 15 | 3 | 2 | 1 |
| Catalina Foothills | 15 | 10 | 2 | 2 | 1 |
| Vail | 12 | 11 | 0 | 0 | 1 |
| Sahuarita | 11 | 10 | 0 | 1 | 0 |
| Green Valley | 11 | 11 | 0 | 0 | 0 |
| site.json summaries | 5 | 4 | 0 | 1 | 0 |
| **All** | **75** | **61** | **5** | **6** | **3** |

Searches used: 20 of 20. Not separately searched (relied on the page's cited official source; low risk):
Stone Canyon HOA document, Colossal Cave location, Sahuarita pecan groves, GVR pools, the Green Valley WRF page
and the Continental Road exit number.
