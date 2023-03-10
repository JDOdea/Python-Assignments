import time

car_0 = "   -           __"
car_1 = " --          ~( @\   \ "
car_2 = "---   _________]_[__/_>________"
car_3 = "     /  ____ \ <>     |  ____  \ "
car_4 = "    =\_/ __ \_\_______|_/ __ \__D"
car_5 = "________(--)_____________(--)____"

counter = 0

while counter < 40:
    print("\033[H\033[J")

    spaces = " " * counter
    print(spaces + car_0)
    print(spaces + car_1)
    print(spaces + car_2)
    print(spaces + car_3)
    print(spaces + car_4)
    print(spaces + car_5)

    counter = counter + 1
    time.sleep(.05)