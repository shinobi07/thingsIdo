from function import play

play()
while True:
    a = input("Do you want to play again? y/n\n")
    print("\n")
    if a == '':
        print("Yo, give me an answer man!")
        print("\n")
    elif a == "y":
        play()
    else:
        input("press enter to exit")
        break
