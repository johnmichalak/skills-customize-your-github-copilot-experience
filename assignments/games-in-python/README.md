# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game while practicing Python strings, loops, conditionals, user input, and random selection. Your game will reveal correctly guessed letters and track incorrect guesses until the player wins or runs out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Use the word list in `starter-code.py` to choose a secret word and initialize the variables that track the game state.

#### Requirements
Completed program should:

- Randomly select one secret word from the predefined `words` list.
- Create a collection to store the letters the player has guessed.
- Track the number of incorrect guesses and define a maximum number allowed.

### 🛠️ Build the Guessing Loop

#### Description
Create the main game loop. On each turn, show the player's progress, ask for a letter, and update the game state based on the guess.

#### Requirements
Completed program should:

- Display each correctly guessed letter in its position and use an underscore for each hidden letter, such as `p _ t h _ n`.
- Prompt the player to enter one letter and handle guesses consistently regardless of capitalization.
- Add new guesses to the collection of guessed letters.
- Increase the incorrect-guess count only when the guessed letter is not in the secret word.
- Show the player how many incorrect guesses remain after each turn.

### 🛠️ Finish the Game

#### Description
End the loop when the player has revealed the complete secret word or used all allowed incorrect guesses, then clearly report the result.

#### Requirements
Completed program should:

- End with a winning message when every letter in the secret word has been guessed.
- End with a losing message when the player reaches the maximum number of incorrect guesses.
- Reveal the secret word when the game ends.
