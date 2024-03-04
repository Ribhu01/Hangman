# Hangman game
Hangman Game

This is a simple implementation of the classic Hangman game in Python.

Description:

This Hangman game allows players to guess letters to uncover a hidden word. The player starts with a certain number of lives, and they lose a life for each incorrect guess. The game ends when the player either correctly guesses the word or runs out of lives.

Usage:
-Clone or download the repository containing the game files.
-Run the hangman.py file using the Python interpreter.
-Follow the on-screen instructions to guess letters and play the game.

 Features:

-Random selection of words from a predefined list.
-Interactive gameplay with user input for letter guesses.
-Visual representation of Hangman stages using ASCII art.
-Clearing the screen after each guess for a better user experience.

How to Play:

-Upon starting the game, a hidden word is chosen from the word list.
-The player is presented with blanks representing each letter of the word.
-The player guesses letters one at a time.
-If the guessed letter is in the word, it is revealed in its correct position(s).
-If the guessed letter is not in the word, the player loses a life.
-The game continues until the player either correctly guesses the word or runs out of lives.

 Credits:

ascii_images.py: Contains ASCII art representations of Hangman stages.
words.py: Provides a list of words for the game to choose from.
