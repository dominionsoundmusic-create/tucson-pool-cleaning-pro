# Independent fact-check (Oct 20 2026)

**What was run.** After all 28 pages were written, five separate fact-check sub-agents (fc1 to fc5) checked
the factual claims and cited sources on every page. None of them wrote any page it checked. Each followed
docs/fact-check/BRIEF.md: list every non-obvious claim (numbers, dates, rules, phone numbers, fees,
providers, programs, statutes, history, populations, prices), verify it, then correct, soften or remove it
in place, re-run build.py, check.py and similarity.py on its pages, and log every claim. Claim-by-claim
tables: docs/fact-check/fc1.md to fc5.md.

**Method limit (read this).** This environment's network policy blocks direct page fetches (WebFetch and
curl fail for tucsonaz.gov, pima.gov, roc.az.gov, weather.gov and nearly every other source). Claims were
verified against WebSearch result summaries of the named official or credible page, usually restricted to
that source's domain, not by opening the page. Each checker had a search budget of 12 to 20 searches; a few
low-risk claims kept without a fresh search are marked "not searched" in fc5.md. To re-verify by opening
every source, allow those domains in the environment's network settings and re-run the checkers.

| Checker | Pages | Claims checked | Confirmed | Corrected | Softened | Removed |
|---|---|---:|---:|---:|---:|---:|
| fc1 | /, /services/, /service-areas/, /how-it-works/, /about/, /faq/, /contact/, privacy, terms | 92 | 86 | 2 | 4 | 0 |
| fc2 | /pool-service/, /pool-cleaning-maintenance/, /pool-service-cost/, /pool-tile-cleaning/ | 66 | 51 | 0 | 10 | 5 |
| fc3 | /swimming-pool-repair/, /pool-leak-repair/, /pool-light-repair/, /pool-pump-repair/, /pool-pump-not-working/ | 65 | 57 | 2 | 6 | 0 |
| fc4 | /green-pool-cleanup/, /my-pool-is-green/, /tucson-pool-maintenance-schedule/, /draining-a-pool-in-tucson/ | 59 | 47 | 5 | 4 | 1 |
| fc5 | Oro Valley, Catalina Foothills, Vail, Sahuarita, Green Valley, plus the 5 town summaries in site.json | 75 | 61 | 5 | 6 | 3 |
| Lead | follow-up: the HomeAdvisor Tucson range left on /faq/ after fc2 removed it elsewhere | 1 | 0 | 0 | 0 | 1 |
| **Total** | 28 pages | **358** | **302** | **14** | **30** | **10** |

(Counts are as each checker reported them; fc4's per-page rows add to 57 decisions for 59 claims listed.)

**Most important fixes.**
- A HomeAdvisor "Tucson" price range ($92 to $288 per visit) and a Tucson repair average ($371) could not be
  found again on HomeAdvisor's pages; both were removed (cost guide, FAQ) or replaced with HomeAdvisor's
  national guide (pool repair page). Every price left on the site is a named publisher's national range with
  a "real quotes vary" note.
- A "within a minute or two" response-time line on the home page was removed (not in INTAKE.md).
- Oro Valley: the gate-swing rule was not in the town's code and was replaced with what the 2024 amendments
  say; an unconfirmed "all drain water must stay on site" line was removed.
- Catalina Foothills: an unconfirmed July 2022 Finger Rock Wash flood was removed; the Esperero culvert work
  now says construction began in January 2026 instead of "replaced".
- Vail: an unconfirmed county trail policy was removed; the site.json summary no longer says "mostly".
- The insurance FAQ on /swimming-pool-repair/ was narrowed to what the Arizona Department of Insurance and
  Financial Institutions says (normal wear and aging is generally not covered).
- Draining guide: the recycling-concentrate rule, a fiberglass and vinyl claim and a case-study paraphrase
  were corrected or softened to what the sources say.
- No page says or implies the line does pool work, checks licenses, or that any company is licensed,
  insured or rated; no company is named.

**Open items for Maurice (business decisions, not checkable facts).**
1. Privacy and contact pages say calls to the automated assistant "may be recorded or logged". Confirm
   whether calls are recorded and adjust the wording.
2. The terms say Arizona law governs them. Approve or change.
