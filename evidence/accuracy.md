# Accuracy

All figures come from the work log, [worklog.md](worklog.md), 1 October 2026.

## Reference material ("gold")

| Page | Content | Lines | How it was labelled |
|---|---|---|---|
| f. 188v | Desportes to the bishop of Lisieux, cipher | 21 | Read by eye against the 1593 decipherment on f. 184-185 |
| f. 176r, f. 176v | Desportes to Clement VIII, cipher | 91 | Aligned to our transcription of the 1593 decipherment on f. 177; every disagreement checked on the image |
| **Total** | | **112 lines, 6,794 signs** | |

The files are in [../gold/](../gold/).

## Held-out test

Twelve lines were kept out of training: f. 188v lines 7 to 10, f. 176r lines 20 to 23, and later f. 176v lines 20
to 23. The first eight (482 signs, 505 letters) were read by eye before any model existed.

| Measure | Result | Earlier attempt (Bourdeau, 17 Sept 2026) |
|---|---|---|
| Signs read correctly | 98.5 % (7 errors in 482) | 73 to 79 % |
| Letters correct after decoding | 95.6 % (22 errors in 505) | 30 to 40 % |

A second test on twelve lines (the same eight plus f. 176v lines 20 to 23; 728 signs, 767 letters), with three
models trained on 100 lines, gave 99.0 % of signs (7 errors) and 97.3 % of letters (21 errors). The four added
lines are a softer test, because their labels were made by correcting recogniser output against f. 177v.

On the unread pages, nine models disagree on 1.0 % of signs (f. 189), 1.3 % (f. 186 recto) and 2.0 % (f. 186
verso). Only 0.2 % of signs fall outside words of the lexicon.

In the first test the recogniser was an ensemble of four models, trained on 53 lines (3,166 signs) at the time of this test. One
held-out label was corrected after the test, when the image showed that the label was wrong.

## Blind test on a page found later (f. 179r)

The letter to the Pope has a third cipher page, f. 179r, which was not known when the models were trained. The
models read its 21 lines first, and the output was saved ([f179r_machine_blind.txt](f179r_machine_blind.txt)). Only
then was the office's decipherment of 1593 on f. 178r read and used as the answer key.

| Measure | Result |
|---|---|
| Signs read correctly | 99.7 % (4 errors in 1,301) |
| Letters correct after decoding | 98.3 % (23 errors in 1,369) |

This is the cleanest test: unseen lines in the same hand, and an answer key written by the royal office in 1593.

The models do not transfer to another hand. On six glossed rows of f. 274r (the bishop of Lisieux's secretary),
without retraining, they read 55.9 % of the signs.

## How much sign error the decoder tolerates

Control: the true sign strings of all 112 reference lines (7,169 letters), with random confusable substitutions,
deletions and insertions added, and a lexicon built from the corpus only.

| Sign error | Letters correct |
|---|---|
| 0 % | 98.6 % |
| 2 % | 95.2 % |
| 5 % | 90.7 % |
| 10 % | 84.8 % |
| 20 % | 71.8 % |
| 25 % | 66.0 % |

Each 1 % of sign error costs about 1.5 % of letters. At 1 to 2 % sign error the text stays readable. At the earlier
25 % it does not.

## Limits

- The unread pages have no reference text, so their error rate is not measured. The held-out figures are the best
  estimate.
- The decoder uses a language model, which can make a wrong reading look fluent. Words marked `[..]` in the
  readings are places where the output is not coherent.
- The signs for names and titles are outside these figures.
