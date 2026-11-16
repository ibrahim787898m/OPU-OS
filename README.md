# OPU/OS — Command Center

A personal dashboard for my CS self-study: weekly plans, roadmap, course notes, quiz scores, LeetCode revision, spaced review, journal, projects and job hunt, all in one place.

It's one `index.html` file with no build step, no framework and no server, hosted on GitHub Pages at **app.ibrahimmustafaopu.com**.

> **A vibe-coding project built with Claude.** This is a demo of what I can build with AI. I came up with the ideas, described the features and tested the results; Claude wrote the code (Claude chat for the first version, Claude Code for everything after). I didn't hand-write the code here. My own hand-written work is in my learning repos ([math](https://github.com/ibrahim787898m/math), [dsa](https://github.com/ibrahim787898m/dsa), [cs50x](https://github.com/ibrahim787898m/cs50x)).

---

## Features

### Dashboard
- Greeting, today's date and what I'm currently working on (or the next roadmap step)
- **Today card**: today's line from the weekly plan, with a checkbox, plus how many reviews are due
- Stats: study hours this week vs. goal, study streak, LeetCode solved and revised, active job applications
- 30-week study heatmap and a last-7-days bar chart
- Roadmap progress by track, GitHub activity, projects and website status

### Study
| Tab | What it does |
| --- | --- |
| **This week** | The Sunday weekly plan as a checklist: day-by-day tasks (today highlighted), must-do outcomes, "watch out" notes and an end-of-week review that can be saved to the journal. A summary strip shows study time, days done, LeetCode revised and reviews done. Past weeks stay in a history menu. |
| **Review** | Spaced repetition. Corrected quiz questions and LeetCode mistakes come back after 1 → 3 → 7 → 14 → 30 → 60 days. *Got it* / *Again* / *Retire*, a daily limit for new items, and my own review items. |
| **Quizzes** | First-attempt scores read automatically from each quiz file (`First attempt: 9/10`), shown as **collapsible topic rows** with average, a mini trend of each quiz's score, and badges (unfinished, to review). Filter by subject, sort by course order or weakest first, and expand or collapse all. Topics with an unfinished quiz open by themselves. Quizzes without a score line can be scored by hand. |
| **Roadmap** | Numbered roadmap steps by track (DSA, Foundations, Math, Courses…) with phase, difficulty and links. A "Next up" banner, plus **suggestions from my repos**: steps that have notes on GitHub but are still marked *todo*. |
| **LeetCode** | Every solved problem with difficulty, pattern, key insight and a link to my solution, grouped into **collapsible rows by pattern** (with revised x/y, mistakes, revisit). A search box finds any problem instantly. A ✓ marks it revised in the current revision round, and filters show not revised, revisit and mistakes. |
| **Sessions** | Logged study sessions (from the focus timer or added by hand), grouped into **collapsible weeks** with total time, problems and a Mon–Sun mini chart. This week opens by itself, older weeks load 8 at a time, and track chips filter by subject. |

**Weekly plans arrive automatically:** a small GitHub Action in a separate private repo copies the latest Notion "Week of …" pages into a secret Gist every 30 minutes. OPU/OS picks them up when it opens. New weeks are added, and mid-week edits update the plan while keeping ticks and review answers. Pasting still works as a fallback (**+ Add weekly plan**: open the page in Notion, press Ctrl+A then Ctrl+C, then paste).

### Notes & Journal
- **Course notes are read live from GitHub** (my `math`, `dsa` and `cs50x` repos). Each file is sorted by its folder path:
  `dsa/python/10_linked_list/quiz/lesson_3.md` → **DSA · Linked List · quiz**
