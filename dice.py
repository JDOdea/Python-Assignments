import random

print("\033[H\033[J")
human_player = input("Enter your name: ")
replaying = True

def main():
    computer_player = "CLU"
    human_wins = 0
    computer_wins = 0
    counter = 0

    print("\033[H\033[J")

    while counter < 5:
        human_roll = roll_die(20)
        computer_roll = roll_die(20)

        print("Round " + str(counter + 1))
        print(human_player + " rolled: " + str(human_roll))
        print(computer_player + " rolled: " + str(computer_roll))

        winner = determine_winner(human_player, human_roll, computer_player, computer_roll)
        if winner == "tie":
            print("Both " + human_player + " and " + computer_player + " wins!")
            human_wins += 1
            computer_wins += 1
        else:
            print(winner + " wins!")
            if winner == human_player:
                human_wins += 1
            elif winner == computer_player:
                computer_wins += 1
        print("\n")
        counter = counter + 1
    
    print(human_player + " wins: " + str(human_wins))
    print(computer_player + " wins: " + str(computer_wins))

    if human_wins > computer_wins:
        print("\nOverall winner: " + human_player + "\n")
    elif computer_wins > human_wins:
        print("\nOverall winner: " + computer_player + "\n")
    elif human_wins == computer_wins:
        print("\nOverall winner: EVERYONE!!\n")

    replay = input("Would you like to play again?(y/n)\n")
    global replaying
    if replay == "y":
        replaying = True
    else:
        replaying = False

def roll_die(max_value):
    die_roll = random.randint(1, max_value)
    return die_roll


def determine_winner(human_player, human_roll, computer_player, computer_roll):
    if human_roll > computer_roll:
        return human_player
    elif computer_roll > human_roll:
        return computer_player
    elif human_roll == computer_roll:
        return "tie"

while replaying == True:
    main()