# Project: Transmigration into Freedom (working title)

An isekai novel in English. Working discussion with the author happens in German.
The prose is always English.

The chapter files are canon. Everything else (docs/, this file) describes them or
plans ahead. Where a planning document contradicts a chapter, the chapter is right
and the document gets changed. How many chapters exist: see HANDBUCH.md.

## Before anything else: THE JOKES ARE NOT A POLISH PASS

The author has had to ask for this SIX TIMES and that is six times too many. It
is not a note to apply at the end. It is part of drafting, and if it is missing
the draft is not finished, in the same way a chapter with a forty-word sentence
is not finished.

THE COUNTABLE RULE: EVERY SCENE WITH ANOTHER PERSON IN IT NEEDS AT LEAST ONE
LINE THAT IS THERE ONLY TO BE FUNNY. Not a line that is witty while doing work.
A line that would be cut by anybody optimising the scene for information, and
which is the reason the scene is worth reading.

AND THE DRIFT ALWAYS LOOKS THE SAME, so it is recognisable: it happens when he
is WORKING. Negotiating, teaching, reading a room, doing arithmetic. The talk
stays but goes functional, and a competent operator comes out instead of him.
It is the same failure as going solemn when somebody is hurt.

THIS CANNOT BE CHECKED BY MACHINE AND check.py DOES NOT TRY. Dialogue density
was measured across all chapters and it does not catch it: the two chapters the
author complained about scored 61 per cent, third and fourth highest in the
book. He was talking constantly and none of it was funny. A metric that cannot
tell those apart is a metric that lies, and a check that lies is worse than no
check (see the Erdkalender entry in docs/decisions.md).
So it lives here instead, at the top, where it is read before writing.

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
- NO DiGiorno punchlines. The author does not want them. The banned shape is a
  short negated sentence immediately refilled by a short positive one, used as a
  reveal: "This is not a stream. This is a floor." "It was not hunting. It was
  leaving." "It is not counting corpses. It is weighing them." Eighteen of these
  had accumulated across fourteen chapters before it was caught.
  This is NOT a ban on negation. "Not much, and never about herself." "The
  hatchet came down. Not away, just down." "Something colder than panic." All
  fine, all ordinary prose, all staying.
  check.py now flags the punchline shape specifically and fires on the first
  one, not the second.
- NO chapter title inside the chapter file text. The `.md` copy carries an H1; the `.txt` does not.
- System output is written in plain brackets on its own lines, e.g. `[ LEVEL UP ]`, `[ TRANSLATION ACTIVE ]`, `[ STATUS ]`.
- Emphasis comes from sentence structure, never from italics.

## Deliverables

Every chapter ships as BOTH `.txt` and `.md`, same content, only the `.md` has the title heading.
File naming: `chapters/chNN-slug.txt` and `chapters/chNN-slug.md`.
Versioning is handled by git now, not by filename suffixes.

## No preparation chapters

NO CHAPTER MAY EXIST TO SET UP A LATER ONE. Every chapter needs its own event
with a consequence that cannot be taken back by the next page.

The test, and it is one sentence long: write the chapter's summary. If it comes
out as "they decided", "they planned", "they agreed", "they gathered",
"they got ready" or "they talked about it", the chapter is broken. Deciding is
not an event. Recruiting is not an event. Packing, briefing, arguing about a
plan and agreeing on a signal are not events.

Preparation is allowed as a PAGE, never as a chapter. Compress it and set it
against something happening.

Caught by the author three times: the first Chapter 6 (a night in a byre with
four witnesses), the first Chapter 9 (a walk through a room and back out), and
Chapter 14 (asking a village for six men). Two of the three were rewritten from
nothing. This is the most expensive recurring mistake in the project, and it
always arrives disguised as good structure, because the arc document genuinely
does call for organising, deciding and preparing. It calls for them as THINGS
THAT HAPPEN INSIDE CHAPTERS, not as chapters.

The repair, when a chapter turns out to be preparation, is not to add action for
its own sake. It is to find the irreversible thing the preparation would
actually cause and put it on the page. Chapter 14 was fixed by asking what
telling forty houses the truth would really do, and the answer was that a man
gets on a horse and rides east.

## Length

Target under 2500 words per chapter. Several run shorter and that is fine.
A chapter with a crowd in it costs words: villagers talk over each other, ask
the same question twice and say unhelpful things, because that is what people
do. If dialogue pushes a chapter over the target, look for the seam and split
it rather than cutting the talk. That is how 6 became 6 and 7.

## Voice

