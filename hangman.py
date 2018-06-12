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
