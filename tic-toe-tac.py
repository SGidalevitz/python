import random
board = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]]
a = board[0]
b = board[1]
c = board[2]
player = random.randrange(1,3)
computer = (3 - player)
def game():
    turn(player)
    computer()
def place(xy, row, col):
    board[row][col] = xy

def turn(xy):
    move = input("Where would you like to move?")
    rowcol = move.split(",")
    for x in rowcol:
        rowcol[rowcol.index(x)] = int(x)
    place(xy, rowcol[0], rowcol[1])
def computer():
    moves = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                moves.append((x, y))
    print(moves)
    #place(computer, moves[random.randrange(0,8)])
    #place(computer, )


turn(1)
computer()




print(a)
print(b)
print(c)
#print("\u0332|".join((a)))
#print("\u0332|".join((b)))
#print("\u0332|".join((c)))