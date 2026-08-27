# -*- coding: utf-8 -*-
import io
AUFTRAEGE=[]

E31 = []

E31.append((
u'*Lot Fourteen* · Version 2.6 · EN',
u'*Lot Fourteen* · Version 3.0 · EN'))

# Das Gespraech ueber den Brief hat den Brief viermal ausgelegt. Zweimal reicht.
E31.append((
u'"No. She told me I would keep it and not use it." He kept his hands at his sides. "I have thought about what using it would mean, and handing it to the man it is about is exactly that, whatever the reason I told myself for doing it."\n\n"Even the kind reason," said Annie.\n\n"Especially the kind reason. He asked for this because he wanted to be forgiven for something, and if I hand it to him, I am the one deciding that he has earned it, and that is not mine to decide. It was never going to be mine."\n\n---\n\nAnnie looked at the letter for a moment longer.\n\n"Then what was it for."\n\n"It exists," said Georgij. "That was the whole of what he asked for, and I did not understand it until this morning. He did not want it read by anybody in particular. He wanted it to be true and written down, in case the only version of the ninth of January that survives is the one in his own head, which he has already told me he does not trust."\n\n---\n\nAnnie sat back.\n\n"You could have told him that yourself and saved her the morning."\n\n"I could have," said Georgij, "and it would have been worth nothing, because it would have been my word about her instead of hers. A man who kept everything for twenty years believes paper. I gave him a piece of paper. I did not give him mine to give, and that is the difference between doing the thing correctly and doing it quickly."\n\n---\n\nAnnie looked at him for a moment the way she looks at a figure she has already checked twice and is checking a third time out of habit rather than doubt.\n\n"You have spent a great deal of this year learning the difference between those two," she said.\n\n"I have spent a great deal of this year learning that I did not use to know there was one."\n\n---\n\nSomething in Annie's face settled, the way it does when an answer has met whatever she was testing it against and held.\n\n"Read me the last line again," she said.\n\n"He was correct about the desk. He was wrong about the book. I am writing this so that somewhere it says which was which."\n\n"That is the entire dispute of this business in two sentences," said Annie, "and she wrote it before her coffee had gone cold, on her first morning at a job she has every reason to have spent thinking about something else."\n\n"Yes."',
u'"No. She told me I would keep it and not use it." He kept his hands at his sides. "Handing it to the man it is about is using it, whatever reason I tell myself for doing it. He asked for this because he wanted to be forgiven for something, and if I hand it to him, I am the one deciding that he has earned it."\n\n---\n\nAnnie looked at the letter for a moment longer.\n\n"Then what was it for."\n\n"It exists," said Georgij. "That was the whole of what he asked for, and I did not understand it until this morning. He wanted it to be true and written down, in case the only version of the ninth of January that survives is the one in his own head, which he has already told me he does not trust."\n\n---\n\nSomething in Annie's face settled, the way it does when an answer has met whatever she was testing it against and held.\n\n"He was correct about the desk. He was wrong about the book," said Annie. "That is the entire dispute of this business in two sentences, and she wrote it before her coffee had gone cold, on a first morning she has every reason to have spent thinking about something else."\n\n"Yes."'))

# Das Bild vom Schatten faellt zwoelf Tage spaeter in Kapitel 32 noch einmal,
# dort gesprochen und als Selbstkorrektur. Hier ist es eine Randbemerkung.
E31.append((
u'He tried the obvious approach first and abandoned it inside ten minutes. Half of Seoul's shipping trade has a surname that starts with one of the four letters, and a list built that way would run to hundreds of names before lunch and be worth nothing at the end of it. Byun had taught him that much in May without meaning to: a letter is not a lead. It is the shadow of one, and shadows point in the direction of a light he still had to find.',
u'He tried the obvious approach first and abandoned it inside ten minutes. Half of Seoul's shipping trade has a surname that starts with one of the four letters, and a list built that way would run to hundreds of names before lunch and be worth nothing at the end of it.'))

AUFTRAEGE.append(('chapters-2/ch31_v2_6_en.md', 'chapters-2/ch31_v3_0_en.md', E31))

# ----------------------------------------------------------------------------
for quelle, ziel, ersetzungen in AUFTRAEGE:
    t = io.open(quelle, encoding='utf-8').read()
    vorher = len(t.split())
    for a, b in ersetzungen:
        if a not in t:
            raise SystemExit('%s: NICHT GEFUNDEN: %s'
                             % (ziel, a[:70].encode('ascii', 'replace')))
        t = t.replace(a, b, 1)
    io.open(ziel, 'w', encoding='utf-8', newline='\n').write(t)
    print('%-34s %5d -> %5d  (%d weg)' % (ziel, vorher, len(t.split()), vorher - len(t.split())))
