# Wordshelf

Upload a photo or screenshot of your English vocabulary list (handwriting works). Wordshelf reads every word and sorts it by CEFR level (A1–C2), with:

- a simple definition, part of speech and pronunciation
- two example sentences
- links to YouTube clips where people say the word (via YouGlish) and to YouTube lessons about it

## Two reading modes

**Free (default, no account needed)**
- Reads the screenshot in your browser with Tesseract.js. This works well for typed or printed text and poorly for handwriting.
- Shows the words it found so you can fix mistakes before looking them up.
- Gets CEFR levels from the CEFR-J Wordlist and the Octanove C1/C2 list (about 8,800 words). Words that aren't on those lists go in a "Not on the CEFR list" group.
- Gets definitions, pronunciation and example sentences (when the dictionary has them) from the Free Dictionary API.

**Claude (most accurate)**
- Reads handwriting, phrasal verbs and translations written next to words, and writes two example sentences for every word.
- Needs an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/settings/keys). The key is stored only in your browser and is sent only to Anthropic.

Your word list is saved in your browser.

## Running locally

It's a single static file: open `index.html` in a browser, or serve the folder with any static server.

## Credits

- CEFR-J Wordlist Version 1.5, compiled by Yukio Tono, Tokyo University of Foreign Studies ([openlanguageprofiles/olp-en-cefrj](https://github.com/openlanguageprofiles/olp-en-cefrj)).
- Octanove Vocabulary Profile C1/C2 1.0 by Octanove Labs, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). `cefr-words.json` combines both lists and is shared under the same license.
- Definitions from [Free Dictionary API](https://dictionaryapi.dev), text recognition by [Tesseract.js](https://github.com/naptha/tesseract.js).
