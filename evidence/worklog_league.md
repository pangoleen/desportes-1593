# league1593: the other letters in the League polyphonic cipher (started 1 Oct 2026)

Builds on `../sega1593/` (the Desportes letters f. 186 and f. 189, read 1 Oct 2026). Heavy files are on the
Spark: `~/code-breaking/league1593/` (new canvases) and `~/code-breaking/sega1593/` (models, venv, code).

Sources read first: `../sega1593/prior_art/volume.md`, `scholarship.md`, `community.md` (other helpers);
Tomokiyo `mayenne.htm` (29 June 2023), `league.htm`, `nevers.htm`, `bnf4715.htm`; the BnF notice of
fr. 3974-3995 (`prior/catalogue_fr3982.txt`, `prior/catalogue_fr3983.txt`); Bourdeau's catalogue; and the public
repository NoAutopilot/cipher-lab (`prior/cipherlab/`), which worked on this cipher family on 24-29 Sept 2026.

## 1. Inventory of the League polyphonic cipher (Tomokiyo's "Mayenne" cipher)

| # | Shelfmark, folio | Gallica ark, image | Writer -> addressee, date | Cipher extent | Status |
|---|---|---|---|---|---|
| 1 | fr. 3982 f. 97 (no. 41) | btv1b9060543f, 202- | commandeur de Diou -> president Jeannin, Rome, 27 Oct 1592 | about 38 lines per page | Deciphered at the time (BnF: "avec chiffre et double déchiffrement") |
| 2 | fr. 3982 f. 101 (no. 42) | same, 210- | bishop of Lisieux -> "monseigneur" (Mayenne), Rome, 27 Oct 1592 | 46 lines on f. 101r | Deciphered at the time (interlined; "double déchiffrement") |
| 3 | fr. 3982 f. 124 (no. 55) | same, 256- | Diou -> Mayenne, Rome, 12 Nov 1592 | mixed clear and cipher | Deciphered at the time ("double déchiffrement") |
| 4 | fr. 3983 f. 106 (no. 48) | btv1b9059406b, 191- | Mayenne -> Diou, Soissons, 28 Feb 1593 (copy) | about 22 lines | Deciphered at the time (interlined gloss) |
| 5 | fr. 3983 f. 108 (no. 49) | same, 195-196 | Mayenne -> Diou, Soissons, 4 March 1593 | about 28 lines on f. 108v | Deciphered at the time (interlined gloss) |
| 6 | fr. 3983 f. 211 (no. 110) | same, 362 | Mayenne -> Diou, camp of Han, 1 April 1593 | a few words | Deciphered at the time (gloss) |
| 7 | fr. 3984 ff. 176r-v, 179r (no. 84) | btv1b9060633d, 327-328, 333 | Desportes -> Clement VIII, Paris, 22 July 1593 | 47 + 45 + 19 lines | Deciphered at the time (ff. 177r-v, 178r) |
| 8 | fr. 3984 f. 188 (no. 89) | same, 351-352 | Desportes -> bishop of Lisieux, 22 and 26 July 1593 | passages + 21 lines | Deciphered at the time (ff. 184-185) |
| 9 | fr. 3984 f. 186 (no. 88) | same, 347-348 | Desportes -> Pietro Aldobrandini, 22 July 1593 | 74 lines | Read 1 Oct 2026 (`../sega1593/results/f186_reading.txt`) |
| 10 | fr. 3984 f. 189 (no. 90) | same, 353 | Desportes -> Frachetta, 22 July 1593 | 33 lines | Read 1 Oct 2026 (`../sega1593/results/f189_reading.txt`) |
| 11 | fr. 3984 f. 274 (no. 115) | same, 513 | bishop of Lisieux -> Desportes, Rome, July 1593 | 7 lines | Deciphered at the time (interlined) |
| 12 | fr. 4715 f. 61 (no. 38) | btv1b52509819x, 137 | unknown writer and addressee, no date | 99 signs in 6 short passages of a clear French letter | UNREAD. Tomokiyo read five spans ("avec", "est capable", "trop avancees", "jalousie au beau pere", "me l'entendoit") with a variant key and nulls: "Solution incomplete". cipher-lab (29 Sept 2026): "Nothing on f.61r is solved"; 27 of 99 signs null or unread |
| 13 | fr. 2751 ff. 116-119 | btv1b52523734p, 241-248 | Diou -> Mayenne | none | Decipherment only; no cipher text survives (cipher-lab, 24 Sept 2026) |
| 14 | fr. 4699 ff. 37, 41 | not digitised | P. de Fortia -> Roissieu and -> La Chapelle, Lyon, 7 Feb 1593 | unknown | "avec chiffre et déchiffrement" (BnF). Cipher type not known. Cannot be seen online |

