#we neeed to write a function which would validate a chess board
#the chess board is represented as a dictionary
#the keys would be the positions on the board
#the values would be the pieces on those positions  

def validate_chess_board(board):
    #check if there is only one king for each player
    white_king = 0
    black_king = 0

    for piece in board.values():
        if piece == "white_king":
            white_king += 1
        elif piece == "black_king":
            black_king += 1

    if white_king != 1 or black_king != 1:
        return False

    #check if there are no more than 16 pieces for each player
    white_pieces = 0
    black_pieces = 0

    for piece in board.values():
        if piece.startswith("white_"):
            white_pieces += 1
        elif piece.startswith("black_"):
            black_pieces += 1

    if white_pieces > 16 or black_pieces > 16:
        return False

    #check if pawns are not on the first or last row
    for position, piece in board.items():
        if piece.endswith("pawn"):
            row = int(position[1])
            if row == 1 or row == 8:
                return False

    return True

board = {
    "a1": "white_rook",
    "b1": "white_knight",
    "c1": "white_bishop",
    "d1": "white_queen",
    "e1": "white_king",
    "f1": "white_bishop",
    "g1": "white_knight",
    "h1": "white_rook",
    "a2": "white_pawn",
    "b2": "white_pawn",
    "c2": "white_pawn",
    "d2": "white_pawn",
    "e2": "white_pawn",
    "f2": "white_pawn",
    "g2": "white_pawn",
    "h2": "white_pawn",
    "a7": "black_pawn",
    "b7": "black_pawn",
    "c7": "black_pawn",
    "d7": "black_pawn",
    "e7": "black_pawn",
    "f7": "black_pawn",
    "g7": "black_pawn",
    "h7": "black_pawn",
    "a8": "black_rook",
    "b8": "black_knight",   
    "c8": "black_bishop",
    "d8": "black_queen",
    "e8": "black_king",
    "f8": "black_bishop",
    "g8": "black_knight",
    "h8": "black_rook"
}

print(validate_chess_board(board))  #should return True



