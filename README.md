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
| **Quizzes** | First-attempt scores read automatically from each quiz file (`First attempt: 9/10`), grouped by topic, with averages, the weakest topic and corrected questions. Quizzes without a score line can be scored by hand. |
| **Roadmap** | Numbered roadmap steps by track (DSA, Foundations, Math, Courses…) with phase, difficulty and links. A "Next up" banner, plus **suggestions from my repos**: steps that have notes on GitHub but are still marked *todo*. |
| **LeetCode** | Every solved problem with difficulty, pattern, key insight and a link to my solution. A ✓ marks it revised in the current revision round, and filters show not revised, revisit and mistakes. |
| **Sessions** | Logged study sessions (from the focus timer or added by hand). |

**Adding a weekly plan:** open the week's page in Notion, press Ctrl+A then Ctrl+C, and paste it into **+ Add weekly plan**. The formatted page (headings, numbered lists, the day-by-day table) is converted automatically, and plain-text pastes work too.

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
- **Keyboard shortcuts**: 1–9 switch sections, `[` collapses or expands the sidebar
- **Collapsible sidebar**: shrink it to an icon strip (the choice is remembered) to give the 3-column Notes view more room
- **Mobile friendly**: a top bar with a ☰ menu drawer; on phones, Notes shows the list *or* the open note (with a Back button), and stat cards and tabs resize to fit

---

## Data & privacy
- Data is saved in the browser (`localStorage`). Optional **cloud sync** saves it to a *private* GitHub Gist, so another browser can restore it from the lock screen.
- **Export / Import JSON** in Settings: a full backup (replaces everything) or a Notion import file (merges roadmap, weekly plans, notes and LeetCode, and never duplicates).
- **Owner-only lock:** only the owner's passphrase opens the app, in any browser, and visitors can't create their own. The code holds only a salted PBKDF2-SHA256 hash (600,000 rounds), never the passphrase. To set or change it, run `python3 tools/set_owner.py` and push.
- The code is public, so the lock keeps people out of the interface but doesn't encrypt anything. That's fine because no personal data is in the code: it lives in the owner's browser and private Gist.
- Personal data never goes in this repo; it only holds the app's code.

---

## Upcoming features
- **Automatic Sunday plan:** the Sunday planner also saves each new plan to a private GitHub repo, and OPU/OS loads it automatically, with no copy-paste.
- **Sync back to Notion:** today data only flows *into* OPU/OS. Roadmap status changes and LeetCode revisions made here don't reach Notion, so the Sunday planner can't see them yet. Planned options:
  1. a weekly "sync to Notion" step done with Claude, or
  2. full two-way sync through a small serverless proxy (for example, a Cloudflare Worker) that holds the Notion key safely.

Until then, roadmap statuses are updated in Notion, and OPU/OS is used for everything else.

---

## Run it
Open `index.html` in a browser. That's it. To host it, push to GitHub Pages; the `CNAME` file sets the custom domain.
