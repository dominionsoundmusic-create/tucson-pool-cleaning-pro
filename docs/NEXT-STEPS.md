# Next steps for Tucson Pool Cleaning Pro (Oct 20 2026)

The rebuilt site is finished on the `build` branch. Nothing is live yet. Here is everything left, in order.
For each step, reply in the chat with your answer and Claude does the rest.

## 1. Two questions: answered

Calls: the "may record or log" wording stays as is. Terms: governed by Texas law. Both are done.

## 2. Look at the site before it goes live (reply "open the pull request")

Claude opens a pull request from `build` to `main` on GitHub. Netlify normally builds a private preview
link for it, so you can click through every page on your phone without touching the live site.
Opening the pull request does not publish anything.

## 3. Photos (optional, can wait until after launch)

34 new photos would make the pages better. Every page already shows an existing photo until its new one
arrives, so nothing looks broken without them.

1. Open `docs/image-list.md` (attached). Each entry has a file name, a size and an Artistly prompt.
2. Paste each prompt into Artistly and generate the image at the size listed.
3. Send the images back to Claude in the chat, named as in the list. Claude puts them in place, rebuilds
   the site and pushes it.

Suggested order: the 1920x1080 hero photos first. They show at the top of each page.

## 4. Go live (you click one button)

When you are happy with the preview, open the pull request on GitHub and press "Merge pull request".
Netlify then publishes the new site at tucsonpoolcleaningpro.com. Claude is not allowed to do this step;
it is your decision.

## 5. After launch, check five things (about five minutes)

- Visit https://tucsonpoolcleaningpro.com/made-up-page and see the "page is not here" page.
- Visit https://tucsonpoolcleaningpro.com/blog and see it land on the home page.
- Tap "ES" in the menu bar and see the page switch to Spanish.
- In Google Analytics, see today's visits show up.
- Call (520) 372-1083 and make sure it reaches the line as before.

If anything looks wrong, tell Claude what you saw.
