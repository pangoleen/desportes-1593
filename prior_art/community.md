# Prior-art check: modern codebreaking community, 2015 to today

Target: BnF, ms. français 3984, f. 189 (Desportes to Girolamo Frachetta, Paris, 22 July 1593) and the cipher
passages of f. 186r-v (Desportes to Pietro Aldobrandini, same date). Gallica ark `btv1b9060633d`.

Date of all checks: 1 October 2026, about 12:25 to 12:55 UTC. Method: direct download of the pages (curl),
the GitHub API (read-only), web search, and the public DECODE API. I wrote no code in the project and changed
no project file. This report is the only file that I made.

## Verdict

**No earlier reading found in these sources.**

No source in this scope holds any part of the plaintext of f. 189 or of the cipher passages of f. 186. Each
distinctive phrase of our draft gives zero hits on the web and zero hits in GitHub code search. Three sources
name the two leaves, and all three say that they are not read.

One lead is outside this scope and is still open. Read section 6 before you claim "first reading" in public.

## The three most important facts

1. **The record is unchanged.** Tomokiyo's `mayenne.htm` has the HTTP header `Last-Modified: 29 June 2023`. It
   still says "(f.186) ... Enciphered passages are undeciphered" and "(f.189) ... Undeciphered". His
   `unsolved.htm` (modified 27 September 2026) does not list these leaves. His blog has no post or comment about
   them.
2. **Two AI projects tried or examined the leaves and neither has a reading.** Bourdeau's repository and site
   (last push 30 September 2026, 22:30 UTC) still say "not read" and "not solved". The only commit to the
   work folder after 17 September is a folder move. A second project, `NoAutopilot/cipher-lab`, holds images of
   f. 186r and f. 189r and calls them "the family's undeciphered leaves" (28 September 2026). Its last commit
   is 1 October 2026, 12:09 UTC. It has no transcription and no plaintext of these leaves.
3. **A contemporary copy can exist in Spain.** The Frachetta literature (A. E. Baldini) says that in September
   1593 Frachetta gave his letters from Mayenne and Desportes to the Spanish ambassador in Rome. The ambassador
   sent copies in cipher to Madrid: Archivo General de Simancas, Estado, leg. 961 (from 20 September 1593) to
   leg. 963 (21 February 1594). I did not find the 22 July letter there, and I could not open those files. This
   is not an earlier reading. It is the place where one could be.

## 1. Tomokiyo: Cryptiana site and blog

I downloaded the index `crypto.htm` and all 280 article pages that it links. I searched each page for "3984",
"Desportes", "Frachetta" and "Aldobrandini".

| Source | Last modified (HTTP header) | What it says about f. 186 / f. 189 | Plaintext? |
|---|---|---|---|
| http://cryptiana.web.fc2.com/code/mayenne.htm | 29 June 2023 | Lists both leaves. "(f.186) Baudouin-Desportes to Pietro Aldobrandini ... Enciphered passages are undeciphered." "(f.189) Baudouin-Desportes to Hieronimo Frachetta ... Undeciphered." Gives the reconstructed key. | No |
| http://cryptiana.web.fc2.com/code/league.htm | 27 November 2019 | Lists "no.88 (fol.186)" and "no.90 (fol.189)" with the other Desportes letters. Sends the reader to `mayenne.htm` for the cipher. | No |
| http://cryptiana.web.fc2.com/code/unsolved.htm | 27 September 2026 | Does not name fr. 3984, Desportes, Frachetta, Mayenne or the League. It has a notice dated September 2026: many solutions arrive, he has "not caught up in noting them all", and the reader must check Bourdeau's site. | No |
| http://cryptiana.web.fc2.com/code/crypto.htm (index) | 30 September 2026 | The "NEW" marks are on other articles (Francis I 1530, Cyphral Distich). No new League article. | No |
| http://cryptiana.web.fc2.com/code/nevers.htm | 8 February 2023 | Names fr. 3984 f. 7 and f. 198 only. | No |
| `henryiv2.htm`, `savoy.htm`, `spanish3.htm`, `paleography.htm` | 2019 to 2023 | Name other leaves of fr. 3984 (f. 197, f. 182, no. 47, no. 68). Not f. 186 or f. 189. | No |
| `variable3.htm` | 25 September 2026 | False hit: "3984" is inside a digit string of another cipher. | No |

