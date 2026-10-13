=====================================
        HANGMAN GAME (PYTHON)
=====================================

DESCRIPTION
-----------
A simple command-line Hangman game written in Python. You enter a list of
words, the program randomly picks one, and you try to guess it one letter
at a time before you run out of wrong guesses.


REQUIREMENTS
------------
- Python 3.x
- No external libraries needed (uses only the built-in "random" module)


HOW TO RUN
----------
1. Open a terminal or command prompt.
2. Go to the folder containing the file.
3. Run:

       python hangman_code.py

   (On some systems use "python3 hangman_code.py")


HOW TO PLAY
-----------
1. When the program starts, type several words separated by spaces and
   press Enter.
   Example:  apple banana mango orange

2. The program randomly selects one word from your list.
3. The word is shown as underscores, for example:  _ _ _ _ _
4. Type one letter at a time and press Enter.
5. If the letter is in the word, it is revealed in all its positions.
6. If the letter is not in the word, your wrong guess count increases.
7. You win by revealing every letter of the word.
8. You lose after 6 wrong guesses.


GAME RULES
----------
- Maximum wrong guesses allowed: 6
- Input is converted to lowercase automatically.
- Guessing a letter you already tried shows a message and does NOT count
  as a wrong guess.


SAMPLE RUN
----------
Input words:
    cat dog bird

Word:  _ _ _
Wrong Guesses:  0 / 6
Guess a letter: a
Correct Guess
Word:  _ a _
Wrong Guesses:  0 / 6
Guess a letter: z
Wrong Guess
...
You Won
The Word is :  cat


NOTES
-----
- Enter the words in lowercase for the best results, since your guesses
  are converted to lowercase before checking.
- Enter only one letter per guess.
- The word list is typed in at the start, so you can customise the game
  every time you play.


POSSIBLE IMPROVEMENTS
---------------------
- Add ASCII hangman drawings for each wrong guess.
- Validate input so only single alphabetic letters are accepted.
- Convert the entered words to lowercase automatically.
- Add a "play again" option.
- Load words from a text file.


FILE LIST
---------
- hangman_code.py   : Main game source code
- README.txt        : This documentation file


=====================================
