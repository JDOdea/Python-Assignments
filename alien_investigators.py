team_options = [
    "Harvey (Physicist)",
    "Wendy (Has a really good flashlight)",
    "Andre (Owns the forest)",
    "Julie (Biologist)",
    "Cleetus (Self-proclaimed expert on things)",
    "Marlowe (Private Investigator)",
    "Brian (Talks to animals)",
    "Joan (Zealot)",
    "Winston (Agreed to be alien bait)",
    "Landrel (Anthropologist)",
    "Marvin (Photographer)",
    "Linda (Conspiracy Nut)"
]
team = []
leader = ""

#print introduction
print("\033[H\033[J")
print("There have reports of strange lights in the forest.")
print("The locals believe aliens have landed and are trying to recruit woodland creatures for their dastardly schemes.")
print("Your job is to assemble a team of investigators to check out the forest to find out what's really going on.")
print("---")
print()

#team selection
for option in team_options:
    
    #if team has at least one member
    if len(team) > 0:
        print("Team so far:")
        for member in team:
            print("  " + member)
    print()

    choice = input("Include '" + option + "'? (y/n) ")
    while choice!= "y" and choice != "n":
        choice = input("Please type 'y' or 'n' ")

    if choice == "y":
        #if no leader, ask for one
        if leader == "":
            leader_choice = input("Should they be team leader? (y/n)")
            while leader_choice != "y" and leader_choice != "n":
               leader_choice = input("Please type 'y' or 'n' ")
            if leader_choice == "y":
                leader = option
                team.append(option)
            else:
                team.append(option)
        else:
            team.append(option)

    # while choice!= "y" and "n":
    #     choice = input("Please type 'y' or 'n'")
        
    print("\033[H\033[J")


#print ending team roster
print("\033[H\033[J")
if len(team) > 0:
    #leader = team[0]
    team.remove(leader)
    print("Team Leader:\n  " + leader)
    print("\nAnd the rest of the team:")
    for member in team:
        print("  " + member)
    print()
else:
    print("You should really make a team...\nTRY AGAIN\n")