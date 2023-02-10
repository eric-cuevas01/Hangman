# Eric Cuevas, Andrew Molina
# February 9, 2023
# The program randomly selects a word from the dictionary and the user tries to guess it by guessing letters. Each incorrect guess will bring them closer to being "hanged."

from dictionary import words
import check_input
import random
import string


def display_gallows(num_incorrect):
  """Several print statements that display the game's gallows and add a body part for every incorrect guess by the player. Special characters (0, |, /, \) should form the shape of a hanging man once the player fails to guess the word."""
  if num_incorrect == 0:
    print("_________")
    print("|        |")
    print("|             ")
    print("|             ")
    print("|             ")
    print("|             ")
  elif num_incorrect == 1:
    print("_________")
    print("|        |")
    print("|        O")
    print("|             ")
    print("|             ")
    print("|             ")
  elif num_incorrect == 2:
    print("_________")
    print("|        |")
    print("|        O")
    print("|        |")
    print("|             ")
    print("|             ")
  elif num_incorrect == 3:
    print("_________")
    print("|        |")
    print("|        O")
    print("|       /|")
    print("|             ")
    print("|             ")
  elif num_incorrect == 4:
    print("_________")
    print("|        |")
    print("|        O")
    print("|       /|\\")
    print("|             ")
    print("|             ")
  elif num_incorrect == 5:
    print("_________")
    print("|        |")
    print("|        O")
    print("|       /|\\")
    print("|       /")
    print("|             ")
  else:
    print("_________")
    print("|        |")
    print("|        O")
    print("|       /|\\")
    print("|       / \\")
    print("|             ")


def display_correct(correct):
  print(" ".join(correct))


def display_incorrect(incorrect):
  incorrect.sort()
  print(" ".join(incorrect))


def display_letters_remaining(incorrect, correct):
  """Any remaining letters that have not been guessed by the player will be shown in a separate prompt. The player must choose from this set of letters."""
  letters = string.ascii_lowercase  # Prints the alphabet in uppercase
  remaining = [
    letter for letter in letters
    if letter not in incorrect and letter not in correct
  ]
  print(" ".join(remaining))


def play_hangman():
  """Chooses a word from dictionary at random. Creates an empty list to be filled with incorrect guesses by the player, if any. Displays the game's gallows and the player's guessed letters that were both correct and incorrect. If the player repeats a letter that has already been guessed, an error message will alert them."""
  word = random.choice(words).lower()
  incorrect = []
  correct = ["_" for _ in range(len(word))]
  num_incorrect = 0
  print("-Hangman-")
  print()

  while num_incorrect < 6 and "_" in correct:
    print("Incorrect selections: ", end="")
    display_incorrect(incorrect)
    print()
    display_gallows(num_incorrect)
    print("Correct guesses: ", end="")
    display_correct(correct)
    print()
    print("Letters remaining: ", end="")
    display_letters_remaining(incorrect, correct)
    print()

    guess = input("Enter a letter: ").lower()
    # guess = guess.upper()
    if guess in word and guess not in correct:
      for i in range(len(word)):
        if word[i] == guess:
          correct[i] = guess
    elif guess in incorrect:
      print("You already guessed that letter. Please guess another.")
      continue
    else:
      incorrect.append(guess)
      num_incorrect += 1

  if '_' not in correct and 0 <= num_incorrect <= 5:
    print('You win!')
    play_again = check_input.get_yes_no(
      "Would you like to play again? (Y/N): ")
    if play_again == True:
      play_hangman()
    elif play_again == False:
      print("Thank you for playing!")
  else:
    display_gallows(num_incorrect)
    play_again = check_input.get_yes_no(
      "GAME OVER! Would you like to play again? (Y/N): ")
    if play_again == True:
      play_hangman()
    elif play_again == False:
      print("Better luck next time.")


play_hangman()
