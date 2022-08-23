import artwork
import words

# Importing the random word
chosen_word = words.random_word
# Creating an empty list to fill in with '_' for display purposes
display = []
# Saving the word's length
word_lenght = len(chosen_word)
# Setting lives to a constant
lives = 6

# Filling in the display
for _ in chosen_word:
    display.append('_')

# Checking whether we exit the game by finding the word or by losing all out lives
while display.count('_') and lives > 0:

    # Ask user for a letter
    guess = input("Choose a letter: ")

    # Inform user that he had chosen the same letter
    # WE DON'T PENALIZE THE USER
    if guess in display:
        print(f"You already guessed '{guess}'.")

    # Else if the guess is different we check it's validity
    else:
        for i in range(word_lenght):
            if chosen_word[i] == guess:
                display[i] = guess

        # If the guess was incorrect PENALIZE the user with the subtraction of 1 life
        if guess not in display:
            lives -= 1
    
    # Display the appropriate stage of the hangman & the word progress
    print(artwork.stages[lives])
    print(display)

# If we still have lives it is the completion of the word that ended the while loop
if lives:
    print("You won.")
else:
    print(f"You lose. The word was {chosen_word}.")


