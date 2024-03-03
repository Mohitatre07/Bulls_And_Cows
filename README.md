# Bulls and Cows Game

This is a simple implementation of the Bulls and Cows game in Python. In this game, the player tries to guess a 4-digit number with no repeated digits. After each guess, the game provides feedback in terms of "bulls" and "cows," where a "bull" represents a correct digit in the correct position, and a "cow" represents a correct digit in the wrong position.

## How to Play

1. Run the Python script `bulls_and_cows.py`.
2. Enter the number of tries you want to have to guess the number (maximum 9).
3. Enter your guess, making sure it's a 4-digit number with no repeated digits.
4. After each guess, the game will provide feedback in terms of bulls and cows.
5. Keep guessing until you guess the correct number or run out of tries.

## Functions

- `generateNum()`: Generates a random 4-digit number with no repeated digits.
- `numOfBullsCows(num, guess)`: Calculates the number of bulls and cows for a given guess compared to the secret number.
- `getHint(num, guess)`: Generates a hint for the guess, showing which digits are correct and in the correct position.

## Restrictions

- The number of tries is limited to a maximum of 9.
- The player must enter a 4-digit number with no repeated digits as a guess.

## Continuation

After finishing the game (either by guessing the correct number or running out of tries), you will be prompted to play again. If you choose to continue, the game will start again; otherwise, it will end.
