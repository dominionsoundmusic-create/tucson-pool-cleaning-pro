# Brief for independent fact-checkers (Oct 20 2026)

You did not write the pages you check. Repo: /home/user/tucson-pool-cleaning-pro (branch build). Read
CLAUDE.md, INTAKE.md and docs/WRITING-GUIDE.md first (rules: no em/en dashes, no banned phrases, only
Tucson-metro places, never imply the line does pool work, no invented facts, no prices as the line's).

For each page in your group (src/pages/<file>.html):
1. List every factual claim that is not common knowledge or business fact from INTAKE.md: numbers, dates,
   rules, phone numbers, fees, providers, programs, statutes, history, population, neighborhoods, prices,
   and every source in the page's sources list.
2. Verify each with WebSearch (mode "standard"; restrict allowed_domains to the official or named source
   domain). WebFetch and curl cannot reach most hosts; a search result summary of the cited page is
   acceptable evidence. docs/research/*.md holds facts already verified this way, with URLs: you may rely
   on them but still check that the page states them correctly. Check that each cited URL plausibly holds
   the claim (domain and topic match).
3. Fix the page in place: CORRECT a wrong fact, SOFTEN a claim the evidence only partly supports, REMOVE a
   claim you cannot confirm (and its source if nothing else uses it). Rewrite in your own words; keep the
   page's structure, FAQs (3 to 6), images and macros. Never add an unsourced fact.
4. Search budget: stay within the cap in your task prompt. Verify the riskiest claims first (numbers, rules,
   phone numbers, prices, legal claims, local history). If the budget runs out, REMOVE or SOFTEN what you
   could not confirm rather than leaving it, and say so.
5. Validate: `python3 build.py --out /tmp/claude-0/<you>/dist`, then
   `python3 scripts/check.py --dist /tmp/claude-0/<you>/dist --skip-links --only <url>` for each page
   (0 errors) and `python3 scripts/similarity.py --dist /tmp/claude-0/<you>/dist --other
   /home/user/dominionsoundmusic-create/phoenix-pool-cleaning-pro/dist --only <url as similarity prints it>`
   (no FAIL). Never run plain `python3 build.py`. Do not commit. Do not edit other pages or shared files.
6. Write docs/fact-check/<you>.md: a per-page table | Claim | Source checked | Verdict
   (confirmed/corrected/softened/removed) | Note |, then totals per page (claims checked, confirmed,
   corrected, softened, removed) and the number of searches you used. Report the totals back.
