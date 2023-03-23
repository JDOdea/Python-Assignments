import sys
import random


def select_difficulty():

    print("\033[H\033[J", end="")

    difficulty_options = {
        0 : "Cheater", 
        1: "Easy",
        2: "Normal",
        3: "Hard",
        4: "Ridiculous",
    }

    print("Enter a difficulty:\n")
    print("-" * 12)
    print("Cheater\n\nEasy\n\nNormal\n\nHard\n\nRidiculous")
    print("-" * 12)
    difficulty_choice = input("\n> ")

    if difficulty_choice == "cheater" or difficulty_choice == "Cheater" or difficulty_choice == "CHEATER":
        difficulty = difficulty_options[0]
    elif difficulty_choice == "easy" or difficulty_choice == "Easy" or difficulty_choice == "EASY":
        difficulty = difficulty_options[1]
    elif difficulty_choice == "normal" or difficulty_choice == "Normal" or difficulty_choice == "NORMAL":
        difficulty = difficulty_options[2]
    elif difficulty_choice == "hard" or difficulty_choice == "Hard" or difficulty_choice == "HARD":
        difficulty = difficulty_options[3]
    elif difficulty_choice == "ridiculous" or difficulty_choice == "Ridiculous" or difficulty_choice == "RIDICULOUS":
        difficulty = difficulty_options[4]
    else:
        difficulty = difficulty_options[random.randint(0, 4)]

    return difficulty


def pick_secret_word():
    """
    Pick a secret word from a list of possible words.

    Returns:
    A string representing the secret word.
    """

    #region Easy Words
    easy_file = open("easy_words.txt")
    easy_text = easy_file.read()
    easy_words = easy_text.splitlines()
    easy_file.close()
    #endregion

    #region Animal Names
    animal_file = open("animals.txt")
    animal_text = animal_file.read()
    animal_words = animal_text.splitlines()
    animal_file.close()
    #endregion

    #region Fruit Names
    fruit_file = open("fruits.txt")
    fruit_text = fruit_file.read()
    fruit_words = fruit_text.splitlines()
    fruit_file.close()
    #endregion

    #region Hard Words
    hard_file = open("hard_words.txt")
    hard_text = hard_file.read()
    hard_words = hard_text.splitlines()
    hard_file.close()
    #endregion

    secret_word_options = []

    if len(sys.argv) == 1:
        for word in easy_words:
            secret_word_options.append(word)
    else:

        if sys.argv[1] == 'easy_words.txt':
            for word in easy_words:
                secret_word_options.append(word)
        elif sys.argv[1] == 'animals.txt':
            for word in animal_words:
                secret_word_options.append(word)
        elif sys.argv[1] == 'fruits.txt':
            for word in fruit_words:
                secret_word_options.append(word)
        elif sys.argv[1] == 'hard_words.txt':
            for word in hard_words:
                secret_word_options.append(word)



    word = random.choice(secret_word_options)
    return word


def print_clothesline(incorrect_count):
    """
    Print a clothesline based on the number of incorrect guesses.

    Returns:
    A string representing the clothesline.
    """

    clothesline = print("")

    if incorrect_count == 0:
        clothesline = color_message(r"""
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````


""", "green")
        

    elif incorrect_count == 1:
        clothesline = color_message(r"""
=====!=====!=======!=====!=======!=====!=======!===========
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|


""", "green")
        

    elif incorrect_count == 2:
        clothesline = color_message(r"""
=====!=====!=======!=====!=======!=====!===================
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
                                            _.~.,_.._
                                             ```````
""", "green")
        

    elif incorrect_count == 3:
        clothesline = color_message(r"""
=====!=====!=======!=====!=======!=========================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
                                            _.~.,_.._
                                             ```````
""", "yellow")
        

    elif incorrect_count == 4:
        clothesline = color_message(r"""
=====!=====!=======!=====!=================================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
""", "yellow")
        

    elif incorrect_count == 5:
        clothesline = color_message(r"""
=====!=====!=======!=======================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
""", "yellow")
        

    elif incorrect_count == 6:
        clothesline = color_message(r"""
=====!=====!===============================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
""", "red")
        

    elif incorrect_count == 7:
        clothesline = color_message(r"""
=====!=====================================================
    /'\
   /   .\
   '|  ='
    |   |
    |   |
    `-._|
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
""", "red")
        

    elif incorrect_count == 8:
        clothesline = color_message(r"""
===========================================================






  _.~.,_.._     _.~.,_.._     _.~.,_.._     _.~.,_.._
   ```````       ```````       ```````       ```````
""", "red")
    
    return clothesline


