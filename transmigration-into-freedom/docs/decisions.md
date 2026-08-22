DECISIONS AND WHAT WAS DISCARDED
Each entry says WHAT was decided and WHY, so a later pass does not undo it by
accident. Newest on top.


=== Where the name comes from, and where that gets spent ===
Origin settled: he took the name at nineteen from a story he had loved as a
boy, from a character who had been kept apart from everyone and concluded he
needed nobody. It is the central argument of this book worn as a name, chosen
before his life made it true and then lived into for nineteen years. That is
worth more than any explanation he could give a character, which is why he
never gives one.
The source work is NOT named on the page, ever. Discussed and rejected on three
grounds: it dates the book to a decade, it pulls a licensed property into
something meant for publication, and a reader who recognises it gets an in-joke
where the wound should be. The permitted vocabulary is "a story he read as a
boy". Whoever knows it will know it.
Placement chosen by the author out of three options: it lands the first time
somebody here writes the name down. Rejected were Marit using it casually about
him (too close to ch7, where she is already the cost) and the system naming him
a second time at a formal moment (right idea, but it must not arrive before
stage 3 of the arc has actually hurt). The written-down version wins because it
runs on machinery that is already standing - the elder's unanswered monthly
letter and the proof Gaara owes him - and because it collects thread 9 (reading
is untested) and thread 13 (he has not seen a book) in the same scene. Details
in thread 16.

=== The name Gaara is self-chosen, and the system read it off him ===
Decided by the author: Gaara is not a birth name. He took it for himself in the
old world, it established itself as what people called him, and it never
appeared on a document. The bible had claimed the opposite for six chapters -
"the name the system gave him" - which ch1 already contradicted: the panel has
it before he says anything, and he reads "his name, spelled correctly". Per the
canon hierarchy the text won and the line was rewritten.
What the decision buys, and why it is worth more than a tidy bible line: the
ch4 exchange gets sharper without a word being changed. "That's not a name" is
correct, he knows it is correct, and "It is now" is therefore a claim and not a
denial - which is also the only shape available to him, since he never says
anything untrue. And it leaves one unspent implication on the table: the panel
reported what he calls himself rather than what he was called, so the system
reads self-conception, not record. That is a different order of thing from
putting a number over a goat, and it belongs in a chapter, not in a doc.
Thread 16 was rewritten to hold the part that is still open.

=== Gaara never says anything untrue, and that is canon now ===
The author decided it: Gaara does not lie. He omits, deflects, answers a
narrower question and stays silent, but he never states a falsehood. The
reason was already on the page and only needed writing down (bible, section 1):
a lie needs a world behind it and he has none, so the truth is the only
version he will not have to remember. Two things were settled with it.
First, an exemption for irony, jokes and exaggeration, because without it
"I built a whole career on it" (ch2) becomes a lie and the rule eats his
humour. Second, the two "Nothing" answers in ch4 and ch5 were checked against
the rule and kept: in ch5 he has just looked at Hallvard and seen nothing at
all, so the evasion is literally true, and that is the model for how to write
the others.

=== The old working life is 19 years ===
It stood as sixteen in ch1, fifteen in ch4, ch5 and ch6, and "roughly 16" in
the bible. The author set it at nineteen: he is 38, he started at 19, and the
figure now says so in all five places. Nothing in the story hangs off the exact
number, but four chapters disagreeing about the same span is the drift the
canon-number watchlist exists to prevent, and this one slipped past it because
"years" has no distinctive subject to watch.

