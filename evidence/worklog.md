# sega1593: running log (session of 1 Oct 2026)

Target: BnF fr. 3984 f. 186r-v and f. 189, Baudouin-Desportes, Paris, 22 July 1593. The key is known
(Tomokiyo, cryptiana `mayenne.htm`, last modified 29 June 2023). The task is glyph recognition.

Credit: Daniel Bourdeau's session of 17 Sept 2026 (`prior/bourdeau/`, copied from
github.com/dbourdeau/cyphersolver, targets/sega1593): gold labels, f. 185 text, segmenter, classifier, decoders.

## Log

- 11:45 Copied Bourdeau's folder to `prior/bourdeau/`. Fetched cryptiana `mayenne.htm` and the key image to
  `prior/cryptiana/`. The page has no 2026 update.
- 11:46 Fetched Gallica canvases at full size to `img/cNNN.jpg`: 326-330, 347, 348, 351, 352, 353.
  Canvases 343-345 gave HTTP 429. Retry later, slowly.
- 11:50 Found: f. 177 carries the decipherment on recto AND verso (canvases 329 and 330).
- Disk: the Mac has less than 1 GB free. Keep files small. The venv uses 0.9 GB.
- 12:30 Read f. 177r (34 lines) and f. 177v (40 lines) from native-resolution strips. First transcription in
  `f177_plain.txt`. Doubtful words carry [?]. The verso is in a second secretary hand. The last three lines are
  hard. The cipher on f. 176 must settle the doubtful words.
- 13:00 Line segmentation with curved centre lines (`seglines.py`, `pages.py`): f188v 23 lines, f189 33,
  f176r 47, f176v 45, f186r 52, f186v 33. Line crops are straightened and cut on demand.
- 13:30 Read f. 188v lines 2-22 by eye against f. 185 and wrote line-level gold transcripts in cipher spelling
  (`gold/f188v.txt`, 1,180 glyphs). Found: the cipher spelling differs from the decipherment in many places
  (espagnolz, tresve, autrement, fist, feux, pais). Bourdeau's `f185_plain.txt` has errors: the cipher reads
  "hier [Navarre] fist sa profession", "ou ie trouve peu de difficultes", "les espagnols lont fait ainsi".
  The *qui* sign in this hand is an arrow with three bars; A (a/n) has a variant with an extra crossbar.
- 13:50 Negative result: a CTC recogniser trained from scratch on 17 lines of f. 188v does not converge
  (it outputs only E). It needs a bootstrap from cut glyphs or more lines.
- 14:00 Compute moved to the DGX Spark at the coordinator's request: `spark:~/code-breaking/sega1593/`
  (venv with torch 2.14.1+cu130, CUDA works). The Mac keeps notes, scripts and results only.
- 14:30 Read f. 176r lines 0-39 by eye with f. 177 as a guide (`gold/f176r.txt`). The cipher corrects the first
  f. 177 transcription in many places ("leur armee si petite", "avec ces choses faire une si vive recherche",
  "a un an", "ou encores au temps", "peu deschec", "ne fussent pour aporter"). Signs fixed by context:
  ♁-like = vostre Sainctete (also ".S.S."); φ with two crossbars = Navarre; arrow with three bars = qui;
  σσ = par; ℒ/# = roy d'Espagne; g = France; δ = M. de Guise; ΔΔ = the Infanta; "Sr"-like = et.
  The scribe leaves word spaces in the cipher.
- 15:10 Trainer made fast (bf16 autocast, channels_last, fixed pad width; 0.06 s per step alone).
- 15:20 KEY RESULT. Line-level CTC (5 conv blocks + 1D conv, no RNN, 64-px-high line images, heavy augmentation)
  trained on 47 gold lines (f188v 2-6, 11-22; f176r 0-19, 24-33; 2,807 glyphs), tested on 8 held-out lines
  (f188v 7-10, f176r 20-23; 481 glyphs): glyph error 2.9 % at epoch 100, 1.7 % at epoch 200.
  Bourdeau's cut-box classifiers reached 73-79 % accuracy. What moved it: (1) clean line-level transcripts read
  by eye against the known plaintext, in the cipher's own spelling, in place of noisy box alignment; (2) a
  segmentation-free sequence model, so merged and split boxes do not matter; (3) straightened line crops.
