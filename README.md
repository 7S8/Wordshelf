# Wordshelf

Upload a photo or screenshot of your English vocabulary list (handwriting works). Wordshelf reads every word and sorts it by CEFR level (A1–C2), with:

- a simple definition, part of speech and pronunciation
- two example sentences
- links to YouTube clips where people say the word (via YouGlish) and to YouTube lessons about it

## Two reading modes

**Free (default, no account needed)**
- Reads the screenshot in your browser with Tesseract.js. This works for typed or printed text only, not handwriting.
- Takes the term before the dash on each line ("word - meaning"), keeps only real words, fixes small misreadings, and lets you edit the list before looking it up.
- Gets CEFR levels from the CEFR-J Wordlist and the Octanove C1/C2 list. Words not on those lists get an estimated level (C1 or C2, from how common the word is). Phrases are rated by their hardest word.
- Gets definitions, pronunciation and example sentences from a built-in copy of Open English WordNet, so lookups are instant and don't depend on other websites. Many words have no example sentence.

**Claude (most accurate)**
- Reads handwriting, phrasal verbs and translations written next to words, and writes two example sentences for every word.
- Needs an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/settings/keys). The key is stored only in your browser and is sent only to Anthropic.

Your word list is saved in your browser.

## Running locally

It's a single static file: open `index.html` in a browser, or serve the folder with any static server.

## Credits

- CEFR-J Wordlist Version 1.5, compiled by Yukio Tono, Tokyo University of Foreign Studies ([openlanguageprofiles/olp-en-cefrj](https://github.com/openlanguageprofiles/olp-en-cefrj)).
- Octanove Vocabulary Profile C1/C2 1.0 by Octanove Labs, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). `cefr-words.json` combines both lists and is shared under the same license.
- Definitions and examples from [Open English WordNet](https://en-word.net) ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)), based on Princeton WordNet ([WordNet License](https://wordnet.princeton.edu/license-and-commercial-use)). The files in `dict/` are derived from it. Word frequencies from [wordfreq](https://github.com/rspeer/wordfreq).
- Text recognition by [Tesseract.js](https://github.com/naptha/tesseract.js).
