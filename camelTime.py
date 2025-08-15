import random


print("Welcome to Camel.")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.\n\n")

done = False
milesTraveled = 0
thirst = 0
camelFatigue = 0
natives = -40
drinks = 3
oasis = random.randrange(20)

input("Press ENTER to start.")

while not done:
    print("\n\n")
    print("What's your next move, cowboy?")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print(" ")
    choice = input("> ")
    if choice.upper() == "Q":
        done = True
    elif choice.upper() == "E":
        print("Miles traveled: " + str(milesTraveled))
        print("Drinks in canteen: " + str(drinks))
        print("The natives are " + str(abs(natives)) + " miles behind you.")
    elif choice.upper() == "D":
        camelFatigue = 0
        print("The camel is pleased.")
        natives += random.randrange(6, 9)
    elif choice.upper() == "C":
        milesTraveled += random.randrange(10, 25)
        thirst += 1
        camelFatigue += random.randrange(1, 4)
        print("You traveled " + str(milesTraveled) + " miles.")
        natives += random.randrange(1, 5)
    elif choice.upper() == "B":
        milesTraveled += random.randrange(5, 13)
        thirst += 1
        camelFatigue += 1
        print("You traveled " + str(milesTraveled) + " miles.")
        natives += random.randrange(3, 7)
    elif choice.upper() == "A":
        if drinks > 0:
            drinks -= 1
            thirst = 0
        else:
            print("Yer canteen's empty, fella!")
    else:
        print("Now hold on here, pardner, ya gotta do something!")
    if oasis > 5 and oasis < 15:
        print("You stumble into an oasis and take a not-so-well-earned rest.")
        print("You rest the camel, whet your whistle, and refill your canteen.")
        print("Looks like ya managed to lose yer pursuers... for now.")
        camelFatigue = 0
        drinks = 3
        thirst = 0
        natives = -40
        oasis = random.randrange(20)
    if thirst > 6 and not done:
        print("Dagnabbit! You ain't drank enough wodder, yer dead!")
        done = True
    elif thirst > 4 and thirst <= 6 and not done:
        print("Yer mighty thirsty there, friend.")
    if camelFatigue > 8 and not done:
        print("You murderer!! This camel done died because of yer carelessness!")
        done = True
    elif camelFatigue > 5 and camelFatigue <= 8 and not done:
        print("Yer camel ain't lookin' too good.")
    if natives >= 0 and not done:
        print(
            "Hot dog!! Them folks caught up to ya and they're takin' their camel, and\n sending you to meet your maker!"
        )
        done = True
    elif natives > -15 and natives < 0 and not done:
        print("Watch out, them fellers are closin' in on ya!")
    if milesTraveled >= 200 and not done:
        print(
            "Hooooooey!!! You made it, camel'n all! Now get outta here 'fore you \ncause more trouble!"
        )
        done = True
    if done:
        print("You wanna turn  back the clock and give it another try? (Y/N)")
        choice = input("> ")
        if choice.upper() == "Y":
            done = False
        else:
            print("See ya next time!")
