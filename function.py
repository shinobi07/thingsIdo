import random

def guessinggame():
    print("""
    WELCOME TO OUR GUESSING GAME!!!!!\nWe will generate a random number in range 1000-3000 and your mission in this \ngame is to guess that random number.\nLET'S PLAY!
    """)
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
                print("This is not a number, you fool. Try again!")
                print("\n")
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


def hangman():
    print("""
    2 PLAYERS - 1 WILL GIVE US A WORD AND 1 WILL GUESS IT.
    IF THE GUESSER NEEDS MORE CLUES JUST TYPE 'more clues'.
    YOU ONLY HAVE 7 TURNS.
    GOOD LUCK!
    """)

    word = input("What word? > ")
    print('////////////\n'*100)
    answer = []
    for i in range(len(word)):
        if word[i] == " ":
            answer.append('  ')
        else:
            answer.append('-')

    def reveal(guess, answer, word):
        if len(guess) == 1:
            place = 0
            for i in range(len(word)):
                if guess == word[i]:
                    answer[i] = guess
                    place += 1
            if place > 0:
                return 'There is/are %s %s(s).' % (place, guess)
            else:
                return 'no letter available'
        elif len(guess) > 1:
            if guess == word:
                return 'Bingo!'
            else:
                return 'Try again!'

    print(" ".join(answer))
    suggestion = input("Any suggestions? > ")
    clues = []
    clues.append(suggestion)
    i = 1
    while i < 8:
        print("Turn %s:" % (i))
        print("Clue: %s characters, %s" % (len(word),", ".join(clues)))
        guess = input('Any ideas? > ')
        print(guess)
        if guess == 'more clues':
            suggestion = input("Any suggestions? > ")
            clues.append(suggestion)
        else:
            check = reveal(guess, answer, word)
            print(check)
            if check == 'Bingo!' or  '-' not in answer:
                print("YOU GOT GAME!")
                break
            print(" ".join(answer))
            i += 1
    else:
        print("You ran out of turns. DEFEAT!")
        print("The word is:",word)


def diceracing():
    print("")
    players = int(input("How many players?\n"))
    print("")
    number = int(input("What number do you want to be as the finish line?\n"))
    print("")
    results = {}
    for player in range(1,players+1):
        print("Let's see how lucky player %s is!" %(player))
        print("")
        turns = 1
        total = 0
        while True:
            b = input("Generate a random number from 1 -> 6 by pressing enter.")
            print("")
            randnum = random.randrange(1,7)
            print("This time's number is %s." % (randnum))
            total += randnum
            print("Your total is now %s." %(total))
            if total == number:
                print("")
                print("Player %s hit the finish line with %s turns." %(player,turns))
                results["player %s" %(player)] = turns
                break
            elif total > number:
                print("")
                print("You got over the number we need.")
                total -= random.randrange(1,7)
                print("Your total is now %s."%(total))
                if total == number:
                    print("")
                    print("Player %s hit the finish line with %s turns." %(player,turns))
                    results["player %s" %(player)] = turns
                    break
            turns += 1
            print("")
        print("")
    print(results)
    for key in results:
        if results[key] == min(list(results.values())):
            print("The winner is %s with %s turns!"%(key,results[key]))


def play():
    print("""
    WELCOME!
    WE HAVE 3 GAMES:
    * HANGMAN
    * GUESSING GAME
    * DICE RACING
    WHICH DO YOU WANT TO PLAY?
    """)
    choice = input()
    if choice.lower() == 'hangman':
        hangman()
    elif choice.lower() == 'guessing game':
        guessinggame()
    elif choice.lower() == 'dice racing':
        diceracing()
    else:
        print("Restart the program and just pick one to play mannn.")