- Close third person, past tense. Short paragraphs. Sentence fragments are normal.
- Concrete sensory detail over abstraction. Show the body, the smell, the weight.
- The humour is dry, sarcastic, and often crude or suggestive. It belongs to Gaara.
- VOLUME IS NOT THE TEST. He can talk through an entire chapter and it can still
  be wrong, because the failure mode is not silence, it is GRAVITY. Operational
  speech does not count: plans, orders, arithmetic and hard truths are not his
  voice, they are his job.
  FLOOR, every chapter: at least two lines from him that are dry, crude,
  suggestive or all three, and at least one of them landing where it is least
  appropriate. A chapter with none is broken even if he never stops talking.
  And check the DISTRIBUTION, not just the count. Chapter 14 cleared the floor
  eight times over and was still wrong, because every one of them sat in the
  first half and the whole back end went solemn the moment somebody confessed
  something. Somebody else's guilt is not a reason for him to go quiet.
  Caught by the author twice (ch8 and ch14) and never once by a script, because
  no script can measure it. Read for it deliberately, before anything else.
- HE FLIRTS WITH EVERYONE AND PROPOSITIONS ALMOST NOBODY. The suggestive line is
  free, general and constant: it goes to the room, to men he finds ridiculous, to
  people pointing weapons at him. An actual offer is rare, specific, and goes
  only to somebody he genuinely wants. Do not let the two merge. A man who offers
  to everybody present is running a policy, and it stops being attraction.
- HE DOES NOT EXPLAIN HIMSELF. No speeches about his own decency, no stating the
  terms of anything he is doing. Where a safeguard matters, it has to be visible
  in the BEHAVIOUR: he asks once, takes the answer in the same breath, and
  changes the subject. The moment he narrates his own scruples he is writing a
  memo about himself, which is the exact man he left behind.
- HE DOES NOT SHUT UP. This is the single thing that drifts fastest. He talks at
  monsters mid-fight, needles people who are pointing weapons at him, and makes
  the joke nobody wanted. Calibrate against chapter 2, where he is alone in a
  dead room with two things trying to kill him and still will not stop talking.
  If a scene has him observing quietly for a page, the scene is wrong.
- His silence is therefore an EVENT and has to be paid for. When it happens,
  give the reader a reason and let another character notice it (ch6, ch7).
- Other characters mostly speak plainly, and plainly does NOT mean tersely.
  Villagers repeat themselves, ask the same question twice, and say unhelpful
  things. Clipped dialogue is a stylised register; if everyone has it, everyone
  sounds like Gaara and nobody sounds like themselves.
- Corporate or workplace jokes in his mouth: one or two per chapter is the normal
  dose, four is the ceiling. Corporate metaphors in the NARRATION are still banned
  outright; his old life shows up as concrete memory, not as simile.
- He is analytical and blunt. He reads people well. What he lacks is the cultural
  dictionary of this world, never the skill itself.
- He never says anything untrue. He omits, deflects and stays silent instead, and
  the evasions are built so they hold up word by word. Jokes and exaggeration are
  exempt. The reasoning is in the bible, section 1, and it is his own.

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
- Technology seen so far is medieval: iron pins, lime mortar, rope and hands, no
  machinery. That is the baseline, not a hard permanent law. How far tech goes and
  how it mixes with magic is OPEN and gets discovered in-story (bible section 7).
  Guardrail: no casual industrial anachronism; advanced tech or printing, if it
  comes, comes deliberately and on the page as hand-tools plus magic.
- He did not die. There was no accident. He went to sleep and woke up here.
- Oldstep has forty houses, so roughly 150 to 200 people. Crowd sizes must match that.
- The village sits on the south leg of the channel (ch8). They do not know it.
  Anything that reaches Oldstep from now on can arrive from underneath.
- Gaara is a name he chose for himself in the old world and that stuck as a
  nickname. The system did not give it to him, it read it off him, and it was
  never on any document. Here it is simply his name.
- His old working life is 19 years long. Not fifteen, not sixteen. Both drifted in
  once and had to be pulled back out of four chapters.
- The level in chapter 2 raised STR and DEX only. CON is 5 until he spends the
  three free points on it in chapter 3. An [ ATTRIBUTES UPDATED ] block that reads
  "X: a to b" must start at the value the previous chapter ended on; check.py now
  says so out loud.
- THE CLOCK IS TWO WEEKS, NOT FOUR. Ch14 gives four days (two east, two back)
  and ch17 corrects it on the page: that is walking time and nothing happens at
  the floor. Do not write a chapter that assumes riders on day four.
- Everything after chapter 1 happens on ONE day, up to and including the night in
  the byre. He walks into the ruin on the morning of day two.

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