Pages modified after 17 September 2026: `catinat1691`, `chinesecrypto_e2`, `cyphraldistich`, `danzay`,
`francis2`, `habsburg`, `louisxiv_villars`, `maitland`, `spanish2C`, `unsolved`, `variable3`,
`walsingham_wilkes`, `worcester`. None of them is about the League cipher.

Blog, https://cryptiana.blogspot.com: I read the feed of the last 150 posts (23 March 2024 to 30 September
2026) and all 102 comments in the comment feed. No post and no comment contains "3984", "Desportes",
"Frachetta", "Aldobrandini" or "Mayenne". The blog search for "Mayenne", "3984", "Desportes" and "Frachetta"
gives zero posts. The 12 posts after 17 September 2026 are about other ciphers.

## 2. Bourdeau's project and its forks

| Source | State on 1 October 2026 | Plaintext? |
|---|---|---|
| https://raw.githubusercontent.com/dbourdeau/cyphersolver/main/targets/sega1593/NOTES.md | Session of 17 September 2026. "Outcome: **not read**." "Two hand-read lines of f. 189 ... decode to nothing." Closed as "not solvable with the present tools". | No |
| https://dbourdeau.github.io/cyphersolver/catalogue.html (entry no. 20), site built 30 September 2026, 22:32 GMT | "Attempted 17 Sept 2026, not read." | No |
| https://dbourdeau.github.io/cyphersolver/writeups.html and index.html | Row "not solved · Baudouin-Desportes → Aldobrandini and → Frachetta". No write-up page (`sega1593.html` gives 404). | No |
| https://github.com/dbourdeau/cyphersolver, commits | 2,003 commits since 15 September. Commits on the folder: d74ebae9 (17 Sept, "closed as not read"), fd38e72f (20 Sept, profiles), d5affd9d (24 Sept, classification), 648309e8 (26 Sept, folder move). None adds a reading. Last push 30 September, 22:30 UTC. | No |
| Same, `README.md`, `TARGETS.md`, `papers/lasry/classification_review.csv` | "not read", "not solved". The list of solutions made for George Lasry on 30 September does not include it. | No |
| Same, issues and pull requests (14 visible, numbers 1 to 16) | Search for "Desportes", "Frachetta", "sega", "Aldobrandini": zero. "3984" gives only PR 8 (Spanish despatches, nos. 47 and 68). Discussions are off. Issues 11 and 12 were deleted (HTTP 410). I could not read them. | No |
| Same, six other branches | No branch changes a file with "sega", "3984" or "desportes" in its name. | No |
| Forks: `setsunaatto/cyphersolver`, `arya1515/cyphersolver`, `aryasn2026/cyphersolver` | Each `main` is 0 commits ahead of Bourdeau. Their other branches are for other letters (Champagne 1590, Sessa 1593, Maisse 1592, Lorraine 1592 and others). | No |
| https://github.com/NoAutopilot/cipher-lab, `ciphers/fr3984-sega-1593/NOTES.md` | A check for earlier solutions made on 24 to 27 September 2026. Verdict "blocked": "none claims a decipherment of nos. 6/8/88/90". "Not decoded, not transcribed here." It names an edition that it could not open (section 6). | No |
| Same, `ciphers/fr4715-f61-mayenne-1592/family/` | Work on the same cipher family, 28 to 29 September. It read the glossed leaves (fr. 3982 f. 97, f. 101, f. 124; fr. 3984 f. 176, f. 188, f. 274). `KEY.md`: "fr.3984 f.186r and f.189r (Desportes) remain the family's undeciphered leaves; they were not cut in this job". The repository holds two 1600-pixel images of the leaves and nothing more for them. Last commit to this folder: 29 September, 22:18 UTC. | No |
| https://github.com/aaymeloglu/unsolved-ciphers | Nine targets. None is fr. 3984. | No |