Checked and excluded: all other items "avec chiffre" without "déchiffrement" in fr. 3981-3988 are in other
ciphers (Lebel/Savoy, Spanish figure ciphers, the Sega figure memoirs nos. 6 and 8, Pericard, Brulart, Nevers's
own ciphers); see Tomokiyo `league.htm`. fr. 3985 f. 20 (Mauclerc) is deciphered on f. 7. The Italian
decipherments of Sega's letters (fr. 3984 ff. 233-246) belong to a figure cipher, not to this one.

## 2. Ranking of what is left to read (before the heavy work)

1. **fr. 4715 f. 61.** The only leaf of the family with no period decipherment. Value: high (it is the last one).
   Feasibility: uncertain. It is short (99 signs), in another hand, with null signs and a variant sign set.
   A language model has little to hold on to in six short passages. The clear text around each passage helps.
   Plan: find the hand among the glossed letters (cipher-lab says it is the hand of fr. 3983 f. 106-108),
   label glossed lines of that hand, measure a recogniser on held-out glossed lines, then read f. 61 by
   machine and by eye, and state plainly what stays open.
2. **Gaps in the period decipherments** of items 1-6 and 11: look at each leaf; any cipher run without a gloss
   is an unread passage. Value: medium. Feasibility: good where the hand has glossed lines for training.
3. **fr. 3984 f. 179r / f. 178r**: 19 more aligned lines in Desportes's hand. Not unread; it is a free extra
   held-out test for the models that read f. 186 and f. 189.
4. Items 13 and 14: nothing to do online.

## 3. fr. 4715 f. 61 (1 Oct 2026)

- Fetched the native colour canvas 137 once (4079 x 5720) to the Spark. The verso (138) is blank. The leaves
  beside it (f. 60, f. 62) are Montholon letters to Nevers of December 1589 in a figure cipher.
- The hand is not Desportes's, not Lisieux's (fr. 3984 f. 274), not Diou's (fr. 3982 f. 124) and not Mayenne's
  secretary's (fr. 3983 f. 106-108). No other leaf in this hand is known, so no labelled lines exist for a
  fine-tune and no held-out glyph test is possible. With 99 large, well-spaced signs the reading was made
  by eye.
- Result: full reading in `results/f61_reading.txt`. New: lines 10-11 "si le gros home l'entendoit tant soit
  peu"; lines 1-2 "avec [S] et des"; the person sign [S]; the list of nulls. Controls: decoder output and a
  shuffled control (0 of 300 shuffles score as well as the true order of lines 10-11).
- Prior art for f. 61: Tomokiyo bnf4715.htm (five spans, "Solution incomplete"; mayenne.htm 29 June 2023);
  NoAutopilot/cipher-lab `ciphers/fr4715-f61-mayenne-1592/` (last commit 29 Sept 2026 22:18 UTC): I downloaded
  NOTES.md, CAMPAIGN.md, AUDIT.md, HYPOTHESES.md, family/KEY.md, V9_PAGE.md and F61_FLOOR.md and searched them:
  "gros" and "homme" do not occur; the line-10 fragment there is "letresur"; they state "Nothing on f.61r is
  solved". Bourdeau's catalogue and README: no entry for fr. 4715 f. 61. DECODE: no record (per
  ../sega1593/prior_art/community.md). Web search for "le gros homme" with Mayenne / fr. 4715: no reading of
  this leaf. No earlier reading of lines 10-11 found.

## 4. Extra held-out test in Desportes's hand: fr. 3984 f. 179r against f. 178r (1 Oct 2026)

