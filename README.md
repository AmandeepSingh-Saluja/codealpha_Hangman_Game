# Hangman Game

## Overview

This repository contains a text-based Hangman game implemented in Python. The game randomly selects a word from a predefined list, and the player guesses one letter at a time to uncover the word. The player has a limited number of incorrect guesses allowed before the game ends.

## Game Rules

1. The game randomly selects a word from a predefined list.
2. The player guesses one letter at a time.
3. If the guessed letter is in the word, it is revealed in its correct position(s).
4. If the guessed letter is not in the word, the player loses a life.
5. The game ends when the player either guesses the word correctly or runs out of lives.

## How to Play

1. Run the game script.
2. Follow the prompts to guess letters.
3. Keep track of your incorrect guesses and remaining lives.
4. Try to guess the word before running out of lives!

## Requirements

- Python 3.x

## Usage

To play the game, run the following command in your terminal:

```bash
python hangman.py
```

## Example Gameplay

```
Welcome to Hangman!
The word has 5 letters.
You have 6 incorrect guesses remaining.
Guess a letter: a
Incorrect guess! You have 5 incorrect guesses remaining.
Current word: _ _ _ _ _
Guess a letter: e
Correct guess! Current word: _ _ e _ _
...
```
---

Feel free to modify the game and README as per your specific needs and preferences! Enjoy playing Hangman!