Two useful facts come from `cipher-lab`:

- Fol. 175 ("22 de Juillet 1593", clear French) is not a decipherment of f. 189. The BnF finding aid says that
  it is the decipherment of no. 74, the letter of the baron de Talmet.
- fr. 3985 no. 7 (Mauclerc to Creil), which Bourdeau put in the same catalogue entry, is a clear-text copy and
  is in print (Goujet 1758, vol. 5, pp. 411-414). This does not affect f. 186 or f. 189.

GitHub code search, all public repositories: "Frachetta" + "3984", "Baudouin-Desportes", "Desportes" +
"Frachetta" and `btv1b9060633d` give hits only in `dbourdeau/cyphersolver` and `NoAutopilot/cipher-lab` (and
one false hit in a student list).

## 3. Other AI-assisted projects and public discussion

| Source | Result | Plaintext? |
|---|---|---|
| https://carter.church/writeups/ | One cipher write-up: the Marmont letter of 1809. | No |
| https://github.com/swarm-ai-research/cipher-break-verification | Enigma 1941 and ADFGVX 1918 only. | No |
| https://github.com/benjaminbreen/PremodernCiphers (made 23 September 2026) | Armstrong 1808, Banér 1640 and others. Code search for our names: zero. | No |
| explainx.ai articles; https://www.schneier.com/blog/archives/2026/09/claude-fable-solves-a-historical-cipher.html (9 September 2026) and its comments | Cyphral Distich, Enigma, ADFGVX. No League cipher. | No |
| prinzai.com | Web search finds no cipher page. Not opened. | Not known |
| Hacker News (Algolia search) | "Frachetta", "Catholic League cipher", "polyphonic cipher", "fr. 3984": zero relevant hits. Threads 49713489 and 49769216 link Bourdeau's site and have 1 and 0 comments. Threads 49766756 and 49689335 have no comment on the League, 1593 or Desportes. | No |
| Reddit | Not accessible (section 7). | Not known |
| X/Twitter, LinkedIn, Medium, Substack | Web search finds nothing on these leaves. No direct search was possible. | Not known |

## 4. Blogs, proceedings, journals, DECODE

| Source | Result | Plaintext? |
|---|---|---|
| Klaus Schmeh, https://scienceblogs.de/klausis-krypto-kolumne/ (site search) | "Mayenne", "Desportes", "Frachetta": no post. Control search "Tomokiyo": 7 posts. | No |
| cipherbrain.net | No connection. Not checked. | Not known |
| Nick Pelling, https://ciphermysteries.com (site search) | "Mayenne", "Desportes", "Frachetta", "fr. 3984": "Nothing Found". | No |
| HistoCrypt 2018 to 2023, https://ecp.ep.liu.se/index.php/histocrypt (site search) | "Mayenne", "Desportes", "Frachetta", "Ligue": zero. "Catholic League": Lasry 2022, "Deciphering a Letter from the French Wars of Religion" (article 402). It is a letter of Sennecey in a homophonic cipher. Not our leaves. "polyphonic": Conti 1649 and Rudolf II. | No |
| HistoCrypt 2024 and later, https://dspace.ut.ee (search API) | "Frachetta": zero. "Catholic League": Desenclos and Lasry 2024, Henri IV to Nevers, 1592, a digit cipher. Not our leaves. | No |
| Cryptologia | By web search only. Tomokiyo, "Identifying Italian ciphers from continuous-figure ciphertexts (1593)", vol. 43 no. 1, is about fr. 3984 nos. 6 and 8 (the Sega notes in figures). No article on f. 186 or f. 189 found. The 2026 "DescryptTool" article gives HTTP 403. | No |
| DECODE, https://de-crypt.org/decrypt-web/RecordsList (public API `api/list/records`) | 10,106 records. Holder contains "3984": 0 records. "3982", "3983", "3985", "Français 4715": 0 each. Control "Français 3995": 73 records. DECODE has no record for these leaves, so it has no transcription and no decipherment of them. A copy of the full record list in `aaymeloglu/unsolved-ciphers` (highest id 10198, the same as the live list) agrees. | No |
| MysteryTwister | Tomokiyo's "Polyphonic Substitution Cipher, part 1" (November 2019) is a made challenge with English plaintext. It does not use the manuscript. | No |