- f. 179r (canvas 333) is the third cipher page of the letter to the Pope: 21 lines, 1,301 glyphs. Its
  decipherment is f. 178r (canvas 331). No line of it was used in training.
- Order of work: (1) the nine models of `../sega1593` read f. 179r BLIND; the output was saved
  (`results/f179r_machine_blind.txt`). (2) I then read f. 178r by eye. (3) I compared, and looked at the image
  wherever the two differed. (4) Gold file `../sega1593/gold/f179r.txt`; score by `eval_struct.py`.
- Result: GLYPH accuracy 99.7 % (4 errors in 1,301); end-to-end LETTER accuracy 98.3 % (23 errors in 1,369).
  The 4 glyph errors: two glyphs lost in a blotted correction with a superscript sign ("deschirer"), one f/s
  read as g/t, one false sign from the library stamp. Most letter errors are the scribe's own spellings
  that the lexicon lacks ("ymaginer", "ymaginaire", "alechement") and one a/n slip of the scribe
  ("tresnes" for "tresues"; the decipherer wrote "tresves").
- This is the cleanest test of the pipeline so far: the lines were unseen, the answer was read after the
  machine output, and the answer key is the 1593 office's own decipherment.

## 5. Survey of the glossed letters: is any passage left unread? (1 Oct 2026)

Fetched once at 1400 px (Spark, `img/`): fr. 3982 images 202-217 and 256-271; fr. 3983 images 189-198, 362-363.
- fr. 3982 f. 97r-v (Diou to Jeannin): cipher with an interlinear gloss; a separate clear decipherment follows
  on ff. 98-99. cipher-lab's note "no word layer" on f. 97r is wrong: the gloss is there.
- fr. 3982 f. 101r-v (Lisieux): interlinear gloss on every line; separate clear decipherment on ff. 102-103.
- fr. 3982 ff. 124r-125v (Diou to Mayenne): interlinear gloss; separate clear decipherment on ff. 128-130.
- fr. 3983 ff. 106r-108v (Mayenne to Diou): interlinear gloss over every cipher line that I can see at this
  size. No separate sheet. I did not check word by word at native size that no cipher word lacks a gloss.
- fr. 3983 f. 211r (image 362): one short cipher run in a clear letter about the siege of Noyon, glossed.
Result: nothing unread found in these letters. They agree with the BnF notice ("avec chiffre et double
déchiffrement" for fr. 3982 nos. 41, 42, 55; "avec chiffre et déchiffrement" for fr. 3983 nos. 48, 49, 110).

## 6. Accuracy per hand

| Hand | Test | Glyphs | Letters |
|---|---|---|---|
| Desportes (fr. 3984) | f. 179r, 21 unseen lines, read blind, key = f. 178r | 99.7 % (4 / 1,301) | 98.3 % (23 / 1,369) |
| Desportes | 12 held-out lines of f. 188v, f. 176r, f. 176v (earlier session) | 99.0 % | 97.3 % |
| Lisieux's secretary (fr. 3984 f. 274r) | Desportes models, ZERO-SHOT, 6 glossed rows (`zeroshot274.py`) | 55.9 % (75 / 170) | not decoded |
| fr. 4715 f. 61 | no labelled leaf in this hand exists; read by eye; decoder and shuffled controls | - | - |

Negative result: the Desportes models do not transfer to another hand. In Lisieux's hand the trefoil e/r sign
comes out as "unknown sign". Each hand needs its own labelled lines. Nothing in Lisieux's, Diou's or
Mayenne's secretary's hand is unread, so I trained no model for them.

## 7. What would take it further

- fr. 4715 f. 61: identify the hand and the date (the Nevers papers around it are of 1589); find who [S], "le
  beau pere" and "le gros home" are. A second leaf in this hand would settle the nulls and the two odd signs.
- fr. 4699 ff. 37 and 41 (Fortia, Lyon, 7 Feb 1593) are not digitised; a BnF reproduction would show whether
  they are in this cipher.
- fr. 3983 ff. 106-108 at native size: confirm that every cipher word has a gloss.
- The Desportes models with f. 179r added to the training set could re-read f. 186 and f. 189; the open points
  there are code signs and blots, so the gain would be small.
