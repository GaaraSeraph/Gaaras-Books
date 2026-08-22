DECISIONS AND WHAT WAS DISCARDED
Each entry says WHAT was decided and WHY, so a later pass does not undo it by
accident. Newest on top.


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