- One finder panel: search, **Subject → Topic dropdowns**, type chips (lesson, quiz, practice, review, reflection, problems, rough, extra, note), GitHub / Mine, sort by topic or recent, and full-text search
- The note gets the rest of the width, and **Focus mode** (button or `\`) hides the panel for full-width reading
- **Code tab**: my code from GitHub (CS50P problem sets, LeetCode solutions, DSA and math programs) in a read-only viewer with syntax colours, line numbers and Copy. It has the same finder panel (repo → folder dropdowns, language chips, search inside code) and a **My code** strip with files and lines of code per language and repo. cs50x code is deliberately not published.
- Notes and code are linked: a note shows "Code in this topic", a code file shows "Notes for this topic", and LeetCode "my solution" opens inside the app
- My own notes in Markdown, with subject, topic, type, tags and pinning
- Markdown rendering with tables, code blocks, task lists, quotes and numbered lists
- **Journal**: daily entries with a mood picker, grouped by month, and a weekly-review template that fills in the week's numbers

### Everything else
- **Ctrl+K command palette**: jump anywhere, run actions, and search *inside* every note
- **Focus timer** (25 / 50 / 90 min) that logs a study session when it ends
- **Skills, Projects, Career** (job pipeline board with follow-up reminders), **GitHub** stats and **Presence** links
- **Long lists stay short**: Review shows 10 at a time, Notes/Code/Journal lists load 30 at a time, the Roadmap folds finished steps, and each Career column shows its 6 latest cards (with "show more" everywhere).
- **Keyboard shortcuts**: 1–9 switch sections, `[` collapses or expands the sidebar
- **Collapsible sidebar**: shrink it to an icon strip (the choice is remembered) to give the 3-column Notes view more room
- **Mobile friendly**: a top bar with a ☰ menu drawer; on phones, Notes shows the list *or* the open note (with a Back button), and stat cards and tabs resize to fit

---

## Data & privacy
- Data is saved in the browser (`localStorage`). Optional **cloud sync** saves it to a *secret* GitHub Gist, so another browser can restore it from the lock screen. A secret Gist is **unlisted, not private**: it doesn't appear on the profile or in search, but anyone with its exact link could open it, and the data isn't encrypted. The link has a long random ID, so it can't realistically be guessed. Just never share it.
- **Storage safety:** the app asks the browser to keep its data (persistent storage), shows data size and last sync/backup in Settings, and reminds you to export a backup every 14 days.
- **Export / Import JSON** in Settings: a full backup (replaces everything) or a Notion import file (merges roadmap, weekly plans, notes and LeetCode, and never duplicates).
- **Owner-only lock:** only the owner's passphrase opens the app, in any browser, and visitors can't create their own. The code holds only a salted PBKDF2-SHA256 hash (600,000 rounds), never the passphrase. To set or change it, run `python3 tools/set_owner.py` and push.
- The code is public, so the lock keeps people out of the interface but doesn't encrypt anything. That's fine because no personal data is in the code: it lives in the owner's browser and secret (unlisted) Gist.
- Personal data never goes in this repo; it only holds the app's code.

---

## Upcoming features
- **Two-way Notion sync (in progress):** browsers can't call Notion directly, and the Notion key must never be in this public code, so a small private Cloudflare Worker holds the key. It can read and update five databases (job applications, roadmap, tasks, LeetCode problems, projects), create new jobs and projects, and never delete anything. Each device connects once in **Settings → Notion sync** (Worker address + sync key, stored only in that browser).
  - Done: the Worker and the Settings connection with a per-database health check.
  - Done: **Career ⇄ Notion job applications.** Jobs found by the daily job-search chat appear on the board with a **NEW** badge, plus why each one fits, its location, pay, type, which résumé to use and links to the posting and the Notion page. Moving a card, editing it or adding a job updates Notion within seconds, and changes made in Notion show up when the app opens or the tab is reopened. Jobs typed into the app before sync are matched by company and role (never duplicated). Skipped jobs are hidden. Deleting a Notion job in the app marks it Skipped there; nothing is ever deleted in Notion. Offline changes wait (⏳) and go out later.
  - Done: **Roadmap ⇄ Notion.** Cycling a step's status (todo → doing → done) or editing its notes updates the Notion Roadmap, so the Sunday planner sees real progress. Status changes made in Notion show up here. Steps added in Notion appear automatically; steps deleted there leave the roadmap. Title, step number and track come from Notion. Steps created only in OPU/OS stay local.
  - Done: **Weekly-plan ticks ⇄ Notion Tasks.** Ticking a day marks that day's task (the one titled with the day, like "Mon 16 — …") Done in Notion, and unticking sets it back to To Do. Notion changes tick or untick the day here. Other tasks on the same date are never changed. Days already ticked before sync were sent to Notion on the first sync.
  - Next: LeetCode practice and projects.
  - Conflicts are decided field by field: if only one side changed a field, that change wins; if both did, the newer edit wins and the app tells you.

---

## Run it
Open `index.html` in a browser. That's it. To host it, push to GitHub Pages; the `CNAME` file sets the custom domain.
