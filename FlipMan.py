import random
from words import *

# leave the number choices as strings to avoid type errors
def get_word(): 
    category = input("Choose a category (1. Super Heroes, 2. Theme Parks, 3. Types of Ghosts): ")
    if category =="1":
        word = random.choice(super_heroes)
    elif category == "2":
        word = random.choice(theme_parks)
    elif category == "3":
        word = random.choice(ghost_types)
    else:
        print("Invalid category chosen. Please choose a valid category.")
        return get_word()
    return word.upper()



def play(word):
    word_completion = "_" * len(word) #adds the amount of underscores depending on the length og the word
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("A Deranged man has entered your home and demands you guess the word he is thinking or he will flip your brand new table.")
    print(display_hangman(tries))
    print(word_completion)
    print("\n") # add a space after each attempt
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("uh-oh, You've already guessed the letter", guess)
            elif guess not in word:
                print("Yikes! ", guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                 print(f"Phew!, {guess} is in the word!") #had to use functional notation here due to error I was only getting on this line
                 guessed_letters.append(guess)
                 word_as_list = list(word_completion)
                 indices = [i for i, letter in enumerate(word) if letter == guess]
                 for index in indices:
                    word_as_list[index] = guess
                 word_completion = "".join(word_as_list)
                 if "_" not in word_completion:
                    guessed = True    
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print("Ahh!", guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("You guessed the word! Your table is safe!")
    else:
        print("Oh NO, you ran out of tries. Your new table is ruined. The word was " + word + ", time to go to Ikea.")

def display_hangman(tries):
    if tries == 6:
        return "(ಠ_ಠ)"
    elif tries == 5:
        return "(╯"
    elif tries == 4:
        return "(╯°"
    elif tries == 3:
        return "(╯°□°"
    elif tries == 2:
        return "(╯°□°)"
    elif tries == 1:
        return "(╯°□°)╯︵"
    else:
        return "(╯°□°)╯︵ ┻━┻"
 # return the appropriate hangman art based on the number of tries remaining


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()