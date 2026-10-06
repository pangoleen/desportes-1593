# Two cipher letters of July 1593, read for the first time

A first reading of two enciphered letters from the Catholic League, written in Paris on 22 July 1593, three days
before Henri IV abjured Protestantism.

**Part of a larger set.** Nine results of the same project, with a map of every key, reading and image, are in
[pangoleen/cipher-readings](https://github.com/pangoleen/cipher-readings) (start with its
[GUIDE.md](https://github.com/pangoleen/cipher-readings/blob/main/GUIDE.md)).

| Letter | Shelfmark | State before | State now |
|---|---|---|---|
| Desportes to Girolamo Frachetta | Paris, BnF, ms. français 3984, f. 189 | "Undeciphered" | [first reading and translation](reading/f189.md) |
| Desportes to Pietro Aldobrandini, the Pope's nephew | BnF, ms. français 3984, f. 186 | "Enciphered passages are undeciphered" | [first reading and translation of the cipher passages](reading/f186.md) |

**Status: first reading, version 0.2, 1 October 2026.** Every line was checked against the page image by the model
that made the reading. No palaeographer has checked it yet. Most signs for persons are resolved from the deciphered
sister letters (the Pope, the King of Navarre, Mayenne, the King of Spain, the Legate, Guise). A few signs and all
cover names ("nostre oncle", "l'homme de la chesne", "l'homme du colege", "docteur Gratian") are open.
Corrections are welcome: please open an issue.

## What the letters say

The writer is an agent of the Duke of Mayenne, head of the League. He writes to Rome in the week when the League's
cause turns.

- To Aldobrandini: the enemy (Henri of Navarre) wins over many who were against him "by the show he makes of
  wishing to become a Catholic, **and on Sunday he is to go to Mass**". Spain wants the League to elect a king, but
  its army "has done nothing but stay on the frontier". Everyone is "tired of serving as a tale for all
  Christendom".
- To Aldobrandini again: the Legate "has shown himself their partisan, to tear apart our poor state", and Mayenne
  was patient to the point of "being willing to accept Monsieur [de Guise] for king, provided he was shown the means
  to defend him".
- To Frachetta: "I hold that we shall have the truce within a few days." The journey of an envoy "has made [the King
  of Navarre] change religion". The papal legate "has done what he could to cover the Spaniard" and "has neglected
  the service of his master, to the point of not delivering a single one of our briefs", working instead "to hasten
  the dismemberment of our state".

Henri IV abjured and heard Mass on Sunday 25 July 1593. The general truce followed on 31 July.

## Why nobody had read them

The cipher was not the obstacle. Satoshi Tomokiyo reconstructed it from sister letters: eleven signs, each of which
stands for two letters, plus signs for common words and for names
([cryptiana, "A Polyphonic Substitution Cipher of the Catholic League"](http://cryptiana.web.fc2.com/code/mayenne.htm)).

The obstacle was the handwriting. The two letters hold about 5,000 small drawn signs. Because each sign has two
values, a wrong sign damages the words around it. An attempt in September 2026 (D. Bourdeau, `cyphersolver`) read
73 to 79 % of the signs and concluded that more than 90 % is needed.

The royal office that intercepted the letters did not read them either. Its register of 1593 says of the letter to
Aldobrandini that "l'on n'a eu loisir encores de deschiffrer", and of the letter to Frachetta: "qui n'a non plus
encore esté deschiffrée" (BnF, ms. français 3983, f. 141v, entries 13 and 14;
[image](images/fr3983_f141v_entries_13_14.jpg)). The back of f. 189 carries the file number 14 and the same note
([image](images/f189v_endorsement.jpg)).

## How the reading was made

1. **A larger answer key.** The office deciphered two sister letters in 1593, and the sheets are bound in the same
   volume (f. 177 for f. 176, f. 184-185 for f. 188). We transcribed the old decipherment of f. 177 (74 lines) and
   aligned both sister letters with their cipher, sign by sign. Result: 112 lines and 6,794 labelled signs in the
   same hand ([gold/](gold/)). The earlier attempt had about 1,100.
2. **Corrected references.** The cipher spells words differently from the office's clean copy ("espagnolz",
   "fist"). The reference text was corrected to the cipher's own spelling.
3. **A line recogniser.** A model reads a whole line of signs, trained on the labelled lines.
4. **A decoder.** It chooses between the two letters of each sign with a model of period French and a lexicon of
   77,004 word forms.

## How good is it

Measured on lines that were held back from training (482 signs, 505 letters, read by eye before any model existed):

| Measure | Earlier attempt | This work |
|---|---|---|
| Signs read correctly | 73 to 79 % | 98.5 % |
| Letters correct after decoding | 30 to 40 % | 95.6 % |

A later blind test on a page found afterwards (f. 179r, 21 lines, checked against the office's decipherment of
1593) gave 99.7 % of signs and 98.3 % of letters.

A control with planted errors shows that each 1 % of sign error costs about 1.5 % of letters. Details are in
[evidence/accuracy.md](evidence/accuracy.md) and in the full work log, [evidence/worklog.md](evidence/worklog.md).

## Is the reading new

We looked for an earlier reading and found none. What was checked, and what was not, is in:

- [prior_art/community.md](prior_art/community.md): the codebreaking community and 2026 projects.
- [prior_art/scholarship.md](prior_art/scholarship.md): catalogues, editions and historical literature.
- [prior_art/volume.md](prior_art/volume.md): the manuscript volume itself and its neighbours, page by page.
- [evidence/register_1593.md](evidence/register_1593.md): the royal office's own notes that the letters were not
  deciphered.

The office that intercepted the letters noted three times that it had not deciphered them: on the back of each
letter (f. 187v: "non encore deschiffree"; f. 189v) and in its register (ms. français 3983, f. 141v).

Open gaps, stated plainly:

- The sister letter to the Pope is marked "Duplicata". A first copy of each dispatch may have left Paris by another
  route. If one reached Rome, its addressee read it there in 1593. No such copy or reading is known.

- The Archivo General de Simancas (Estado, legajos 961 and 963) holds copies of letters that Frachetta gave to the
  Spanish ambassador in September 1593. Nobody has checked whether the letter of 22 July is among them.
- The Vatican and Aldobrandini archives were not checked.
- Several printed works could be searched only in part.

## Who wrote the letters

The 1593 register calls the writer "Desportes". The office wrote "Baudouyn Desportes" on its decipherments
(f. 178v, f. 185v), and the BnF catalogue names him "Baudouin-Desportes". Satoshi Tomokiyo holds that Baudouin is
right (October 2026). One more fact supports this: Mayenne's letter of 4 March 1593 to the commandeur de Diou, in
this same cipher, is countersigned "Baudouyn" (BnF, ms. français 3983, f. 109v). So Mayenne's secretary Baudouin
worked with this cipher.

Part of the literature (Lavaud 1936, Drouot 1937) keeps this man apart from Thibault Desportes, sieur de
Bévilliers, brother of the poet Philippe Desportes and envoy of Mayenne to Rome. The reply of the bishop of Lisieux
is addressed to "Desportes Sr de Beuvillier" (f. 274v), and an earlier version of this file preferred Thibault for
that reason. The point stays open, and a comparison of hands would settle it. See
[prior_art/scholarship.md](prior_art/scholarship.md).

## Follow-up of 3 October 2026

S. Tomokiyo published this reading on 3 October 2026 and asked two questions
([cryptiana, "An Intercepted Report of Henry IV's Upcoming Attendance at Mass in a Polyphonic Cipher"](https://cryptiana.web.fc2.com/code/polyphonic1593.htm)).

- **Do the two letters add something to the letters that the office read in 1593?**
  [reading/comparison.md](reading/comparison.md). In short: the forecast of the conversion on Sunday is not new.
  The office read it in the letter to Lisieux ("Il se doibt faire cath. dimanche", f. 184r). Seven passages are in
  the two unread letters only.
- **Who deciphered the other letters in 1593?** [evidence/decipherer_1593.md](evidence/decipherer_1593.md). In
  short: the office read this cipher from the letters of 27 October 1592 onward; its clerks did not know the rare
  signs, so the key was probably rebuilt and not captured; the hands are not Viète's. No clerk is named. A hand
  comparison by a model is weak evidence, so the panels are in `images/` for a palaeographer to judge.

Two of his three corrections to the clear text of f. 186r are applied, with one more change of notation
("[le Legat]": the sign carries the article). His third reading, "en reste" for "icy reste" (l. 12), is noted in
the reading file.

## Credits

- **Satoshi Tomokiyo** reconstructed the cipher and listed the two letters as undeciphered.
- **Daniel Bourdeau** (`dbourdeau/cyphersolver`) made the first attempt, identified the leaves and the ground-truth
  pages, and published notes and labels that this work started from.
- **Bibliothèque nationale de France / Gallica** provides the page images. Images here are reduced crops with the
  credit "gallica.bnf.fr / BnF".
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents, and with a
  DGX Spark for training.

## Contents

| Folder | Content |
|---|---|
| `reading/` | The readings, with the raw machine output in `reading/raw/`, and the comparison of the four letters of 22 July. Also a third leaf in the same cipher, BnF fr. 4715 f. 61, read in full (`fr4715_f61_reading.txt`); Tomokiyo had read five spans of it. |
| `gold/` | The labelled lines used for training and testing, and our transcriptions of the 1593 decipherments: f. 177-178 (use the file `v2`; the first one has errors) and f. 184 |
| `evidence/` | Accuracy figures, the 1593 register entries, the work log, and the study of the 1593 decipherer |
| `prior_art/` | The search for earlier readings |
| `images/` | Reduced images for reference |
| `code/` | The scripts as they were used. They are not yet cleaned up. |

## Open points

- A check of both readings by a palaeographer. The model checked every line against the page images; a human has
  not.
- The remaining signs and the cover names.
- The gaps in the search for earlier readings (see "Is the reading new").

The work logs in `evidence/` are the logs as written during the work. They name folders of the working machines
(for example `prior/bourdeau/`, `tmp/`, `results/`); those folders are not part of this repository. No file from
another project is included here.

## Licence

Code: MIT. Text: CC BY 4.0. Images: reduced crops from Gallica, under the BnF's conditions of reuse, with the
credit "gallica.bnf.fr / BnF". Details are in [LICENSE.md](LICENSE.md).
