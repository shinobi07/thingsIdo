import random
def guessinggame():
    print("""WELCOME TO OUR GUESSING GAME!!!!!\nWe will generate a random number in range 1000-3000 and your mission in this \ngame is to guess that random number.\nLET'S PLAY!""")
    print("")
    b = str(random.randint(1000, 3000)) # or str(random.choice(range(1000,3000))) or random.randrange(1000,3000)
    c = []
    tries = int(input("How many tries do you want?\n"))
    print('')
    if tries == 0:
        print("Then why do you wanna play anyway? FUCK YOU MAN!")
        print("\n")
    else:
        k = tries
        while True:
            a = input("Input a 4-digit number. You have " + str(k) + " shot(s) left.\n")
            print('')
            k -= 1
            if not a.isdigit():
                print("This is not a number, you fool!")
                print("\n")
                break
            elif len(a) != 4:
                print('4 digits are enough!\n')
            elif a[0] == "0":
                print("Don't they teach you Maths at school? Try again my man!")
                print("\n")
            else:
                c.append(a)
                i = 0
                hit = 0
                miss = 0
                while True:
                    if i == 4:
                        break
                    else:
                        if a[i] == b[i]:
                            hit += 1
                        else:
                            miss += 1
                    i += 1
                if hit < 4:
                    if len(c) == tries or k == 0:
                        print("hit: " + str(hit) + "\nmiss: " + str(miss))
                        print("\n")
                        print("You ran out of tries!")
                        print("The number is " + b)
                        print("\n")
                        break
                    elif len(c) < tries:
                        print("hit: " + str(hit) + "\nmiss: " + str(miss))
                        print("\n")
                elif hit == 4:
                    print("""
                    BULLSEYE!!!!!
                    YOU ARE THE WINNER!!!!!
                    CONGRATULATIONS!!!!!
                    """)
                    break
guessinggame()
while True:
    a = input("Do you want to play again? y/n\n")
    print("\n")
    if a == '':
        print("Yo, give me an answer man!")
        print("\n")
    elif a == "y":
        guessinggame()
    else:
        input("press enter to exit")
        break
