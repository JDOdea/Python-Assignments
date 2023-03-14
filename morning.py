def wake_up():
    print("I'm waking up!")
    return "I'm awake now!!"

def get_out_of_bed():
    print("I'm getting out of bed!")
    return "I'm out of bed!!"

def brush_teeth(toothpaste):
    print("I'm brushing my teeth with " + toothpaste + "!")

def eat_breakfast(breakfast):
    print("I'm eating " + breakfast + " for breakfast!")

def get_dressed():
    clothes = input("What clothes will you wear?\n")
    shoes = input("What shoes will you wear?\n")
    return "I am wearing " + clothes + " and " + shoes + "!"

def main():
    awake = wake_up()
    print(awake)
    bed = get_out_of_bed()
    print(bed)

    toothpaste = input("What toothpaste will you use?\n")
    breakfast = input("What will you have for breakfast?\n")

    brush_teeth(toothpaste)
    eat_breakfast(breakfast)
    outfit = get_dressed()
    print(outfit)

main()