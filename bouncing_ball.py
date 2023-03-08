import time # We will cover "import" later in the course

############################################################
# This section contains the "frames" for the animation
############################################################

frame_0 = """
+---------------------+
|O                    |
|                     |
|                     |
|                     |
|                     |
+---------------------+
"""

frame_1 = """
+---------------------+
|                     |
| O                   |
|                     |
|                     |
|                     |
+---------------------+
"""

frame_2 = """
+---------------------+
|                     |
|                     |
|  O                  |
|                     |
|                     |
+---------------------+
"""

frame_3 = """
+---------------------+
|                     |
|                     |
|                     |
|   O                 |
|                     |
+---------------------+
"""

frame_4 = """
+---------------------+
|                     |
|                     |
|                     |
|                     |
|    o                |
+---------------------+
"""

frame_5 = """
+---------------------+
|                     |
|                     |
|                     |
|     O               |
|                     |
+---------------------+
"""

frame_6 = """
+---------------------+
|                     |
|                     |
|      O              |
|                     |
|                     |
+---------------------+
"""

frame_7 = """
+---------------------+
|                     |
|       O             |
|                     |
|                     |
|                     |
+---------------------+
"""

frame_8 = """
+---------------------+
|                     |
|                     |
|        O            |
|                     |
|                     |
+---------------------+
"""

frame_9 = """
+---------------------+
|                     |
|                     |
|                     |
|         O           |
|                     |
+---------------------+
"""

frame_10 = """
+---------------------+
|                     |
|                     |
|                     |
|                     |
|          o          |
+---------------------+
"""

frame_11 = """
+---------------------+
|                     |
|                     |
|                     |
|           O         |
|                     |
+---------------------+
"""

frame_12 = """
+---------------------+
|                     |
|                     |
|            O        |
|                     |
|                     |
+---------------------+
"""

frame_13 = """
+---------------------+
|                     |
|                     |
|                     |
|             O       |
|                     |
+---------------------+
"""

frame_14 = """
+---------------------+
|                     |
|                     |
|                     |
|                     |
|              o      |
+---------------------+
"""

frame_15 = """
+---------------------+
|                     |
|                     |
|                     |
|               O     |
|                     |
+---------------------+
"""

frame_16 = """
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                o    |
+---------------------+
"""

frame_17 = """
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                  o  |
+---------------------+
"""

frame_18 = """
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                   o |
+---------------------+
"""

frame_19 = """
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                   _ |
+---------------------+
"""

############################################################
# This section contains the code to create the animation 
############################################################

#print("Follow the bouncing ball...")
startFrameStr = input("What frame, from 1 to 20, should the ball start on?\n")
startFrameInt = int(startFrameStr) - 1

#counter = 0
counter = startFrameInt
while counter < 20:
    # This incantation will clear the terminal
    # You should NOT try to understand it... I don't :)
    print("\033[H\033[J")

    print("Follow the bouncing ball...")

    if counter == 0:
        print(frame_0)
    elif counter == 1:
        print(frame_1)
    elif counter == 2:
        print(frame_2)
    elif counter == 3:
        print(frame_3)
    elif counter == 4:
        print(frame_4)
    #Original
    #elif 5 == counter:
    elif counter == 5:
        print(frame_5)
    elif counter == 6:
        print(frame_6)
    elif counter == 7:
        print(frame_7)
    #Original
    #elif counter == 9:
    elif counter == 8:
        print(frame_8)
    elif counter == 9:
        print(frame_9)
    #Original
    #elif counter == 9:
    elif counter == 10:
        print(frame_10)
    #Original
    #elif counter == 9:
    elif counter == 11:
        print(frame_11)
    elif counter == 12:
        print(frame_12)
    elif counter == 13:
        print(frame_13)
    elif counter == 14:
        print(frame_14)
    elif counter == 15:
        print(frame_15)
    elif counter == 16:
        print(frame_16)
    elif counter == 17:
        print(frame_17)
    elif counter == 18:
        print(frame_18)
    elif counter == 19:
        print(frame_19)

    counter = counter + 1

    # Make the program pause for "x" seconds
    #x = 1.1
    x = 0.1
    time.sleep(x)

    if counter == 20:
        print("\033[H\033[J")