- Corpus for the language model: 22 OCR volumes from archive.org (Henri IV Lettres missives, Catherine de
  Medicis Lettres, Memoires de la Ligue, Villeroy, Satyre Menippee): 5.9 M words after filtering (`lm_build.py`).
- 16:00 Decoder (`decode.py`): word-lattice Viterbi over glyph classes. A lexicon trie over class patterns
  (62,460 period words; the signs que/qui/pour/par may stand inside a word), a word-bigram model, a character
  5-gram fallback for words not in the lexicon, soft word gaps from the recogniser (the scribe leaves word
  spaces; the CTC model has a space class), and one substitution per word from ensemble disagreement.
  Control on TRUE glyph strings of the 8 held-out lines: 97.9 % of letters right. So the polyphonic layer
  itself costs about 2 % with this language model.
- 16:40 HELD-OUT RESULT 1 (4 models, trained on 53 lines / 3,166 glyphs; test f188v 7-10 and f176r 20-23,
  482 glyphs, read by eye before any model existed): glyph accuracy 98.5 % (7 errors), end-to-end letter
  accuracy 95.6 % (22 errors in 505 letters). Bourdeau: 73-79 % glyphs, 30-40 % letters.
  One held-out gold label changed after the test (f176r l. 23 "grans" has three a/n glyphs; the image confirms).
- 17:00 f. 176v (45 lines) labelled by the semi-automatic route: recogniser output, corrected to the f. 177v
  text, then every disagreement (44 of 2,805 glyphs) checked on the image (`cmp_gold.py`, `spots.py`). In about
  half of the cases the recogniser was right and my draft wrong (the scribe's slips: "escrir", "fair",
  "labadonner", "ioze", "touiours"). f. 176r lines 40-45 added. Gold set now 112 lines, 6,794 glyphs.
  f. 177 corrections from the cipher: "prevention dune feinte conversion", "le Sr Pietre ma fait cest honneur"
  (Pietro Aldobrandini), "In foro conscientiae" is in clear on f. 176v, "preocupee", "desnuez de tous moiens".
- 17:10 Launched 6 runs on the Spark: v_* (hold-out f188v 7-10, f176r 20-23, f176v 20-23) and p_* (all lines,
  for the unread pages).
- First machine reading of f. 189 (2 quick models) is already coherent French; see `tmp/read_f189.txt`.
- 17:40 Language model rebuilt (`lm_build.py`): the 18th-century prints (Memoires de la Ligue, Villeroy) had long s
  read as f by the OCR; each non-final f is now resolved against the clean volumes. Absolute discounting
  (D = 2) in the bigram model; spelling-variant rules add the scribe's phonetic forms to the lexicon
  (77,004 word forms).
- 17:50 DECODER TOLERANCE CONTROL (`tolerance.py`; true glyph strings of all 112 gold lines, 7,169 letters,
  corpus-only lexicon, random confusable substitutions + deletions + insertions, no ensemble alternatives):
  glyph error 0 % -> 98.6 % letters; 2 % -> 95.2 %; 5 % -> 90.7 %; 10 % -> 84.8 %; 20 % -> 71.8 %;
  25 % -> 66.0 %. So each 1 % of glyph error costs about 1.5 % of letters, and the recogniser's 1-2 % error
  is inside the range where the text stays readable.
- Sign table from the deciphered pages (f. 177, f. 185): ♁/".S.S." = Sa/Vostre Sainteté; ♀ with two bars =
  le roy de Navarre; Ω = M. du Maine (Mayenne); ℒ and "#" = le roy d'Espagne; g with under-loop = France;
  plain g after the Monsieur sign = le Legat; crossed "ƻ" with bars = Monsieur; δ = M. de Guise; ΔΔ =
  l'Infante; S with a cross = Saint; "Sr" superscript = Sieur; σσ = par (also inside words: Rty, Rler).
- Prior-art check so far: cryptiana `mayenne.htm` (last modified 29 June 2023), `league.htm` (2019),
  `unsolved.htm` (27 Sept 2026): nothing on f. 186 / f. 189 beyond "undeciphered". Bourdeau's README (30 Sept
  2026): "Not read". BnF notice of fr. 3984: no. 88 and no. 90 are "Lettre, avec chiffre" (no decipherment),
  while nos. 84, 86, 87, 115 have "déchiffrement". BnF fr. 3983 no. 72 (ff. 140-146) is the royal office's
  "Extraict de lectres interceptés, tant en chiffre qu'aultrement": it lists Desportes to the Pope (22 July)
  and to Lisieux (22 and 26 July), but NOT the letters to Aldobrandini and Frachetta.
  Web search for phrases of the reading ("docteur Gratian", "l'homme de la chesne") with Desportes/Frachetta:
  no hit.
