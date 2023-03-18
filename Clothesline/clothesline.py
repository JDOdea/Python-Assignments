import random

def main():

    secret_word = pick_secret_word()
    secret_word_length = len(secret_word)
    guess = ("-" * secret_word_length)
    incorrect_count = 0
    letters_guessed = []
    
    
    while incorrect_count < 8 and guess != secret_word:

        clear_screen()

        print_clothesline(incorrect_count)
        print("")

        print("Word:    " + guess)
        #print("Guesses: " + str(letters_guessed))
        print("Guesses: " + ' '.join(letters_guessed))
        print("")

        print("Guess a letter... if you dare!")
        letter = input("> ")
        if len(letter) > 1:
            letter = letter[0]
        letters_guessed.append(letter)

        is_correct = is_letter_in_word(letter, secret_word)

        if is_correct == True:
            guess = update_guess(guess, letter, secret_word)
        else:
            incorrect_count += 1

    if guess == secret_word:
        clear_screen()

        print_clothesline(incorrect_count)
        print("")

        print("Word:    " + guess)
        print("Guesses: " + ' '.join(letters_guessed))
        print("")
        print("The word was " + secret_word)
        print("")
        print("You win!!")
    
    if incorrect_count == 8:
        clear_screen()

        print_clothesline(incorrect_count)
        print("")

        print("Word:    " + guess)
        print("Guesses: " + ' '.join(letters_guessed))
        print("")
        print("The word was " + secret_word)
        print("")
        print("You lose...")


def pick_secret_word():
    easy_file = open("easy_words.txt")
    easy_text = easy_file.read()
    easy_words = easy_text.splitlines()
    easy_file.close()

    animal_file = open("animals.txt")
    animal_text = animal_file.read()
    animal_words = animal_text.splitlines()
    animal_file.close()

    fruit_file = open("fruits.txt")
    fruit_text = fruit_file.read()
    fruit_words = fruit_text.splitlines()
    fruit_file.close()

    hard_file = open("hard_words.txt")
    hard_text = hard_file.read()
    hard_words = hard_text.splitlines()
    hard_file.close()

    secret_word_options = []

    for word in easy_words:
        secret_word_options.append(word)

    for word in animal_words:
        secret_word_options.append(word)

    for word in fruit_words:
        secret_word_options.append(word)

    for word in hard_words:
        secret_word_options.append(word)

    word = random.choice(secret_word_options)
    return word
    

    #FIRST TRY
    # easy_words = open("easy_words.txt")
    # lines = easy_words.readlines()

    # secret_word_options = []
    # for line in lines:
    #     line = line.replace("\n", "")
    #     secret_word_options.append(line)

    # random_secret_word = random.choice(secret_word_options)
    # return random_secret_word


def print_clothesline(incorrect_count):
    clothesline = print("")

    if incorrect_count == 0:
        clothesline = r"""
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````


"""
    elif incorrect_count == 1:
        clothesline = r"""
=====!=====!=======!=====!=======!=====!=======!===========
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|


"""
    elif incorrect_count == 2:
        clothesline = r"""
=====!=====!=======!=====!=======!=====!===================
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
                                            _.~.,_.._
                                             ```````
"""
    elif incorrect_count == 3:
        clothesline = r"""
=====!=====!=======!=====!=======!=========================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
                                            _.~.,_.._
                                             ```````
"""
    elif incorrect_count == 4:
        clothesline = r"""
=====!=====!=======!=====!=================================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""
    elif incorrect_count == 5:
        clothesline = r"""
=====!=====!=======!=======================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""
    elif incorrect_count == 6:
        clothesline = r"""
=====!=====!===============================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""
    elif incorrect_count == 7:
        clothesline = r"""
=====!=====================================================
    /'\
   /   .\
   '|  ='
    |   |
    |   |
    `-._|
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""
    elif incorrect_count == 8:
        clothesline = r"""
===========================================================






  _.~.,_.._     _.~.,_.._     _.~.,_.._     _.~.,_.._
   ```````       ```````       ```````       ```````
"""
    
    print(clothesline)
    return clothesline


def is_letter_in_word(letter, word):
    if letter in word:
        return True
    else:
        return False


def update_guess(old_guess, letter, secret_word):

    if letter in secret_word:

        new_guess = ""
        for index in range(len(old_guess)):
            if secret_word[index] == letter:
                new_guess = new_guess + letter
            else:
                new_guess = new_guess + old_guess[index]

        return new_guess
        #FIRST TRY
        # word_list = list(secret_word)
        # guess_list = list(old_guess)

        # for letter_index in range(len(word_list)):
        #     character = word_list[letter_index]

        #     if character == letter:
        #         guess_list[letter_index] = letter
        #         return str(guess_list)


def clear_screen():
    print("\033[H\033[J", end="")



main()