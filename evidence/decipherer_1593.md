# Who deciphered the League letters of July 1593, and did the office hold the key?

Work of 3 October 2026, as written during the work. It names folders of the working machines (`sega1593/`, `league1593/`, the Spark); those folders are not part of this repository. The three panels of hands are in `images/`. Question from S. Tomokiyo, "An Intercepted Report of Henry IV's Upcoming Attendance at Mass
in a Polyphonic Cipher" (3 Oct 2026, https://cryptiana.web.fc2.com/code/polyphonic1593.htm): who deciphered the
letters to the Pope and to the bishop of Lisieux, and was it François Viète?

Marks used below:
- **[img x2]** = read on a native page image and checked a second time on a closer crop.
- **[img x1]** = read once on a native page image. Not checked twice.
- **[inferred]** = my conclusion, not a statement of a source.
- A hand comparison made by a model is weak evidence. The images are here so that a palaeographer can judge.

Shelfmarks: BnF ms. français 3982 (Gallica `btv1b9060543f`), 3983 (`btv1b9059406b`), 3984 (`btv1b9060633d`),
3985 (`btv1b90606498`); BnF Cinq Cents de Colbert 33 (`btv1b10033958p`). "Image N" is the Gallica view number.

## Short answer

1. The sheets f. 177r-v and f. 178r are a **working decipherment made straight from the cipher by two clerks who
   took turns**, often in the middle of a sentence. It is almost word-perfect.
2. The office read the letter signs with full fluency, and it rendered the frequent signs for persons at once. It
   **did not know the rare signs**: it copied two of them into the decipherment as drawings, and it dropped a third.
   In the decipherment of the Lisieux postscript (f. 185r) another writer copied the person signs and wrote the
   names above them afterwards, and left the sign for Guise bare. In October 1592 the same office left a blank
   for that same sign. This is the pattern of a **reconstructed key, not of the League's own key table**.
   Confidence: medium to high that the office did not hold the League table of signs; medium that it broke the
   cipher by analysis (I cannot exclude a captured letter alphabet without the list of signs).
3. The office read this cipher **from the letters of 27 October 1592 onward**, and again in March-April 1593. The
   July 1593 work is routine work in a cipher that the office already knew.
4. Hands: none of the hands on the 1593 decipherments looks like Viète's autograph. Two are French secretary
   hands; Viète wrote a large upright italic. The digest is endorsed "nevers 1593 sett", with the same filing
   formula as Nevers's own autograph letter written at Nevers on 8 September 1593.
5. The best present answer [inferred]: **a small group of clerks whose papers stayed with the duke of Nevers**,
   with at least three writers. Hand A is the chief decipherer: a hand that looks the same deciphered the Mauclerc letter
   of 3 August 1593 in another cipher (fr. 3985 f. 7r), and a hand of the same family worked on the Rome letters
   of October 1592. Two readings stay open, and I put them at about two to one:
   (i) they are Nevers's own secretaries, who read the letters at Nevers in August-September 1593;
   (ii) hands A and B are the king's decipherers (Chorin, or a clerk of Viète), who worked on the packet while
   Nevers was at court on 7-15 August 1593 and gave him the sheets; Nevers's secretary (hand C/E) then did the
   Lisieux letter and the digest.
   Viète in person: not likely (he was at Tours; the hands differ; his file shows nothing for that summer).
   Names of the clerks: not found.

---

## (a) The decipherer's deviations

### How the comparison was made

- Cipher side: `desportes-1593/gold/f176r.txt`, `f176v.txt`, `f179r.txt` (112 lines, about 1,740 words, 50 sign
  tokens), with the glyph positions in `tmp/struct_*.json` on the Spark, and crops of the cipher lines.
- Decipherment side: I read f. 177r (34 lines), f. 177v (40 lines) and f. 178r (19 lines) again, line by line, on
  native crops (canvases c329, c330, c331).
