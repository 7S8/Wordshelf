# Wordshelf

Upload a photo or screenshot of your English vocabulary list (handwriting works). Wordshelf reads every word and sorts it by CEFR level (A1–C2), with:

- a simple definition, part of speech and pronunciation
- two example sentences
- links to YouTube clips where people say the word (via YouGlish) and to YouTube lessons about it

## Reading modes

| Mode | Cost | Handwriting | Example sentences |
|---|---|---|---|
| **Gemini** (default) | Free key from [Google AI Studio](https://aistudio.google.com/apikey), no card | Yes | 2 for every word |
| **Qwen** | Free key from [OpenRouter](https://openrouter.ai/settings/keys); free models have daily limits | Yes | 2 for every word |
| **Claude account** | Your claude.ai account, no key: opens [Wordshelf on claude.ai](https://claude.ai/artifact/Jh8aBwWKWLGvDPcpPvPz4N), which runs on the visitor's own Claude plan | Yes | 2 for every word |
| **Claude API** | Paid Anthropic API key from [console.anthropic.com](https://console.anthropic.com/settings/keys) | Yes, most accurate | 2 for every word |
| **Basic** | No key at all | No, typed or printed text only | Only when the built-in dictionary has one |

Keys are stored only in your browser and sent only to that provider. The page picks the newest suitable model automatically (Gemini Flash, or the largest free Qwen vision model on OpenRouter).

**Basic mode** reads screenshots with Tesseract.js, takes the term before the dash on each line, keeps only real words, gets CEFR levels from the CEFR-J and Octanove word lists (estimating words that aren't listed), and uses a built-in copy of Open English WordNet for definitions.

Your word list is saved in your browser.

## Running locally

It's a single static file: open `index.html` in a browser, or serve the folder with any static server.

## Credits

- CEFR-J Wordlist Version 1.5, compiled by Yukio Tono, Tokyo University of Foreign Studies ([openlanguageprofiles/olp-en-cefrj](https://github.com/openlanguageprofiles/olp-en-cefrj)).
- Octanove Vocabulary Profile C1/C2 1.0 by Octanove Labs, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). `cefr-words.json` combines both lists and is shared under the same license.
- Definitions and examples from [Open English WordNet](https://en-word.net) ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)), based on Princeton WordNet ([WordNet License](https://wordnet.princeton.edu/license-and-commercial-use)). The files in `dict/` are derived from it. Word frequencies from [wordfreq](https://github.com/rspeer/wordfreq).
- Text recognition by [Tesseract.js](https://github.com/naptha/tesseract.js).