## 5. Distinctive phrases

Web search, each phrase in quotation marks, in the old and the modern spelling: "haster le desmembrement de
nostre estat" / "hâter le démembrement de notre état"; "nostre docteur gratian" / "notre docteur Gratian";
"l'homme de la chesne" / "l'homme de la chaîne"; "ennemis formelz" / "ennemis formels" with "neutres"; "que
l'on aura la trefve dans peu de jours"; "a este le plus pernicieulx"; "n'avoir fait tenir un seul de nos
brefs"; "ne se sont pas seulement montres neutres". **No hit that is a 1593 text.** The results are dictionary
pages and texts that have no relation.

GitHub code search, all public repositories: "desmembrement de nostre estat", "docteur gratian", "homme de la
chesne", "ennemis formelz": **0 results each**.

## 6. Leads outside this scope (not earlier readings, but check them)

1. **Simancas.** A. E. Baldini, "Girolamo Frachetta: un pensatore politico nell'Italia della Controriforma",
   https://www.ragionidistato.it/2021/02/07/girolamo-frachetta-un-pensatore-politico-nellitalia-della-controriforma/
   (note 29), and his entry "Frachetta, Girolamo" in the *Dizionario Biografico degli Italiani*, vol. 49 (1997),
   https://www.treccani.it/enciclopedia/girolamo-frachetta_(Dizionario-Biografico)/. In September 1593
   Frachetta gave his correspondence with Mayenne and Desportes to the Spanish ambassador, the duke of Sessa.
   Sessa sent copies in cipher to Madrid. They are with his despatches from 20 September 1593 (AGS, Estado,
   leg. 961) to 21 February 1594 (leg. 963). From December 1593 Frachetta also gave copies of two letters of
   Desportes to the Este agent Gilioli (Archivio di Stato di Modena, Ambasciatori Roma, 153). The four letters
   of 22 July are originals in a royalist collection, so it is possible that they were intercepted and that
   Frachetta did not get his. But if a duplicate went to Rome, a contemporary clear copy can be in these files.
   Baldini's fuller account is "Le guerre di religione francesi nella trattatistica italiana della ragion di
   Stato: Botero e Frachetta", *Il Pensiero politico* XXII (1989), pp. 301-324. I read none of these files.
2. **The sender.** Baldini names him Thibault Desportes, secretary of Mayenne, who was in Rome in 1590-91 and
   1592-93. The BnF catalogue and Tomokiyo write "Baudouin-Desportes". Use both names in searches of the
   printed literature.
3. **Acta Nuntiaturae Gallicae.** `cipher-lab` names this series (the Sega legation) as the edition to check
   and says that it could not open it. I did not confirm that a Sega volume exists.
4. **Bourdeau's own list** of places for the office's clear copies: Archivio Aldobrandini (Frascati) and the
   Vatican Fondo Borghese.

## 7. What I could not access

- Reddit (r/codes, r/cryptography): the JSON search gives HTTP 403, and the search tool refuses the domain.
- X/Twitter and LinkedIn: no search access. The general web search found nothing.
- cipherbrain.net: no connection. I searched the scienceblogs archive only.
- Cryptologia full texts (tandfonline gives HTTP 403). I checked titles and abstracts through web search.
- DECODE record attachments (login necessary). The public record list was fully searchable.
- Deleted issues 11 and 12 of `dbourdeau/cyphersolver`.
- prinzai.com.
- Exa search: rate limit after one query. Google Books API: daily quota used up. Gallica full-text search
  (SRU) does not do an exact phrase match, so its results prove nothing in either direction.
- Private channels: e-mail between Tomokiyo, Lasry, Bourdeau and others, and work that is not yet public.
  Tomokiyo's own notice says that his list is behind the solutions that he receives.
- Simancas, Modena, Baldini 1989 and the printed editions (section 6): outside this scope and not read.
