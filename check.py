board = [[0,0,0],
                [0,0,1],
                [0,0,0]]
possiblemoves = [(0,1),(0,2),(1,1),(1,2)]
movevalues = []


winseq = []
def wincheck(symbol, predict):
    if wincheck_row(symbol, predict) or wincheck_column(symbol, predict) or wincheck_diag_1(symbol, predict) or wincheck_diag_2(symbol, predict):
        return True
    else:
        return False
def wincheck_row(symbol, predict):
    global winseq
    if predict:
        boardno = board_predict
    else:
        boardno = board
    #Checks whether the wincheck is a normal wincheck or tied to the computer algo
    for i in range(3):
        if (boardno[i][0] == boardno[i][1] == boardno[i][2]) and (boardno[i][0] == symbol):
            winseq = [(i, 0), (i, 1), (i, 2)]
            return True
def wincheck_column(symbol, predict):
    global winseq
    if predict:
        boardno = board_predict
    else:
        boardno = board
    #Checks whether the wincheck is a normal wincheck or tied to the computer algo
    for i in range(3):    
        if (boardno[0][i] == boardno[1][i] == boardno[2][i]) and (boardno[0][i] == symbol):
            winseq = [(0, i), (1, i), (2, i)]
            return True
def wincheck_diag_1(symbol, predict):
    global winseq
    if predict:
        boardno = board_predict
    else:
        boardno = board
    #Checks whether the wincheck is a normal wincheck or tied to the computer algo
    if (boardno[0][0] == boardno[1][1] == boardno[2][2]) and (boardno[0][0] == symbol):
        winseq = [(0, 0), (1, 1), (2, 2)]
        return True
def wincheck_diag_2(symbol, predict):
    global winseq
    if predict:
        boardno = board_predict
    else:
        boardno = board
    #Checks whether the wincheck is a normal wincheck or tied to the computer algo
    if (boardno[2][0] == boardno[1][1] == boardno[0][2]) and (boardno[2][0] == symbol):
        winseq = [(2, 0), (1, 1), (0, 2)]
        return True
for x in possiblemoves:
    print(x)
    board_predict = board.copy()
    board_predict[1][1] = 2
    if wincheck(2, True):
        #if the predicted board is winning then it has a higher value than if it isn't
        movevalues.append(1)
    else:
        movevalues.append(0)
    board_predict.clear()
    pos = possiblemoves[movevalues.index(max(movevalues))]
pos = possiblemoves[movevalues.index(max(movevalues))]