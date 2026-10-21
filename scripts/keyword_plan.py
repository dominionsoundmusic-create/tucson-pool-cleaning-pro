#!/usr/bin/env python3
"""Assign every keyword in keywords/Tucson-Pool-Keywords.xlsx to a page (target or supporting)
or to the deliberately-unused list with a one-line reason. Writes docs/keyword-plan.md.

Usage: python3 scripts/keyword_plan.py   (exit code 1 if any row is left unclassified)
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "home": "/", "services": "/services/", "areas": "/service-areas/", "faq": "/faq/",
    "service": "/pool-service/", "cleaning": "/pool-cleaning-maintenance/", "repair": "/swimming-pool-repair/",
    "pump": "/pool-pump-repair/", "tile": "/pool-tile-cleaning/", "green": "/green-pool-cleanup/",
    "leak": "/pool-leak-repair/", "light": "/pool-light-repair/",
    "g-cost": "/pool-service-cost/", "g-green": "/my-pool-is-green/", "g-pump": "/pool-pump-not-working/",
    "g-schedule": "/tucson-pool-maintenance-schedule/", "g-drain": "/draining-a-pool-in-tucson/",
    "town:oro-valley": "/oro-valley-pool-service", "town:catalina-foothills": "/catalina-foothills-pool-service",
    "town:green-valley": "/green-valley-pool-service", "town:vail": "/vail-pool-service",
    "town:sahuarita": "/sahuarita-pool-service",
}

# Primary target keyword(s) of each page. The rest of its assigned keywords are supporting.
TARGETS = {
    "swimming pool service tucson": "home", "pool service tucson": "home",
    "pool service companies tucson": "services", "pool service arizona": "areas",
    "how often does pool service come": "faq",
    "weekly pool service tucson": "service",
    "pool cleaning service tucson az": "cleaning", "tucson pool cleaning service": "cleaning",
    "swimming pool repair tucson": "repair",
    "pool pump repair tucson": "pump", "pool pump repair tucson az": "pump",
    "pool tile cleaning tucson az": "tile", "pool tile cleaning tucson": "tile", "tucson pool tile cleaning": "tile",
    "green pool cleanup tucson": "green", "pool leak repair tucson": "leak",
    "tucson pool service cost": "g-cost", "my pool is green what do i do": "g-green",
    "pool pump stopped working": "g-pump", "pool maintenance schedule": "g-schedule",
    "tucson pool water recycling": "g-drain",
    "pool cleaning oro valley": "town:oro-valley", "pool cleaning catalina foothills": "town:catalina-foothills",
    "pool service green valley az": "town:green-valley", "pool service vail az": "town:vail",
    "pool service sahuarita az": "town:sahuarita",
}
# The light repair page targets "pool light repair tucson", which is not a row in the file (see SERVICES.md).

U_PUBLIC = "a public pool, city pool or pool-hours search (CLAUDE.md: public-pool searches go in the unused list)"
U_BRAND = "names a specific pool company or brand (CLAUDE.md rule 3: never name a pool company)"
U_PLACE = "a place outside the Tucson metro (CLAUDE.md rule 4)"
U_JOBS = "jobs or job descriptions for pool workers, not a homeowner service"
U_SUPPLY = "shopping for parts or products, not a service"
U_OFF = "off-topic: not about caring for or repairing a home pool"

UNUSED = [  # first match wins
    (r"\bjobs?\b|job description", U_JOBS),
    (r"santee|bullhead|salt lake|queen creek|casa grande|gold canyon|green bay|rancho santa fe|saginaw|camarillo|"
     r"fulshear|marathon fl|mission tx|salinas|san jacinto|grass valley|south scottsdale|glendale az|85048|85053|"
     r"yuma|gilbert", U_PLACE),
    (r"splash pool|e ?konomy|ambiance|boulton|luna pool|aaa pool|blue knight|blue ?point|abcs|gila pool|joe's|oasis pool|"
     r"quality pool service|reflections|great valley|kayak|touch of class|affordable pool|asp pool|cabana boys|"
     r"dedicated pool|desert shadows|desert willow|doc's|dynasty|eclipse|greg's|island pool|kona pool|legacy pool|"
     r"leslie's|lido|michael's|northwest pool care|park pool service|phoenix pro|pool hawk|re ?phresh|sapphire|"
     r"sparkle and splash|terry's|true blue|tucson pool service inc|can you fix my pool llc|green out|desert pool repair",
     U_BRAND),
    (r"hours|is the valley pool open|pools in tucson open|green valley pool prices|green valley az pools|"
     r"pool in catalina az", U_PUBLIC),
    (r"repair parts|pool cleaners for inground pools", U_SUPPLY),
    (r"green cleaning tucson|green patches in pool|green pool report", U_OFF),
]

EXPLICIT = {  # supporting keywords, by page
    "home": ["pool service in tucson", "tucson pool cleaning", "pool cleaning tucson az", "pool cleaning in tucson",
             "pool service near me", "pool maintenance in tucson", "best pool service tucson", "best pool service tucson az"],
    "services": ["pool repair companies tucson", "pool repair companies in tucson", "pool cleaning companies in tucson az",
                 "pool cleaning companies in tucson", "tucson pool cleaning companies", "pool companies that clean pools",
                 "pool chemical service tucson", "tucson pool service reviews"],
    "areas": ["pool service east tucson", "pool cleaning az", "pool cleaning in arizona", "pool cleaning marana"],
    "faq": ["how often pool cleaner", "how often to service a pool", "how often do you service a pool"],
    "service": ["pool maintenance service near me", "pool service salt water", "how often do you service a salt water pool"],
    "cleaning": ["pool cleaners near me", "how often pool cleaning", "how many times should a pool be cleaned",
                 "pool cleaning instructions"],
    "repair": ["tucson pool repair", "swimming pool repair tucson az", "pool repair tucson", "pool repair tucson az",
               "pool repair near me", "pool repair service near me", "pool repair in tucson", "pool repair tucson arizona",
               "best pool repair tucson", "is pool repair covered by insurance"],
    "pump": ["pool pump repair near me", "pool pump repair cost", "can a pool pump be repaired", "who can repair a pool pump",
             "pool pump replacement tucson", "tucson pool pump", "tucson pool pumps", "pool pump repair shop near me",
             "pool pump repair in tucson"],
    "tile": ["pool tile cleaning near me", "pool tile cleaning cost", "arizona pool tile cleaning", "pool tile cleaners tucson",
             "pool tile cleaning tucson cost", "when cleaning pool tile you should", "tucson pool tile",
             "swimming pool tile cleaning near me", "pool tile cleaning and repair near me", "best pool tile cleaning tucson"],
    "green": ["green pool cleaning service tucson", "green pool cleaning tucson", "green pool cleanup cost",
              "how much does it cost to fix a green pool"],
    "leak": ["pool line repair near me", "how to fix a small hole in a pool", "pool lining repair near me"],
    "light": ["pool lights repair near me"],
    "g-cost": ["pool service cost", "pool cleaning cost", "how much does pool service cost", "pool cleaning rates",
               "how much is a pool service per month", "how much does it cost to get my pool cleaned",
               "what does pool cleaning cost", "how much does pool service cost in arizona", "how much is pool service in arizona",
               "how much is pool service in tucson", "pool service tucson prices"],
    "g-pump": ["pool pump troubleshooting guide", "reasons pool pump not working", "what can cause a pool pump to stop working"],
    "g-schedule": ["how often pool maintenance", "how often maintain pool", "pool maintenance steps", "pool opening service near me",
                   "pool opening service cost", "what does pool opening service include",
                   "do i need to clean my pool before closing it"],
    "town:oro-valley": ["oro valley pool service", "oro valley pool services", "oro valley pool repair",
                        "pool service oro valley prices"],
    "town:catalina-foothills": ["pool service catalina foothills", "catalina pool service", "catalina foothills pool",
                                "catalina pool repair"],
    "town:green-valley": ["pool service in green valley az", "who provides water for green valley az"],
    "town:vail": ["pool cleaning vail az", "vai pool services"],
    "town:sahuarita": ["pool service sahuarita", "sahuarita az pool"],
}
SUPPORT = {kw: page for page, kws in EXPLICIT.items() for kw in kws}


def classify(kw):
    k = kw.lower().strip()
    if k in TARGETS:
        return ("page", TARGETS[k])
    if k in SUPPORT:
        return ("page", SUPPORT[k])
    for pat, why in UNUSED:
        if re.search(pat, k):
            return ("unused", why)
    return None


def main():
    wb = openpyxl.load_workbook(ROOT / "keywords" / "Tucson-Pool-Keywords.xlsx", read_only=True)
    rows = list(wb["ALL"].iter_rows(values_only=True))[1:]
    types = {}
    for ws in wb.worksheets[1:]:
        for r in list(ws.iter_rows(values_only=True))[1:]:
            if r[0]:
                types[r[0]] = r[1]
    seen, assigned, unused, missing = set(), defaultdict(list), [], []
    for kw, vol, sd, cpc, seeds in rows:
        if not kw or kw in seen:
            continue
        seen.add(kw)
        typ = types.get(kw, "")
        c = classify(kw)
        if c is None:
            missing.append(kw)
            continue
        kind, val = c
        if kind == "unused":
            unused.append((kw, vol, sd, typ, val))
            continue
        url = PAGES[val]
        role = "TARGET" if kw.lower() in TARGETS else "supporting"
        if role == "supporting" and re.search(r"near me\b", kw):
            role = "supporting (near me: national volume)"
        elif role == "supporting" and not re.search(r"tucson|arizona|\baz\b|oro valley|catalina|green valley|vail|vai |sahuarita|marana", kw):
            role = "supporting (national volume)"
        assigned[url].append((kw, vol, sd, typ, role))
    if missing:
        print("UNCLASSIFIED:", missing)
        return 1
    n_as = sum(len(v) for v in assigned.values())
    out = ["# Keyword plan (Tucson Pool Cleaning Pro, Oct 20 2026)", "",
           "Source: keywords/Tucson-Pool-Keywords.xlsx (Ubersuggest, United States, pulled Oct 20 2026), ALL tab,",
           f"{len(seen)} unique keywords. Generated by `python3 scripts/keyword_plan.py`; every keyword is either assigned to",
           "one page (as its TARGET or a supporting keyword) or listed as deliberately unused with a reason.", "",
           "Rules applied:",
           "- \"Near me\" terms and terms with no place name (\"pool service cost\", \"pool maintenance schedule\") carry",
           "  national volume. They are supporting keywords and are never read as proof of Tucson demand. The exceptions",
           "  are the two question guides CLAUDE.md names (\"my pool is green what do i do\", \"pool pump stopped working\")",
           "  and the maintenance schedule guide, whose national question rows are their targets, written for Tucson.",
           "- Town pages: Maurice's rule is that any town with 10 or more searches a month gets its own page. Oro Valley",
           "  (\"pool cleaning oro valley\" 90), Catalina Foothills (\"pool cleaning catalina foothills\" 10, \"pool service",
           "  catalina foothills\" 10), Green Valley (\"pool service green valley az\" 20; the hours and prices rows are",
           "  public-pool searches), Vail (\"pool service vail az\" 20) and Sahuarita (\"pool service sahuarita az\" 10).",
           "  Marana (\"pool cleaning marana\" 0) gets no page and folds into the Tucson pages.",
           "- Public-pool searches, company and brand names, parts shopping, jobs and places outside the Tucson metro",
           "  are unused.",
           "- Volume / SD = monthly searches / Ubersuggest SEO difficulty. Type is the row type in the seed tabs.", "",
           f"Assigned: {n_as}. Unused: {len(unused)}.", "", "## Assigned keywords by page", ""]
    for url in PAGES.values():
        if url not in assigned:
            continue
        out += [f"### {url}", "", "| Keyword | Volume | SD | Type | Role |", "|---|---:|---:|---|---|"]
        for kw, vol, sd, typ, role in sorted(assigned[url], key=lambda r: (r[4] != "TARGET", -(r[1] or 0), r[0])):
            out.append(f"| {kw} | {vol:,} | {sd} | {typ} | {role} |")
        out.append("")
    out += ["### /pool-light-repair/", "",
            "Target \"pool light repair tucson\" is not a row in the file; the page is justified by \"pool lights repair near",
            "me\" (590 a month nationally, SD 9), listed above under this page as supporting.", ""]
    out += ["## Deliberately unused", "", "| Keyword | Volume | SD | Type | Reason |", "|---|---:|---:|---|---|"]
    for kw, vol, sd, typ, why in sorted(unused, key=lambda r: (r[4], -(r[1] or 0), r[0])):
        out.append(f"| {kw} | {vol:,} | {sd} | {typ} | {why} |")
    (ROOT / "docs" / "keyword-plan.md").write_text("\n".join(out) + "\n")
    for url in PAGES.values():
        if url in assigned:
            t = [r[0] for r in assigned[url] if r[4] == "TARGET"]
            print(f"{url:40s} {len(assigned[url]):3d} kws  target={', '.join(t) or 'NONE'}")
    print(f"assigned {n_as}, unused {len(unused)}, total {len(seen)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
