#tictactoe using dictinary to store board state

theBoard = {
            '1' : ' ','2' : ' ','3' : ' ',
            '4' : ' ','5' : ' ','6' : ' ',
            '7' : ' ','8' : ' ','9' : ' ',
                       
}

def _printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'] )
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'] )
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'] )

turn = 'X'

for i in range(9):
    print('Turn of ' + turn + '. Enter which space')
    space = input()
    theBoard[space] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'   

_printBoard(theBoard)       
