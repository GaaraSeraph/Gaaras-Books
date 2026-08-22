# Project: Isekai novel (untitled)

An isekai novel in English. Working discussion with the author happens in German.
The prose is always English.

The chapter files are canon. Everything else (docs/, this file) describes them or
plans ahead. Where a planning document contradicts a chapter, the chapter is right
and the document gets changed. How many chapters exist: see HANDBUCH.md.

## Read first

- `docs/story-bible.md` - all established canon: protagonist, system rules, world, cast, open threads. Check it before writing anything, and update it after every new chapter.
- `docs/character-arc.md` - the long arc, the progression tracker, pacing rules, and the things that must not drift.

## Leading documents - one source each

Each topic has exactly one authoritative file. Collect it there, link from
elsewhere, never copy. A second hand-maintained copy always drifts.

| Topic | Leading file |
|---|---|
| Formatting, file naming, versioning, workflow | `CLAUDE.md` (this file) |
| Status window: format + values per chapter | `docs/character-arc.md`, section 4 |
| The long arc, pacing, what must not drift | `docs/character-arc.md` |
| Cast: characters, levels, quotes | `docs/cast.md` |
| System rules, world, protagonist, threads | `docs/story-bible.md` |
| Decisions and what was discarded, with reasons | `docs/decisions.md` |
| Reading/paste versions (generated, never edit) | `book.md`, `HANDBUCH.md`, `MANIFEST.txt`, `chapters/*.txt` |

## Hard formatting rules

These are not preferences. The author's writing app renders markdown as literal characters.

- NO markdown inside chapter prose. No asterisks, no hashes, no underscores, no horizontal rules.
- NO em dashes anywhere, ever. Plain hyphens only.
- NO chapter title inside the chapter file text. The `.md` copy carries an H1; the `.txt` does not.
- System output is written in plain brackets on its own lines, e.g. `[ LEVEL UP ]`, `[ TRANSLATION ACTIVE ]`, `[ STATUS ]`.
- Emphasis comes from sentence structure, never from italics.

## Deliverables

Every chapter ships as BOTH `.txt` and `.md`, same content, only the `.md` has the title heading.
File naming: `chapters/chNN-slug.txt` and `chapters/chNN-slug.md`.
Versioning is handled by git now, not by filename suffixes.

## Length

Target under 2500 words per chapter. Chapters 5 and 6 run shorter and that is fine.

## Voice

- Close third person, past tense. Short paragraphs. Sentence fragments are normal.
- Concrete sensory detail over abstraction. Show the body, the smell, the weight.
- The humour is dry, sarcastic, and often crude or suggestive. It belongs to Gaara.
  Other characters mostly speak plainly. If everyone is witty, nobody is.
- At most one corporate or workplace joke per chapter. Corporate metaphors in the
  narration are banned outright; his old life shows up as concrete memory, not as simile.
- He is analytical and blunt. He reads people well. What he lacks is the cultural
  dictionary of this world, never the skill itself.

## Workflow with the author

1. Discuss what happens in the next chapter before writing it. He decides forks.
2. Write the chapter, then reread it for logic and continuity against the bible
   before presenting it. Repeat until two consecutive passes find nothing.
3. Present both files, then summarise what changed and why, in German.
4. Update `docs/story-bible.md` and the progression tracker in `docs/character-arc.md`.

## System rules, and making the story stick to them

Established system and world rules live in ONE place: `docs/story-bible.md`
section 2 (the system) and section 3 (the world). When the story establishes a
new rule, write it there and note the chapter it was established in, so a later
chapter can be held to it. This is the thing that most often goes wrong in this
genre: a rule is found, then quietly ignored.

Enforcement, in layers:
- Mechanical (`check.py`): attributes are only STR/DEX/CON/INT/WIS; the
  canon-number watchlist (forty houses, thirty-nine companies, eleven coins,
  Marit at 6); and the status/skill progression is reconstructed from the chapter
  blocks and flagged if any value regresses or a skill drops rank. Run
  `python3 check.py` to see the full status/skill history per chapter.
- Semantic (a standing agent pass before a release, because a regex cannot judge
  it). Prompt: "Read docs/story-bible.md sections 2 and 3 as the rulebook, then
  read every chapter in order. List every place where an established rule is later
  broken or quietly ignored. Quote the rule with its location and the breaking
  line with its location. Read-only, do not change anything." That catches the
  class the author cares about most.

## Continuity traps that have already bitten

- Charisma was removed from the stat block. Attributes are STR, DEX, CON, INT, WIS only.
- 10 is NOT the human average on the attribute scale. See the bible.
- He was barefoot until chapter 3. No boots before that.
- Technology stays medieval permanently. No concrete, no rebar, no machinery.
  Iron pins, lime mortar, rope and hands. The flavour is science plus magic.
- He did not die. There was no accident. He went to sleep and woke up here.
- Oldstep has forty houses, so roughly 150 to 200 people. Crowd sizes must match that.

## Build und Pruefung (Repo-Automatik)

Dieses Buch liegt im Repo `Gaaras-Books` und teilt sich dessen Automatik.

- **Kanon sind die `.md` in `chapters/`.** Die `.txt` daneben, `book.md`,
  `HANDBUCH.md` und `MANIFEST.txt` sind **erzeugt** und werden nie von Hand
  bearbeitet. Nach einer Aenderung: `python3 build.py`.
- `build.py` erzeugt die `.txt` (Prosa ohne Titelzeile) aus der `.md`, dazu
  `book.md`, `HANDBUCH.md` (aus `docs/`) und `MANIFEST.txt`. So laufen `.md` und
  `.txt` nie auseinander.
- `python3 check.py chapters/chNN-...` prueft mechanisch: keine Gedankenstriche,
  kein Markdown im Prosatext, Bandwurmsaetze (> 40 Woerter), DiGiorno "not X, but Y",
  "would rather", Fragezeichen-Verdacht, Wortzahl. Dass Gaara nie luegt und die
  Nachvollziehbarkeit der Inhalte sind menschliche Pruefpunkte, nicht mechanisch.
- Beim Commit laufen Build und Pruefung automatisch (Git-Hook). Die **Sperrklinke**
  (`.check-baseline`, `git config hooks.ratchet true`) blockiert nur, wenn ein
  Kapitel mehr Fehler bekommt als bisher geduldet. Eine GitHub Action baut bei
  jedem Push nochmal (Netz fuer Handy-/Web-Edits).
