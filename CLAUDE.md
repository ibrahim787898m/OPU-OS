# CLAUDE.md — OPU/OS

This repo is an **AI-built showcase app**, not a learning repo. Here, Claude writes and edits the code directly. This overrides the "hints, never solutions" rule in `~/code/CLAUDE.md`, but only for this repo. The owner still runs git himself: suggest commit messages, don't commit.

## What it is
- One file: `index.html` (HTML + CSS + vanilla JS, no build step). Hosted on GitHub Pages (`CNAME`).
- `README.md` is the public description; keep it updated when features change.
- `OPUOS_GUIDE.txt` (git-ignored) is the owner's private, detailed guide. Read it for how features work, the data flows and the Notion structure, and update it when behaviour changes.
- `tools/set_owner.py` writes the owner-passphrase hash into `index.html`.

## Hard rules
- **The repo is public.** Never commit personal data, tokens, passphrases, Notion content or import/backup JSON. Import files go to `~/Downloads`, not the repo.
- **Never handle the passphrase.** The owner runs `tools/set_owner.py` in his own terminal. Don't change the `OWNER` line or ask for the passphrase.
- **Keep saved data compatible.** New fields go through `migrate()`; never wipe or reshape `localStorage['opuos.v1']` destructively.
- Course notes and code are read **live and read-only** from public repos (Settings → note repos / code repos). Don't copy them into the app. **cs50x code stays out** (academic honesty), so don't add a way to show it.
- Data flows into OPU/OS only (GitHub live, Notion by paste/import). Nothing writes back to Notion or GitHub.
- **Icons:** use the SVG helper `I('name')` (the `ICONS` map at the top of the script), not rare Unicode symbols. Symbols like ⏻ ⌥ ⇤ are missing from phone fonts and show as "?". Plain arrows, ✓, ● and emoji are fine.
- **Sync:** never let background or cache updates call `save()` (use `save(true)`). Never push before the first `pullGist()` of a session. See the sync rules comment in the code.

## Code map (sections in index.html, in order)
seed → `migrate()` → Gist sync → lock (`OWNER`, PBKDF2) → router → Dashboard → Study (week plan parser, review queue, quizzes, roadmap suggestions, LeetCode) → GitHub notes (`ghMeta`, `loadGhNotes`; one tree fetch per repo feeds notes and code) → Code (`codeMeta`, `hl` highlighter, `lcCode`) → Notes & Journal (tabs Notes | Code | Journal) → Markdown renderer (`md`, `inl`: escape first) → Settings → forms → actions object `A` (`data-act` clicks) → timer → command palette.

## Testing (no Node here)
Test in headless Chrome (`google-chrome --headless=new`):
- Build a copy of `index.html` with a test harness that calls `enter()`, runs `mergeImport()` on sample data, opens every view and collects `window.onerror`. Read results with `--dump-dom --virtual-time-budget=…`.
- Take screenshots at desktop size and at 390×844 (phone).
- WebCrypto (PBKDF2) hangs under `--virtual-time-budget`. Test the lock in real time instead (have the page POST its results to a local receiver).
- Never test against the real repo file's `OWNER` hash. Use a copy with a throwaway passphrase.

## Weekly plans automation
The private repo `~/code/opuos-automation` (GitHub Action, `notion_to_gist.py`) writes the latest Notion plans into the secret Gist file `opuos-weekly-plans.json`. In the app, `checkAutoPlans()` and `mergeAutoPlans()` read it with the sync token (plans are matched by week, and `srcMd` detects changes).

## Pending (decided "later")
Sync back to Notion, optional Cloudflare Pages + Access, optional data encryption. Details are in `OPUOS_GUIDE.txt` section 12.
