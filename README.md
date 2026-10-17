# Wordshelf

Upload a photo, screenshot, PDF, Word (.docx, .doc), RTF, OpenDocument (.odt, .ods, .odp), Excel (.xlsx, .xls), CSV, PowerPoint (.pptx) or text file of your English vocabulary list (handwriting works in the AI modes). Wordshelf reads every word and sorts it by CEFR level (A1–C2), with:

- a simple definition, part of speech, and British and American pronunciation (IPA plus UK/US read-aloud buttons)
- two example sentences
- links to YouTube clips of British and American speakers saying the word (via YouGlish) and to YouTube lessons about it

## Reading modes

| Mode | Cost | Handwriting | Example sentences |
|---|---|---|---|
| **Gemini** (default) | Free key from [Google AI Studio](https://aistudio.google.com/apikey), no card | Yes | 2 for every word |
| **Qwen** | Free key from [OpenRouter](https://openrouter.ai/settings/keys); uses a free Qwen model, or another free vision model (Gemma, Llama, Mistral…) when no Qwen can read images; free models have daily limits | Yes | 2 for every word |
| **Claude account** | Your claude.ai account, no key: opens [Wordshelf on claude.ai](https://claude.ai/artifact/Jh8aBwWKWLGvDPcpPvPz4N), which runs on the visitor's own Claude plan | Yes | 2 for every word |
| **Claude API** | Paid Anthropic API key from [console.anthropic.com](https://console.anthropic.com/settings/keys) | Yes, most accurate | 2 for every word |
| **Basic** | No key at all | No, typed or printed text only | Only when the built-in dictionary has one |

Keys are stored only in your browser and sent only to that provider. The page picks the newest suitable model automatically (Gemini Flash, or the largest free Qwen vision model on OpenRouter).

**Basic mode** reads screenshots with Tesseract.js, takes the term before the dash on each line, keeps only real words, gets CEFR levels from the CEFR-J and Octanove word lists (estimating words that aren't listed), and uses a built-in copy of Open English WordNet for definitions, with example sentences from Tatoeba, Europarl and Project Gutenberg (about 90% of A1–B2 words have one).

Pick a theme from the **Theme** button: Automatic, Morning, Sunset, Night or Twilight. Each one changes the library scene at the top (sky, sun or moon, stars) and the page colors together.

Pick a language in **Translate to** (about 100 languages, defaults to your browser language) to see each word translated: by the AI when you have a Gemini, Qwen or Claude key, otherwise by the free [MyMemory](https://mymemory.translated.net) service (daily limit). Each card also links to Google Translate for the sentences.

Your word list is saved in your browser. Use **Print** to print (or save as PDF) all levels or only the ones you choose, with or without definitions, sentences, pronunciation and notes.

## Test yourself

Under the add-words panel: **Learn** (word for a meaning, gaps in your example sentences, translations; works without a key), **IELTS** (synonyms in context, paraphrase and gap-fill) and **GRE** (one- and two-blank text completion, sentence equivalence). IELTS and GRE questions are written by your AI (Gemini, Qwen, Claude) once per word and kept in your browser. Weak words come up first, and you can drill the ones you missed.

## Languages

- **Type words in Russian** (or another language): they are added in English (typos like doubled letters are fixed first), with the original kept as a note.
- **Site language:** the 🌐 button in the top bar. Built in: Russian, Ukrainian, Kazakh, Kyrgyz, Uzbek, Tajik, Turkish, Azerbaijani, German, French, Spanish, Italian, Portuguese, Arabic, Persian, Hindi, Chinese, Japanese, Korean and Indonesian. Any other language is translated once with your AI key and saved in your browser. Interface texts live in `i18n/` (`source.json` is the English list; check translations with `python3 tools/check-i18n.py`).

## Privacy

Visits are counted anonymously with [GoatCounter](https://www.goatcounter.com) (no cookies, no personal data). The site also counts how often scanning, adding words, translating and printing are used. Your words, notes and keys are never sent: they stay in your browser.

## Running locally

It's a single static file: open `index.html` in a browser, or serve the folder with any static server.

## Credits

- CEFR-J Wordlist Version 1.5, compiled by Yukio Tono, Tokyo University of Foreign Studies ([openlanguageprofiles/olp-en-cefrj](https://github.com/openlanguageprofiles/olp-en-cefrj)).
- Octanove Vocabulary Profile C1/C2 1.0 by Octanove Labs, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). `cefr-words.json` combines both lists and is shared under the same license.
- Definitions and examples from [Open English WordNet](https://en-word.net) ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)), based on Princeton WordNet ([WordNet License](https://wordnet.princeton.edu/license-and-commercial-use)). The files in `dict/` are derived from it. Word frequencies from [wordfreq](https://github.com/rspeer/wordfreq).
- Example sentences from [Tatoeba](https://tatoeba.org) ([CC BY 2.0 FR](https://creativecommons.org/licenses/by/2.0/fr/)), the [Europarl corpus](https://www.statmt.org/europarl/) and [Project Gutenberg](https://www.gutenberg.org) public-domain books.
- Documents are read in the browser with [pdf.js](https://mozilla.github.io/pdf.js/), [mammoth.js](https://github.com/mwilliamson/mammoth.js) and [SheetJS](https://sheetjs.com) (including its compound-file reader for .doc) and [JSZip](https://stuk.github.io/jszip/).
- Text recognition by [Tesseract.js](https://github.com/naptha/tesseract.js).

---

Created by Nuramatova Sakinat Ibnuabasovna. © 2026 Wordshelf. All rights reserved.