def is_letter_in_word(letter, word):
    """
    Determine if the letter is in the secret word.

    Returns:
    A boolean indicating whether the letter is in the word.
    """

    if letter in word:
        return True
    else:
        return False


def update_guess(old_guess, letter, secret_word):
    """
    Update the guess with the new letter.

    Returns:
    A string representing the updated guess.
    """

    if letter in secret_word:

        new_guess = ""
        for index in range(len(old_guess)):
            if secret_word[index] == letter:
                new_guess = new_guess + letter
            else:
                new_guess = new_guess + old_guess[index]

        return new_guess


def print_game_ui(difficulty, incorrect_count, guess, letters_guessed):
    """
    Print game UI
    """
    
    clear_screen()

    print(difficulty)
    if difficulty == "Cheater":
        incorrect_count = 4
    if incorrect_count < 4:
        print(print_clothesline(0))
    else:
        print(print_clothesline(incorrect_count - 4))
    print("")


    print("Word:    " + guess)
    print("Guesses: " + ' '.join(letters_guessed))
    print("")


def color_message(msg, color):
    """
    Add color to the message.

    Returns:
    A string representing the colored message.
    """

    if color == "red":
        return("\033[0;30;41m" + msg + "\033[0;0m")
    
    elif color == "yellow":
        return("\033[0;30;43m" + msg + "\033[0;0m")
    
    elif color == "green":
        return("\033[0;30;42m" + msg + "\033[0;0m")


def clear_screen():
    """
    Clear the screen.
    """

    print("\033[H\033[J", end="")





def main():
    """
    The main function for running the game.
    """


    """Choose difficulty"""
    difficulty = select_difficulty()


    #region Variables
    
    """Select random secret letter"""
    secret_letter = chr(random.randint(ord("a"), ord("z")))
    secret_letter_guessed = False

    """Select secret word and get its length"""
    secret_word = pick_secret_word()
    secret_word_length = len(secret_word)

    guess = ("-" * secret_word_length)
    letters_guessed = []
    incorrect_max = 12

    if difficulty == "Cheater":
        incorrect_count = 0
        incorrect_max = 100
    elif difficulty == "Easy":
        incorrect_count = 0
    elif difficulty == "Normal":
        incorrect_count = 4
    elif difficulty == "Hard":
        incorrect_count = 8
    elif difficulty == "Ridiculous":
        incorrect_count = 11
    
    #endregion
    
    #region Main Loop

    """While player has guesses left"""
    while incorrect_count < incorrect_max and guess != secret_word:
        
        if secret_letter_guessed == True:
            
            incorrect_count -= 1
            print_game_ui(difficulty, incorrect_count, guess, letters_guessed)
            print(color_message("Secret letter found! +1 Guess", "green"))
            secret_letter_guessed = False
        else:
            print_game_ui(difficulty, incorrect_count, guess, letters_guessed)

        print("Guess a letter... if you dare!")
        letter = input("> ")


        """Accepting only first letter if multiple entered"""
        if len(letter) > 1:
            letter = letter[0]
        

        """Determine if letter is secret letter"""
        if letter == secret_letter:
            secret_letter_guessed = True

            """Color secret letter depending on if in secret word"""
            if secret_letter in range(len(secret_word)):
                secret_letter = color_message(secret_letter, "green")
            else:
                secret_letter = color_message(secret_letter, "red")


        
        """Determine if guess is correct or not"""
        is_correct = is_letter_in_word(letter, secret_word)


        if is_correct == True:

            guess = update_guess(guess, letter, secret_word)

            letter = color_message(letter, "green")

            if letter not in (letters_guessed):

                letters_guessed.append(letter)

        else: 

            letter = color_message(letter, "red")

            if letter not in (letters_guessed):

                letters_guessed.append(letter)

                if secret_letter_guessed == False:
                    incorrect_count += 1
       
    #endregion      
        
    #region Endgame
    if guess == secret_word:

        print_game_ui(difficulty, incorrect_count, guess, letters_guessed)

        print("The word was " + secret_word)
        print("")
        outcome = color_message("You win!!", "green")
        print(outcome + "\n")
    
    if incorrect_count == 12:

        print_game_ui(difficulty, incorrect_count, guess, letters_guessed)

        print("The word was " + secret_word)
        print("")
        outcome = color_message("You lose...", "red")
        print(outcome + "\n")
    #endregion



main()
