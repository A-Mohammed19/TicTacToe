tiktaktoe_board = [
    ['X', 'O', 'O'],
    ['O',  'O', 'X'],
    ['X',  'O', 'X'],
]


if (tiktaktoe_board[0][0] == 'X'
        and tiktaktoe_board[0][1] == 'X'
        and tiktaktoe_board[0][2] == 'X'):
    print("X wins!")
# TODO: Handle the other cases
elif (tiktaktoe_board[0][0] == 'X'
        and tiktaktoe_board[1][0] == 'X'
        and tiktaktoe_board[2][0] == 'X'):
    print("X wins!")
elif (tiktaktoe_board[0][1] == 'X'
        and tiktaktoe_board[1][1] == 'X'
        and tiktaktoe_board[2][1] == 'X'):
    print("X wins!")
elif (tiktaktoe_board[1][0] == 'X'
        and tiktaktoe_board[1][1] == 'X'
        and tiktaktoe_board[1][2] == 'X'):
    print("X wins!")

elif (tiktaktoe_board[0][2] == 'X'
        and tiktaktoe_board[1][2] == 'X'
        and tiktaktoe_board[2][2] == 'X'):
    print("X wins!")

elif (tiktaktoe_board[2][0] == 'X'
        and tiktaktoe_board[2][1] == 'X'
        and tiktaktoe_board[2][2] == 'X'):
    print("X wins!")
elif (tiktaktoe_board[2][0] == 'X'
        and tiktaktoe_board[1][1] == 'X'
        and tiktaktoe_board[0][2] == 'X'):
    print("X wins!")
elif (tiktaktoe_board[0][0] == 'X'
        and tiktaktoe_board[1][1] == 'X'
        and tiktaktoe_board[2][2] == 'X'):
    print("X wins!")
    
elif (tiktaktoe_board[0][0] == 'O'
            and tiktaktoe_board[0][1] == 'O'
            and tiktaktoe_board[0][2] == 'O'):
        print("O wins!")
elif (tiktaktoe_board[0][0] == 'O'
        and tiktaktoe_board[1][0] == 'O'
        and tiktaktoe_board[2][0] == 'O'):
    print("O wins!")
elif (tiktaktoe_board[0][1] == 'O'
        and tiktaktoe_board[1][1] == 'O'
        and tiktaktoe_board[2][1] == 'O'):
    print("O wins!")
elif (tiktaktoe_board[1][0] == 'O'
        and tiktaktoe_board[1][1] == 'O'
        and tiktaktoe_board[1][2] == 'O'):
    print("O wins!")

elif (tiktaktoe_board[0][2] == 'O'
        and tiktaktoe_board[1][2] == 'O'
        and tiktaktoe_board[2][2] == 'O'):
    print("O wins!")

elif (tiktaktoe_board[2][0] == 'O'
        and tiktaktoe_board[2][1] == 'O'
        and tiktaktoe_board[2][2] == 'O'):
    print("O wins!")
elif (tiktaktoe_board[2][0] == 'O'
        and tiktaktoe_board[1][1] == 'O'
        and tiktaktoe_board[0][2] == 'O'):
    print("O wins!")
elif (tiktaktoe_board[0][0] == 'O'
        and tiktaktoe_board[1][1] == 'O'
        and tiktaktoe_board[2][2] == 'O'):
    print("O wins!")


else:
    print("No winner")
