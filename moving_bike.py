import time

bike1_0 = "        __o"
bike1_1 = "    _`\<,_"
bike1_2 = "    (-)/ (-)"

bike2_0 = "        __o"
bike2_1 = "    _`\<,_"
bike2_2 = "    (+) L(+)"

counter = 0
pedal = ("up")

while counter < 40:
    print("\033[H\033[J")
    spaces = " " * counter
    if pedal == "up":
        print(spaces + bike1_0)
        print(spaces + bike1_1)
        print(spaces + bike1_2)
        pedal = "down"
    else:
        print(spaces + bike2_0)
        print(spaces + bike2_1)
        print(spaces + bike2_2)
        pedal = "up"
    

    counter = counter + 1
    time.sleep(.15)