=== Workplace jokes go up to four, narration metaphors stay banned ===
The old rule was one corporate joke per chapter, which ch2 already broke twice
over. The author raised it: one or two per chapter is the normal dose, four is
the ceiling. The other half of the rule did NOT move - corporate metaphors in
the narration remain banned outright. Five had crept in ("bill him in days",
"walked a factory floor", "Assets:/Liabilities:", "a bad quarterly", "no
filing category") and were rewritten as concrete memory or plain description.
The split is the point: the jokes are HIS and they characterise him; the
metaphors are the narrator's and they make the book sound like a business book.

=== Level 2 raises only what he used ===
ch2's level-up block granted +1 CON, and ch3's [ ATTRIBUTES UPDATED ] then
computed from CON 5. Both cannot be true. Fixed at the ch2 end: the level
raises STR and DEX, the two he actually used, and leaves CON alone, plus 3 free
points. Chosen over correcting ch3 because ch3's whole decision scene leans on
the number five ("the number that had run his life"), and because it turns a
bookkeeping error into a system rule worth having: the system pays out on use,
not on need, which is exactly why he has to spend his own points on endurance.
check.py now verifies that an "X: a to b" block starts where the previous
chapter ended, so this class cannot recur silently.

=== World laws are discovered in-story, not pre-legislated ===
The bible had claimed a hard world law - "technology stays medieval, permanently,
no machinery" - that NO chapter established. The chapters only show a medieval
village and dead ruins (ch3); the "permanently / no machinery / science plus
magic" absolute came from the planning setup, not the text, and the author never
committed to it. Per the canon hierarchy the text wins, so the bible now
separates three things: canon (what Gaara has actually seen), the author's faint
leanings (clearly marked, e.g. "science plus magic"), and open questions to be
discovered in-story. Concretely OPEN and to be revealed on the page, not decided
in a doc: the true tech level and whether printing exists (section 7, thread 13),
and the nobility system and any noble-backer requirement (thread 14). Guardrails
keep early chapters from contradicting a future reveal (no casual industrial
anachronism; keep the lord's real power ambiguous). Why: the author wants to
discover this world, not read it off a rulebook.

=== Progression check stays a warning, never a hard gate ===
check.py reconstructs Level/HP/MP/attributes/skill-ranks across all chapters and
flags any value that regresses ("REGEL VERLETZT"). It PRINTS this; it never fails
the build or the ratchet. Reason: a valveless cross-chapter gate would block a
legitimate story beat (a curse, an injury, a system penalty, a class change that
reshuffles stats). The author chose warning-only on purpose. The full status/skill
history still prints on every run, so a real accidental regression is visible.

=== System and world rules are tagged with the chapter they were established in ===
story-bible.md sections 2 and 3 carry a (chN) tag on every rule. Reason: so a
later chapter can be held to the rule, and "a rule was found, then quietly
ignored" (the thing the author dislikes most in the genre) is traceable to where
it started. If a chapter ever contradicts a tagged rule, the chapter wins and the
line is re-tagged, per CLAUDE.md's canon hierarchy.

=== Canon-number watchlist in check.py ===
A short list of numbers with a fixed canon value and a distinctive subject:
forty houses, thirty-nine companies, eleven coins, Marit at Level 6. check.py
errors if the subject appears with a different number. It is a watchlist, not a
stoplist - it never counts bare numbers, so harmless numbers do not trip it, and
a legitimate other subject is booked with --baseline. Gaara's own level and
attributes are NOT on the list; they change and live in character-arc.md section 4.

=== Cast has one source ===
The cast lived in both cast.md and the story bible's section 4, word for word.
cast.md is now the leading document; the bible keeps a short index and points to
it. Two copies of the same character notes drift.

=== Status window has one source ===
The running status window (its format and its per-chapter values) lives only in
character-arc.md, section 4. The story bible used to carry a second "Current
sheet"; two hand-maintained copies drift - the bible's was already stamped "end
of Chapter 4" while six chapters existed, and it omitted the Race field that the
chapters actually render. The bible now points to the tracker.

=== Versioning is git, not filename suffixes ===
Chapter files are named chNN-slug (no vN suffix); versioning is git's job. The
story bible briefly said "chNN-slug-vN", which contradicted CLAUDE.md. CLAUDE.md
is the leading document for formatting and naming; the bible now defers to it.

=== Attributes are STR, DEX, CON, INT, WIS only ===
No charisma, luck or appearance stat. Gaara notices the absence and approves it.
check.py errors on CHA/Charisma/LUK/LUCK/Luck/APP/Appearance, so a relapse cannot
slip in unnoticed, including inside a [ STATUS ] block. Baseline was 0.

=== Hand-maintained counts moved to the build ===
"N chapters written" / "last updated" stamps drift. HANDBUCH.md now carries the
chapter count from the build. "35 planned" stays in the bible, because the build
cannot know it.
