# Random Word Maker

A tiny PyQt5 desktop app that displays three random words from a built-in list when you click the corresponding buttons.

## What it is

This repository contains a minimal PyQt5 application (`main.py`) that shows three placeholder labels and three buttons. Clicking a button picks a random word from an internal `word_list` and displays it in the matching label. It's useful as a learning example for PyQt5 layouts, signals/slots, and simple GUI wiring.

## Prerequisites

- Python 3.8+ (tested on Python 3.10/3.11)
- PyQt5

The project also includes a `requirements.txt` listing pinned dependency versions used while developing.

## Install

It's recommended to use a virtual environment. From the project root:

```bash
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
# .venv\Scripts\activate    # Windows (PowerShell/CMD)
pip install -r requirements.txt
```

If you don't want to use a venv you can install dependencies globally with `pip install -r requirements.txt`.

## Run

From the project root (with the virtualenv activated if you used one):

```bash
python main.py
```

The app will open a small window titled "Random Word Maker". Click any of the three "Click me" buttons to populate the corresponding label with a randomly selected word from the built-in list.

## Files

- `main.py` — the PyQt5 application source.
- `requirements.txt` — pinned Python dependencies used for development.

## Usage notes

- The words are chosen from an internal list (`word_list`) in `main.py`. Several words appear multiple times in the list by design or oversight — you can edit the list to add/remove words or to de-duplicate entries.
- The UI is intentionally minimal and unstyled. Styling (fonts, colors) can be added using Qt stylesheets.

## Future improvements

Some ideas (also listed as comments in `main.py`):

- Add a feature to combine the three words into a phrase.
- Allow users to add their own words or load word lists from files.
- Save generated words to a history file.
- Add styling and theming (dark mode) and keyboard shortcuts.
