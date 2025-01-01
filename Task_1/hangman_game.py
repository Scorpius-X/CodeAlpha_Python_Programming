# Design a text-based Hangman game. The program selects a random word, and the player guesses one,
# letter at a time to uncover the word. You can set a limit on the number of incorrect guesses allowed.
import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_game = False
lives_left = 5

display = []

for _ in range(word_length):
    display += "_"

print("Welcome to the Hangman game")

# print(f"chosen word is : {chosen_word}")

while not end_game:

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid input.")
    
    
    if guess in display:
        print(f"You have already guessed the letter {guess} .")

    
    if guess in chosen_word:
        for position in range(word_length):
            right_letter = chosen_word[position]
            if right_letter == guess:
                display[position] = right_letter
    
    
    if guess not in chosen_word:
        lives_left -= 1
        print(f"The letter {guess} you guess is not in the word ")
        print(f"You have {lives_left} lives left.")
        if lives_left == 0:
            print(f"You lose!, the correct word is {chosen_word}.")
            break
    
    
    print(f"{' '.join(display)}")
    print("\n")

    if "_" not in display:
        end_game = True
        print(f"you win!, the correct word is {chosen_word}")
    
    

    

    

    
    