- **The file `desportes-1593/gold/f177_office_decipherment_1593.txt` is not a safe base for this comparison.** It
  is a first reading with many errors of ours, and most of its apparent "deviations" are not on the page. Examples:
  it has "saincte convention" (page: "faincte conversion"), "dix pieces et naura rien" (page: "Et dy penser
  Remuer rien"), "Il y a dix ans" (page: "Il y a ung an"), "ou mesmes" (page: "ou encores"), "faire perdre a la
  demeure Joinct aussi" (page: "fe penser a ladvenir Injuste Ce q"), "vingt mil hommes" (page: "xij^m hommes"), and
  its lines v35-v40 are mostly wrong. I did not edit the file (public repository). It needs a new transcription.
- The gold file `f176r.txt` lacks one short line of cipher: a marginal addition at the foot of f. 176r, "ainsi Q a
  la personne de [Mayenne sign]" (line 46 in `struct_f176r.json`), with an insertion mark in line 28. The
  decipherer put it in the right place (f. 177r line 25: "ainsi q a la personne de du Mayne") [img x1].

### Table of deviations (f. 177r, f. 177v, f. 178r against the cipher)

| Kind | Count | Notes |
|---|---|---|
| Words where the decipherer chose the wrong letter of a sign pair, or guessed | 3 sure, 4 possible, in about 1,740 words | Sure: "de ne luy desnier une tresve" for "celuy de faire une tresve" (f. 177v line 16: "de faire" and "desnier" are the same seven signs; he added "ne" above the line to save the sense, and the digest follows him with "estoit de luy accorder"); "mal entre nous" for "malgre nous" (g/t); "guerres" for the scribe's "tresnes". Possible: "quilz" for "ou ilz"; "se Reduict" for "la reduit"; "ne luy pouvoit" for "ne len pouvoit"; "l'apprehention" for "la prevention" (h/u; both readings are good French, and his can be the right one) |
| Words left out and marked | 1 | "deschec": a "+" in its place (f. 177r line 28) |
| Signs left out without a mark | 1 | The sign after "tresnes" on f. 179r line 10 |
| Signs copied into the decipherment as drawings (not understood) | 2 | f. 177v line 23 (Jupiter-like sign, later glossed "dallemagne"); f. 177v line 26 (h-like sign, a trial word struck out) |
| Words added that are not in the cipher | 0 | The one apparent addition is the marginal line of the cipher (see above) |
| Self-corrections on the sheet (strike-through, overwriting, insertion) | about 14 | 177r: lines 13, 16, 20, 23, 26, 27 (two), 34. 177v: lines 12, 16, 26, 35, 39. 178r: lines 9, 10 |
| Silent corrections of the cipher scribe's slips | about 10 | "prendre" (cipher "pendre"), "laissans" (cipher "laisse" + one stray sign), "par ce moyen courage" (cipher "ce m en courage"), "ordre" ("ordr"), "grandz" (broken word), "donnent" ("donnen"), "escrire" ("escrir"), "matiere" ("matire"), "asseuré" ("asseue"), "cognois" ("cosnoist") |
| Signs for persons, places and common words rendered at once, in line, with no gap | about 47 of 50 | Sa/Vostre Saincteté ("V. S."), le R. d'Hespaigne, France, "party", le Roy de Navarre ("R. de N."), Mons. de Guyse, l'Infante, Mr du Mayne, Mr le Legat, d'Espagne, le Sr Pietre |
| Normalisation | throughout | He writes his own spelling ("yeux", "subiect", "relligion", "cath."), "3000" for "trois mil", "quinze" for "xv" |

The rate of real misreadings is under 0.5 % of the words. The two clerks read this cipher as a matter of routine.

### The ten most telling examples

1. **f. 177v line 23** [img x2]. Cipher (f. 176v line 22): "les exemples de [sign like the Jupiter symbol] &
   dagleterre". Decipherment: "veu q les exemples de [the same sign, drawn] . & dangleterre", with a gap and a
   point. Above the sign, in a thinner pen: "dallemagne". The clerk did not know the sign. He drew it and left
   room. The name came later, and it fits the sense (Germany and England as the lost kingdoms). A man with the
   key table writes the name at once.
2. **f. 177v line 26** [img x2]. Cipher (f. 176v line 25): "la depesche escrite a [sign like h with a bar] le
   m^s". Decipherment: "la despesche escripte a [the same sign, drawn] [one word, struck out] . Le m^s mal sur
   lestat". He drew the sign, tried a meaning, and struck it out. The sign stays unread.
3. **f. 185r** (postscript to Lisieux, hand D) [img x1]. The writer copies the person signs and adds the names
   above the line: "le legat" (twice), "du Mayne". He leaves the Guise sign bare: "la proposition quilz ont faicte
   de [δ] pour estre Roy". He leaves a gap after a struck "luy": "les promesses que [gap] luy avoit faictes". On
   f. 177r, hand A writes "Mons de Guyse" for the same sign with no hesitation; there the context ("marier [δ]
   avec [the Infanta]") gives the name away.
4. **f. 184r lines 10, 13, 14** (hand C) [img x1, seen first by the coordinator]. "du Mayne ——", "Le Roy
   despaigne", "le Legat" stand in gaps, in larger letters. The names were put in after the line was written.
5. **fr. 3982 f. 101r and f. 102r** (Lisieux to Mayenne, Rome, 27 Oct 1592) [img x1]. In the cipher the group
   "Monsieur-sign + δ" stands in the left margin. The interlinear gloss has nothing above it. The separate
   decipherment has "soit vous Monseigneur, Monsieur de [blank] ou aultre agreable a ung chascun". The decipherer
   of 1592 knew the sign for "Monsieur" and not the sign for Guise. A League secretary cannot have left that blank.
6. **f. 177r line 28** [img x2]. Cipher: "K ne sera pas peu deschec". Decipherment: "qui ne sera pas peu +, &
   apres". He could not turn the seven signs d/q e/r f/s c/p h/u e/r c/p into "d'eschec". He put a cross and went
   on. This shows a man who works from the sign pairs. It does not separate "key held" from "key broken": the true
   addressee had the same trouble.
7. **f. 177r line 27** [img x2]. He wrote "chascun faict", struck "faict" and wrote "scait" (cipher "sait"; f and
   s share one sign). A wrong choice inside a pair, caught at once.
8. **f. 177r line 20** [img x1]. He wrote "en grande apprehension", struck it, and wrote "entrez en apprehension"
   (cipher "entres en aprehention"). He guessed ahead of the signs and then corrected. So f. 177 is the first
   writing, made straight from the cipher. It is not a fair copy.
9. **Two hands take turns on one sheet** [img x1]. f. 177r: hand A. f. 177v lines 1-17: hand B. Lines 18-32: hand
   A. From the middle of line 32 ("En semblable les Raisons") to line 40: hand B. f. 178r lines 1-15: hand B; from
   "Ce a quoy nous voyons" in line 15 to the end (line 19): hand A. Both clerks could decipher. Small dashes in the left
   margin of the cipher page f. 176v can be their place marks; I did not check this.
10. **f. 177v, margin beside lines 16-19** [img x2]. A third, italic hand: "C'est de le faire pape comme apert par
    aultres lres que les espagnolz le luy promettoyent". The note explains "l'Interest de son particulier" of the
    Legate. The writer knew other intercepted letters. The same reader underlined many passages and wrote a "Nota"
    mark beside f. 177r lines 22-34; the digest (fr. 3983 f. 141r) uses those passages.

Other points:
- The cipher pages f. 176r-v and f. 179r carry no interlinear gloss and no work marks (overview seen at 760 px).
  The letters of 1592 and of spring 1593 carry an interlinear gloss. By July 1593 the office wrote the plain text
  straight on a new sheet.
- "poquinteste" (f. 184r line 9) is **not** a transliteration. On f. 188r line 10 Desportes wrote "de
  poquinteste" in clear text, in his own hand [img x1, native crop of c351]. The clerk copied it. The first
  letter has the same form as the p of "principal", "par" and "prejudice" on the same lines. So the word of
  f. 189 line 17 (classes C B + D H I A G E F G E) is "po" + "quinteste".
- The digest gives the numbers as "15 jours", "3000 chevaux" and "12 m hommes". The cipher has roman numerals in
  clear ("xv", "xij^m"). The numbers needed no key.

## (b) Verdict: key held, or cipher broken?

**The office worked with a key that it had built itself. It did not hold the League's table of signs.**
Confidence: medium to high (about three in four).

For:
- Rare signs are drawn, not read (examples 1 and 2), or dropped.
- Frequent person signs are read at once on f. 177 (written last?), glossed after the fact on f. 185r, and put
  into gaps on f. 184r (examples 3 and 4). The order of the three sheets is not known; the pattern is the same in
  each order: names come from the sense, one by one.
- The Guise sign is a blank in 1592, bare on f. 185r in 1593, and read on f. 177r where the sense forces it.
- The copy of an intercepted Lisieux letter of October 1592 (fr. 3982 f. 105r) also has open gaps in the text.

Against, or neutral:
- The speed and the accuracy of f. 177 are those of trained clerks with a complete letter table. That is true
  for a broken cipher and for a held key alike.
- A clerk with the true table can meet a sign that the writer made up after the table was issued. This explains
  one or two drawn signs. It does not explain the blank for Guise in 1592.
- I cannot tell how the office first got the eleven letter pairs. Analysis of the long Rome letters of October
  1592 is the simple answer [inferred]. A captured alphabet without its list of names is possible. No work sheet
  (frequency count, trial alphabet) was found; I did not search for one in fr. 3982.

What the sheets do not show: any sign of a first break in July 1593. The July decipherment is not a feat of that
month. If there was a break, it was in late 1592.

## (c) When could the royalist side first read this cipher?

| Date of letter | Leaf | What is there | Who glossed it |
|---|---|---|---|
| 27 Oct 1592, Diou to Jeannin, Rome | fr. 3982 f. 97r-v (images 202-203); f. 98-99 (204-205); address f. 100v (209) | Sealed original; interlinear gloss; separate decipherment | Royalist office [inferred from the next row] |
| 27 Oct 1592, Lisieux to Mayenne, Rome | fr. 3982 f. 101r-v (210-211); f. 102-103 (212-214); address "A Monseigneur" with two seals, f. 104v (217) | Sealed original; interlinear gloss on every line; separate decipherment, numbered "37." at the head, with corrections and the blank "Monsieur de ___" | Royalist office: the blank for Guise excludes a League clerk [img x1] |
| Oct 1592, Lisieux to Mayenne | fr. 3982 f. 105r (image 218) | "Coppie de la lre Intercepte escrite par l'Evesque de Lizieulx a Monsieur de Mayenne", numbered "34." at the head; gaps left in the text | The heading says "intercepted" in the office's own words [img x1] |
| 12 Nov 1592, Diou to Mayenne, Rome | fr. 3982 f. 124-130 (256-271) | Gloss and separate decipherment (per `league1593/NOTES.md`; I did not look again) | not checked |
| 28 Feb 1593, Mayenne to Diou, Soissons | fr. 3983 f. 106-107 (191-194) | Interlinear gloss | not checked in detail |
| 4 Mar 1593, Mayenne to Diou, camp of Soissons | fr. 3983 f. 108-109v (195-198) | Original, marked "Dup.ta", signed "Charles de Lorraine", countersigned "Baudouyn"; interlinear gloss in a small secretary hand | An outgoing League original with a gloss, kept in the Nevers papers: intercepted and read by the royalist office [img x1; inferred] |
| 22-26 July 1593 | fr. 3984 f. 176-189 | See (a) | The office of the digest |

Result: the royalist side could read this cipher when it worked on the Rome letters of 27 October 1592. The
sheets carry no date of work. The letters cannot have been taken before late November 1592. The numbers "34." and
"37." belong to a numbered file older than the digest of September 1593 (whose numbers are 1-27); I did not find
the list that goes with them.

A side result for the question "who is Desportes": the Mayenne letter of 4 March 1593 in this cipher is
countersigned "Baudouyn" (fr. 3983 f. 109v, image 198) [img x1].

## (d) Hands

Side-by-side images (same pixel scale within a few per cent; about 160-170 px per cm; contrast stretched):

- `../images/hands_viete_vs_office.jpg`: Viète (V1, V2), Cinq Cents de Colbert 33 f. 402r of October 1593 (V3), and the
  four hands of the 1593 decipherments (A, B, C, D).
- `../images/hands_office_1592_1593.jpg`: the office hands of 1593 (A, A2, B, C, D, the digest E, the marginal note M)
  beside the office work on the letters of October 1592 (H = f. 105r, Gl = gloss f. 101r, G = f. 102r).
- `../images/hands_nevers_vs_office.jpg`: Nevers's autograph of 8 September 1593 (N) beside D, M and E.
- Script: `mkpanels.py`. Source crops: `src/`.

| Label | Leaf | Script | Role |
|---|---|---|---|
| A | fr. 3984 f. 177r; f. 177v lines 18-32; f. 178r lines 15-19 | French secretary; "que" always as the q-with-stroke sign; "&" as a hooked sign | Decipherer 1 |
| B | f. 177v lines 1-17 and 32-40; f. 178r lines 1-15 | French secretary, more angular; writes "que" and "Et" in full; reversed e; open p | Decipherer 2 |
| C | f. 184r-v (Lisieux letter) | Small upright round hand, italic forms mixed with secretary abbreviations | Decipherer or copyist 3 |
| E | fr. 3983 f. 140-144 (digest) | Same type as C | Digest writer |
| D | fr. 3984 f. 185r (postscript) | Round italic, less formal than C | Decipherer 3 or 4 |
| M | f. 177v margin | Bold italic | Reader and annotator |
| H, G, Gl | fr. 3982 f. 105r, f. 102r, f. 101r | French secretary | Office work of 1592-93 |
| N | fr. 3985 f. 209r (image 419) | Fast sloping italic; signed "Lodovico Gonzaga"; own number cipher in the text | The duke of Nevers, at Nevers, 8 Sept 1593 |
| V1 | Cinq Cents de Colbert 33 f. 260r (image 265) | Large upright italic | Author's draft with the struck words "envoyees a F. V. pour estre Interpretees en decembre" |
| V2 | Cinq Cents de Colbert 33 f. 198r (image 203) | Same hand as V1 | Corrections on the printed pamphlet of 1590, Viète's hand according to Pesic 1997 n. 8 (via Tomokiyo) |
| V3 | Cinq Cents de Colbert 33 f. 402r (image 407) | Fine sloping italic | Working translation of Tassis, 26 Oct 1593. Writer not named |

What I see (weak evidence, for a palaeographer to confirm or reject):

- **V1 and V2 are one hand.** Same R with a long leg, same upright d with a straight stem, same two-stroke e.
- **A and B are not Viète's hand.** They are French secretary scripts; V1/V2 is a pure italic. This difference is
  one of script type and is safe.
- **C, D, E and M are italic in type, and still differ from V1/V2**: their d has a stem bent back to the left
  (uncial form), V1/V2 has a straight stem; they are small and round, V1/V2 is large and angular with small
  capitals inside words ("Duc", "Roy"). I see no hand of Viète on the League decipherments.
- **C and E look like one hand** (the digest writer wrote the fair decipherment of the Lisieux letter).
- **D and M can be the same hand as C/E at a faster pace, or a second writer of the same school.** The coordinator
  sees f. 184 and f. 185 as two hands. I cannot decide.
- **H, G and Gl (1592) are of the same family as A and B.** G has the capital I and the ductus of A, and the open
  p of B; G and Gl write "que" in full like B. Same office, probably the same clerks; not proved.
- **N (Nevers himself) is not C, D, E or M.** His hand is much faster and slopes.
- **The decipherment of the Mauclerc letter of 3 August 1593 (fr. 3985 f. 7r) looks like hand A** [img x1, on the
  1000 px copy `sega1593/prior_art/img/fr3985_f007r_dechiffrement_Mauclerc.jpg`; not in the panels]: same large
  looped initial, same q-with-stroke sign. That letter is in another cipher (code numbers). So hand A was not a
  copyist for one cipher; he was the man who deciphered.
- **V3 is not A, B, C or D.** So the Viète file of October 1593 and the Nevers file of July-September 1593 show
  different writers.
- Limit: Viète used clerks (Tomokiyo names Charles du Lys and Jacques Alleaume). The absence of his hand does not
  exclude his office. The endorsements and the place do that better (next point).

Endorsements:
- fr. 3983 f. 145v (digest): "nevers 1593 sett / Extraict de plusieurs lres Interceptes." and a paraph
  (`sega1593/prior_art/img/z3983_f145v_endorse.jpg`) [img x1]. The first line is in a small fast hand; the title
  is in a clear italic.
- fr. 3985 f. 209r, left edge (Nevers's autograph letter from Nevers, 8 Sept 1593): "nevers [..] sett / 8 [..]
  sett 93" [img x1, 1500 px image; two words not read]. Same formula, same Italian month form "sett".
- [inferred] "nevers 1593 sett" on the digest is a filing note of the Nevers archive: place or owner, year,
  month. It ties the digest to Nevers's own papers of September 1593. It does not name the decipherer.

## (e) Where the people were, and prior art

### The passage in the Mémoires de Nevers

*Mémoires de M. le duc de Nevers*, ed. Gomberville (Paris, 1665), part 2, p. 482 ("Discours d'Estat"; Gallica
`bpt6k64451005`, view 531; https://gallica.bnf.fr/ark:/12148/bpt6k64451005/f531.item ). Nevers to the Pope, after
his audiences in Rome (winter 1593-94). Transcribed from the page image [img x2]:

> Comme aussi d'avoir trouvé bon de n'adjouster foy aux impostures que Monsieur le Cardinal de Plaisance vous a
> escrit de moy en Aoust dernier; disant en premier lieu, qu'il m'avoit convié de parler à luy lors que j'estois à
> saint Denis, & que je ne luy avois fait aucune response. D'ailleurs que j'avois fait prendre à Nevers toutes les
> lettres qui n'estoient parvenuës en vos mains, & en ce faisant avoir rejetté son pernicieux dessein [...]

> Je pense aussi avoir suffisamment verifié à vostre Sainteté le contraire de ce qu'il vous a escrit touchant
> lesdites lettres interceptes, pour vous avoir fait connoistre que ledit sieur Cardinal, sçachant fort bien que la
> ville de Nevers est en l'obeïssance du Roy, & qu'il y a garnison payée par sa Majesté, il n'est pas vray-semblable
> qu'apres avoir reconnu que l'on luy avoit pris deux ou trois de ses pacquets passant par ladite ville, il ait
> voulu continuer à y faire passer les autres, mais qu'il aura fait tenir autres chemins à ses messagers pour
> aller à Lion ou en Lorraine, pour les porter seurement, ainsi qu'il se peut faire, & que la verité est qu'il a
> fait.

What the source states: the Legate wrote to Rome in August 1593 that Nevers had the missing letters taken at
Nevers. Nevers does not deny that "two or three" packets of the Legate were taken "passant par ladite ville". He
denies that all the missing letters were taken there. He speaks of a time "lors que j'estois à saint Denis"; the
catalogue dates below put him there on 7 and 9 August 1593, not on the day of the abjuration.

What I infer: the packet of 22-28 July 1593 was taken at Nevers by the royal garrison in Nevers's own town, in
the first days of August, while the duke was away. The papers went to the duke. This fits the endorsement of the
digest.

### Results of the search in printed sources

A sub-search made these checks on 3 October 2026 (web only). I verified three items myself in the OCR text of the
*Lettres missives*; they are marked **[verified]**. All other items are **reported, not checked by me**.

Where Nevers was (reported; source: the printed BnF catalogue, *Catalogue des manuscrits français. Ancien
fonds*, vol. 3, items of fr. 3984-3986, https://archive.org/details/p1cataloguegnr03bibluoft ):
- 12 July 1593: he grants the capitulation of Dannemoine (fr. 3984 f. 147).
- 25 and 26 July: Henri IV writes to him from Saint-Denis (fr. 3984 f. 199, f. 231). So Nevers was not at the
  abjuration. Our own survey of the volume has these two letters (`desportes-1593/prior_art/volume.md`, images
  365-368 and 429-431).
- Saint-Denis 7 and 9 August; Melun 13 August; Montereau 14-15 August; **Nevers 21 August to 18 September**;
  then "Fovan, frontière" 26 September, Villersexel 28 September, Montbéliard 29 September, Basel 1 October, Chur
  9 October, Poschiavo 13 October, Desenzano 20-23 October, Rome 21 November 1593.
- I confirm one point on the page: fr. 3985 f. 209r is an autograph letter "de Nevers ce 8 septembre 1593"
  [img x1].
- [inferred] The digest holds letters up to 22 August 1593 and is filed "nevers 1593 sett". It was made during
  the duke's stay at Nevers, before he left for Rome between 18 and 25 September. Its use is plain: a file for
  the embassy to the Pope. A like file exists for 1592: fr. 3982 no. 110, "Copie de plusieurs depeches
  interceptées d'Espaigne, et deschifrées et baillées à Mr le marquis de Pisani, pour apporter au pape, en
  octobre 1592" (BnF notice, `league1593/prior/catalogue_fr3982.txt`).

Viète (reported): at Tours in 1592-93 (French Wikipedia "François Viète", after Ritter 1895). Tomokiyo: Cinq
Cents de Colbert 33 has nothing between early 1590 and October-November 1593.

Chorin:
- 1590: Agrippa d'Aubigné, *Histoire universelle*, ed. de Ruble, vol. 8, pp. 201-202 (reported; Tomokiyo cites
  the Thierry edition).
- **[verified]** Henri IV to Beauvoir, Paris, 26 February 1595 (*Recueil des lettres missives de Henri IV*,
  vol. 4, pp. 308-310, https://archive.org/details/recueildeslettre04henr ): "Je vous envoie Chorin, l'un des
  aides des mareschaux de camp, et par luy les originaux et memoires de certaines lettres qui sont tombées
  entre mes mains, lesquels estans escripts en chiffres il a deschiffrez. L'archiduc Ernest les envoyoit au roy
  d'Espagne [...]"; "une personne duquel l'industrie a deschiffrer toutes sortes de chiffres est d'autant plus
  remarquable, que sa profession est d'estre soldat et de mieux servir son Roy de son espée que de sa plume."
  (OCR text, read once. The year in the OCR heading is not clear; the letter before it is dated Paris,
  26 February 1595.)
- **[verified]** Henri IV to du Plessis, 24 July 1594 (same volume): "au faict particulier duquel Chorin m'a
  parlé de vostre part". Chorin was then with the king, after the surrender of Laon.
- Nothing found on Chorin for 1592-1593.

How the court handled intercepts:
- **[verified]** Henri IV to Matignon, 23 November 1593 (*Lettres missives*, vol. 4): La Borde "vous portoit une
  depesche de moy fort importante, avec le déchiffrement et l'alphabet des lettres interceptées que vous m'aviés
  auparavant envoyées". So in 1593 a governor sent intercepts to the court, and the court sent back the
  decipherment **and the alphabet**.
- Reported: Henri IV to Nevers, 31 May 1593 (*Lettres missives*, vol. 3, pp. 785-786), speaks of "lettres
  interceptées, tant du légat que d'aultres".
- [inferred] This gives a second way to the same sheets. Nevers sends the Rome packet of October 1592 to the
  court; the king's decipherer breaks it and returns the plain text and the alphabet; from then on Nevers's
  clerks read the cipher themselves. The alphabet that comes back is a reconstructed one, with the names worked
  out from the sense. That is what the sheets show. So the finding of (b) holds in both cases; only the name of
  the man who made the first break changes.

Nevers's household and ciphers:
- Tomokiyo, "Catalogue of Ciphers (Mainly Related to Duke of Nevers) in BnF fr. 3995"
  (`league1593/prior/nevers.txt`): the volume holds, beside Nevers's own keys, **partial reconstructions of
  ciphers from intercepted letters** (his nos. 31-34, 39, 48, 50, 51, 53, 54; dates 1590-1592), some with notes
  in Italian ("di parigi", "fiorenza"), and no. 55 "Chiffre de monsieur du Mayne avec le Chevalier de Dyou"
  (1592), the other cipher of the same two men. Nobody reports a sheet for the polyphonic cipher there.
  [inferred] Someone near Nevers, who wrote Italian, rebuilt intercepted ciphers in 1590-1592. This supports
  reading (i) below.
- Secretaries of Nevers in 1592-94: no name found with a role (reported). A council at Nevers on 24 September
  1592 names Champlemys, Champloiseau, Montholon, Bolacre, Romenay, Marchant, signed De Lachassaigne (BnF
  fr. 4718 no. 50), without roles (reported).
- Blaise de Vigenère: no proven office with Nevers after 1566 (Boltanski, reported); a letter of July 1593 to the
  duke exists (Métral 1939, via Wikipedia, reported). His place in 1593 was not found. He died in 1596. Nothing
  ties him to these sheets. Do not name him.

Prior art (reported, plus my reading of Tomokiyo's two pages): no historian names the decipherer of the League
intercepts in the Nevers papers. L'Épinois (1886, pp. 573-604) quotes the pieces and names nobody. De Ruble's
note in d'Aubigné (vol. 8, p. 202) links fr. 3982 to letters "interceptées et déchiffrées" without a name.
Tomokiyo (3 Oct 2026) asks the question and calls Viète "an obvious candidate". Nobody we found cites the 1595
letter on Chorin in this context.

Not accessed: Boltanski 2006 (book), Pesic 1997, Ritter, Kahn, Richard, Drouot, Lavaud, Tizon-Germe, De Waele,
Le Roux; the *Mémoires de Nevers* beyond view 531; the BnF online notices (blocked on that day).

### Two readings of "who", side by side

| Point | (i) Nevers's own clerks | (ii) the king's decipherers, sheets given to Nevers |
|---|---|---|
| Working sheets with struck words lie in Nevers's papers | fits | needs the decipherer to hand over his only sheet |
| Hand A, or its family, on the Rome letters of 1592, on the Mauclerc letter of 3 Aug 1593 (fr. 3985 f. 7r, other cipher) and on f. 177 | one clerk of the house over nine months | one court decipherer over nine months, each time for Nevers |
| Digest in hand C/E, filed "nevers 1593 sett", says "l'on n'a eu loisir encores de deschiffrer" | the office speaks of its own work | the secretary reports what the court men left undone |
| fr. 3995: rebuilt keys of intercepted ciphers, Italian notes | fits | neutral |
| Court practice: "le déchiffrement et l'alphabet" sent back (Nov 1593) | neutral | fits |
| Nevers at court 7-15 August 1593, a few days after the capture | neutral | fits, and explains "no leisure" for two letters |
| Hands C and D (f. 184, f. 185) work in a different way from A and B | two levels of skill in one house | two different teams |

A test that can settle it: find hand A or B in a dated minute or letter of Nevers's secretariat (fr. 3974-3995,
fr. 4699-4720), or in a paper of the royal camp.

## (f) What stays open

1. Names. No clerk of the office is named. A palaeographer who knows the Nevers secretaries of 1590-1595 can
   test hands A, B, C/E and D against signed minutes in fr. 3974-3995 and fr. 4699-4720.
2. The first break. Where and when the letters of 27 October 1592 were taken; who first read them; whether a
   work sheet survives. The numbered file with "34." and "37." needs its list. fr. 3982 f. 105-131 and the
   digest-like pieces of fr. 3982-3983 were not read.
3. Whether the office held a captured alphabet. A League key sheet in the Nevers papers would settle it.
   Tomokiyo found the original of another Mayenne cipher in fr. 3995 no. 55; nobody has reported the table of
   the polyphonic cipher there.
4. The three rare signs (Jupiter-like "dallemagne"?, the h-like sign after "escrite a", the round sign after
   "tresnes" on f. 179r). The 1593 clerks did not know them either.
5. The reading "tresnes" on f. 179r line 10. The 1593 clerk wrote "guerres" [img x2, the first letter is not
   certain]. Our gold file reads "tresves". With the Spain-like sign after it, "traisnes" (delays) is a third
   candidate. This touches the published reading of f. 179r, not f. 186 or f. 189.
6. My readings marked [img x1].
7. Whether hand D is the digest writer, and whether hand A is one man from October 1592 to August 1593.
8. The marginal dashes on f. 176v as place marks of the two clerks.
9. The date and the place of capture of each packet (July-August 1593, and autumn 1592).
10. Chorin's hand. No autograph of his is known to us. If one exists (for example in the State Papers, France,
    1595), compare it with hands A and B.

## Files

- `NOTES.md`: this file.
- `f177_f178_office_decipherment_v2.txt`: the new line-by-line transcription of f. 177r, f. 177v and f. 178r
  (34 + 40 + 19 lines), made from this re-reading. It is meant to replace the faulty first reading.
- `../images/hands_viete_vs_office.jpg`, `../images/hands_office_1592_1593.jpg`, `../images/hands_nevers_vs_office.jpg`.
- `mkpanels.py`: builds the three panels from `src/` and from `../compare/img/c343.jpg`, `c345.jpg`.
- `src/`: Tomokiyo's pages as fetched on 3 Oct 2026 (`polyphonic1593.htm`, `viete.htm`, `viete.txt`,
  `nevers.htm`); IIIF
  manifest of Cinq Cents de Colbert 33; Gallica IIIF images and regions fetched once each (Cinq Cents de Colbert
  33 images 203, 204, 206, 248, 265, 407, 614; fr. 3982 images 212, 218; fr. 3983 image 249; fr. 3985 images 419,
  420; Mémoires de Nevers view 531).
- On the Spark, `~/code-breaking/sega1593/decipherer/`: band crops of f. 177r (`r_*.jpg`, `rb_*.jpg`), f. 177v
  (`v_*.jpg`), f. 178r (`w_*.jpg`), zooms `z1`-`z8`, sign sheets `signs_f176r.jpg` etc.

Note on Gallica: the HTML and text pages now answer with a "Vérification de sécurité" page. I did not try to
pass it. The IIIF image service answered normally. So I read printed pages from images, and I could not use the
Gallica full-text search.
