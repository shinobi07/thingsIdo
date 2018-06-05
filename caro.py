board = [["0"]*5 for i in range(5)]
print("Here is the board for our game today.\n")
for row in board:
    print("\t" + " ".join(row))
    print("")
p1 = input("Player 1, x or o? ")
if p1 == "x":
    p2 = "o"
    print("Then player 2 will go with %s." % (p2))
elif p1 == "o":
    p2 = "x"
    print("Then player 2 will go with %s." % (p2))
else:
    print("By default, Player 1 will go with x and Player 2 with o.")
    p1 = "x"
    p2 = "o"

def check(player,board):
    if player == 'x':
        for row in range(len(board)):
            if board[row] == ['x','x','x','x','x']:
                return True
                break
            else:
                check = []
                for i in board:
                    for col in range(len(i)):
                        if i[col] == 'x':
                            check.append(col)
                if check == [0,1,2,3,4] or check == [4,3,2,1,0]:
                    return True
                    break
    elif player == 'o':
        for row in range(len(board)):
            if board[row] == ['o','o','o','o','o']:
                return True
                break
            else:
                check = []
                for i in board:
                    for col in range(len(i)):
                        if i[col] == 'o':
                            check.append(col)
                if check == [0,1,2,3,4] or check == [4,3,2,1,0]:
                    return True
                    break
    return False

i = 1
while True:
    place1 = list(map(int, input("Player 1, where do you want to go? <row> <column> ").split()))
    if board[place1[0]-1][place1[1]-1] != p1 and board[place1[0]-1][place1[1]-1] != p2:
        board[place1[0]-1][place1[1]-1] = p1
    else:
        print("Another place, please!")
        place1 = list(map(int, input("Player 1, where do you want to go? <row> <column> ").split()))
        board[place1[0]-1][place1[1]-1] = p1
    for row in board:
        print("\t" + " ".join(row))
        print("")
    place2 = list(map(int, input("Player 2, where do you want to go? <row> <column> ").split()))
    if  board[place2[0]-1][place2[1]-1] != p2 and board[place2[0]-1][place2[1]-1] != p1:
        board[place2[0]-1][place2[1]-1] = p2
    else:
        print("Another place, please!")
        place2 = list(map(int, input("Player 2, where do you want to go? <row> <column> ").split()))
        board[place2[0]-1][place2[1]-1] = p2
    for row in board:
        print("\t" + " ".join(row))
        print("")
    if i == 5:
        if check(p1,board):
            print("Player 1 won!")
            break
        elif check(p2,board):
            print("Player 2 won!")
            break
        else:
            continue
    i += 1
