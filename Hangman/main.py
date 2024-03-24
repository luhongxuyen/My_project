import random
from hangman_words import word_list as w
from hangman_acsii_art import stages as s
from hangman_acsii_art import logo
import os

def clear():
    os.system('cls')

def hangman_game(word_list: list, stages: list, lives= 6):
  chosen_word = random.choice(word_list)

  length = len(chosen_word)

  display = ["_" for _ in range(length)]

  print(f"{stages[lives]}")

  print(f"({''.join(display)})\n")
  
  while lives > 0:
      try:
        guess = input("Guess a letter: ").lower()
        
        clear()   
        
        if guess in display:
            clear()
            already_in = f"You've already guessed '{guess}'. Try something else...\n"
        else:
            already_in = ""

        for i in range(length):
            if guess == chosen_word[i]:
                display[i] = guess

        print(f"{stages[lives]}\n{already_in}({''.join(display)})\n")
        
        if guess not in chosen_word:
            clear()
            lives -= 1
            print(f"{stages[lives]}\nYou guessed '{guess}', that's not in the word. You lose a life!\n({''.join(display)})\n")
        
        if "_" not in display:
            print("You won the game!")
            break
        
        if lives == 0:
              print("You lose.")
          
      except ValueError:
          print("Something went wrong!")
          break

def main():
    print(logo)
    hangman_game(w, s)

if __name__ == "__main__":
    main()