- 18:30 HELD-OUT RESULT 2 (final). Models v_s0, v_s1, v_r0 trained on 100 gold lines (6,066 glyphs); test on
  12 lines never used for training (f188v 7-10, f176r 20-23, f176v 20-23; 728 glyphs, 767 letters):
  GLYPH accuracy 99.0 % (7 errors); end-to-end LETTER accuracy 97.3 % (21 errors).
  Per page: f188v 96.7 % of letters, f176r 95.9 %, f176v 99.2 %. (`eval_e2e.py`)
  Caveat: the f176v gold was made by correcting recogniser output against f. 177v, so its 4 lines are a
  softer test than the 8 lines read by eye before any model existed (those: 98.5 % glyphs, 95.6 % letters).
- 18:40 Unread pages read with 9 models (p_s0, p_s1, p_r0 trained on all 112 lines; v_*, h_*): f189 2,088
  glyphs, f186r 2,565, f186v 2,046. Ensemble disagreement 1.0 %, 1.3 %, 2.0 % of glyphs; glyphs outside
  lexicon words 0.2 %. Raw machine output with glyph classes: `results/dump_*.txt`.
- 19:30 Every line of the three pages checked on the image (annotated sheets `annot.py`, zooms `wspot.py`,
  `gl.py`); edited readings with doubt marks and translations: `results/f189_reading.txt`,
  `results/f186_reading.txt`. Findings on the hand: the sign with a crossed stroke over S = Sa Sainteté, with
  two bars = Monsieur; "V.S.I." is a clear abbreviation; clear "Mre" = maistre; "part.er" = particulier; on
  f. 186v the gutter hides the last 1-2 glyphs of most lines.
- External checks of the reading (none was in the lexicon or forced by the language model):
  "doit dimanche aller a la messe" (22 July 1593 was a Thursday; Henri IV abjured on Sunday 25 July);
  "Mateouci/Mateuci" and "Malvoisie" (the papal commissaries Girolamo Matteucci and Innocenzo Malvasia);
  "pontificat du [pape] Gregoire" (Gregory XIV paid the papal army of 1591); "duc de Feria"; "accepter
  Monsieur [de Guise] pour roy" (the Spanish proposal of July 1593, also in f. 188v).
- Prior-art check (final): cryptiana mayenne.htm / league.htm / unsolved.htm (27 Sept 2026) - "undeciphered";
  Bourdeau README and repo (30 Sept 2026) - "Not read"; BnF notice - nos. 88, 90 "avec chiffre" only, and the
  royal office's extracts (fr. 3983 no. 72) skip both letters; web searches for "Mateuci"/"Malvoisie" with
  Desportes 1593, "docteur Gratian", "homme de la chesne", "servir de fable a toute la crestiente": no hit.
  I found no earlier reading. I did not search printed literature (e.g. studies on Frachetta or on Philippe
  Desportes's brother) beyond the web.
- Not resolved: one name in f189 l. 17; the sign after "voiage de" (f189 l. 26); f186v ll. 0-3 (about 10
  glyphs, gutter); the clear words of f186r l. 17; the cover names of the Frachetta letter.
- Housekeeping: canvases, models, logs and renders live on the Spark (`~/code-breaking/sega1593/`, 370 MB
  without the venv). The Mac keeps scripts, gold, lines, results. To rerun: `./sync.sh`, then on the Spark
  `./venv/bin/python eval_e2e.py v_s0.pt v_s1.pt v_r0.pt` and `annot.py <page> 0 60 <models>`.

## What would take it further
- A specialist's check of the code signs and cover names; the Aldobrandini and Frachetta papers may name them.
- Higher-resolution or colour images of f. 186v (gutter) and the blots on f. 189.
- f. 274 and the other letters in this cipher (fr. 3982, 3983, 4715 f. 61) should now read with the same
  models after a few gold lines of each hand.
- The clear opening of f. 186r still needs a letter-by-letter transcription.
