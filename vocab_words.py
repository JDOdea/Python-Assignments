import time

print("\nVOCABULARY WORDS")
print("----------------")
print("\nPlease enter four word/definition pairs.\n")

word_0 = input("Type in your first word: ")
while word_0 == "":
    word_0 = input("Please type in a word: ")
definition_0 = input("Now type in its definition: ")
while definition_0 == "":
    definition_0 = input("Please type in a definition: ")

word_1 = input("Type in your second word: ")
while word_1 == "":
    word_1 = input("Please type in a word: ")
definition_1 = input("Now type in its definition: ")
while definition_1 == "":
    definition_1 = input("Please type in a definition: ")

word_2 = input("Type in your third word: ")
while word_2 == "":
    word_2 = input("Please type in a word: ")
definition_2 = input("Now type in its definition: ")
while definition_2 == "":
    definition_2 = input("Please type in a definition: ")

word_3 = input("Type in your final word: ")
while word_3 == "":
    word_3 = input("Please type in a word: ")
definition_3 = input("Now type in its definition: ")
while definition_3 == "":
    definition_3 = input("Please type in a definition: ")


print("\033[H\033[J")

keep_going = "yes"

while keep_going == "yes":
    if word_0 != "":
        input("Define '" + word_0 + "': ")
        if definition_0 != "":
            print("The definition is: " + definition_0 + "\n")
        else:
            print("-- No definition found --\n")

    if word_1 != "":
        input("Define '" + word_1 + "': ")
        if definition_1 != "":
            print("The definition is: " + definition_1 + "\n")
        else:
            print("-- No definition found --\n")

    if word_2 != "":
        input("Define '" + word_2 + "': ")
        if definition_2 != "":
            print("The definition is: " + definition_2 + "\n")
        else:
            print("-- No definition found --\n")

    if word_3 != "":
        input("Define '" + word_3 + "': ")
        if definition_3 != "":
            print("The definition is: " + definition_3 + "\n")
        else:
            print("-- No definition found --\n")

    hold = 2
    time.sleep(hold)
    print("\033[H\033[J")

    print("\nYour words are:\n")
    print(word_0 + ": " + definition_0 + "\n")
    print(word_1 + ": " + definition_1 + "\n")
    print(word_2 + ": " + definition_2 + "\n")
    print(word_3 + ": " + definition_3 + "\n")

    keep_going = input("Would you like to continue? (yes/no)\n")


