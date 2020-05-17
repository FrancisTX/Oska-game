import copy

def oskaplayer(board, turn, steps_ahead):
    return 0

def movegen(board, turn):
    possible_states = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == turn:
                states = move(board, row, col)
                for element in states:
                    if element not in possible_states:
                        possible_states.append(element)
    return possible_states

def can_move(board, row, col):
    return 0

def move(board, row, col):
    possbile_move = []
    first_row_space = len(board[0])
    if board[row][col] == 'w':
        #move forward on the diagonal
        #check the chess's position at the 0 or the end
        if row < len(board)/2:
            if col == 0:
                if board[row+1][0] == '-':
                    new_board = copy.deepcopy(board)
                    temp_next_row = list(new_board[row+1])
                    temp_this_row = list(new_board[row])
                    temp_next_row[0] = 'w'
                    temp_this_row[col] = '-'
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
            if col == first_row_space - (row + 1):
                if board[row+1][len(board[row+1]) - 1] == '-':
                    new_board = copy.deepcopy(board)
                    temp_next_row = list(new_board[row+1])
                    temp_this_row = list(new_board[row])
                    temp_next_row[len(board[row+1]) - 1] = 'w'
                    temp_this_row[col] = '-'
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)

            if row < len(board)/2 - 1:
                print("Hey")
                if col == 0 and board[row+1][col] == 'b':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row+1])
                    temp_next_next_row = list(new_board[row+2])
                    temp_this_row[col] = '-'
                    temp_next_row[col] = '-'
                    temp_next_next_row[col] = 'w'
                    new_board[row+2] = ''.join(temp_next_next_row)
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if col == first_row_space - (row + 1) and board[row+1][col - 1] == 'b':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row+1])
                    temp_next_next_row = list(new_board[row+2])
                    temp_this_row[col] = '-'
                    temp_next_row[col-1] = '-'
                    temp_next_next_row[col-2] = 'w'
                    new_board[row+2] = ''.join(temp_next_next_row)
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if col != 0 and col != first_row_space - (row + 1) :
                    if board[row+1][col - 1] == 'b': 
                        if (col - 1) != 0:
                            new_board = copy.deepcopy(board)
                            temp_this_row = list(new_board[row])
                            temp_next_row = list(new_board[row+1])
                            temp_next_next_row = list(new_board[row+2])
                            temp_this_row[col] = '-'
                            temp_next_row[col-1] = '-'
                            temp_next_next_row[col-2] = 'w'
                            new_board[row+2] = ''.join(temp_next_next_row)
                            new_board[row+1] = ''.join(temp_next_row)
                            new_board[row] = ''.join(temp_this_row)
                            possbile_move.append(new_board)

                    if board[row+1][col] == 'b' :
                        if col != first_row_space - (row+2):
                            new_board = copy.deepcopy(board)
                            temp_this_row = list(new_board[row])
                            temp_next_row = list(new_board[row+1])
                            temp_next_next_row = list(new_board[row+2])
                            temp_this_row[col] = '-'
                            temp_next_row[col] = '-'
                            temp_next_next_row[col] = 'w'
                            new_board[row+2] = ''.join(temp_next_next_row)
                            new_board[row+1] = ''.join(temp_next_row)
                            new_board[row] = ''.join(temp_this_row)
                            possbile_move.append(new_board)
            if row == len(board)/2 - 1:
                if col == 0 and board[row+1][0] == 'b':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row+1])
                    temp_next_next_row = list(new_board[row+2])
                    temp_this_row[col] = '-'
                    temp_next_row[col] = '-'
                    temp_next_next_row[col+1] = 'w'
                    new_board[row+2] = ''.join(temp_next_next_row)
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if col == 1:
                    if board[row+1][0] == 'b':
                        new_board = copy.deepcopy(board)
                        temp_this_row = list(new_board[row])
                        temp_next_row = list(new_board[row+1])
                        temp_next_next_row = list(new_board[row+2])
                        temp_this_row[col] = '-'
                        temp_next_row[col-1] = '-'
                        temp_next_next_row[col-1] = 'w'
                        new_board[row+2] = ''.join(temp_next_next_row)
                        new_board[row+1] = ''.join(temp_next_row)
                        new_board[row] = ''.join(temp_this_row)
                        possbile_move.append(new_board)
                    if board[row+1][1] == 'b':
                        new_board = copy.deepcopy(board)
                        temp_this_row = list(new_board[row])
                        temp_next_row = list(new_board[row+1])
                        temp_next_next_row = list(new_board[row+2])
                        temp_this_row[col] = '-'
                        temp_next_row[col] = '-'
                        temp_next_next_row[col+1] = 'w'
                        new_board[row+2] = ''.join(temp_next_next_row)
                        new_board[row+1] = ''.join(temp_next_row)
                        new_board[row] = ''.join(temp_this_row)
                        possbile_move.append(new_board)
                if col == 2 and board[row+1][1] == 'b':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row+1])
                    temp_next_next_row = list(new_board[row+2])
                    temp_this_row[col] = '-'
                    temp_next_row[col-1] = '-'
                    temp_next_next_row[col-1] = 'w'
                    new_board[row+2] = ''.join(temp_next_next_row)
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)

            if col != 0 and col != first_row_space - (row + 1):
                if board[row+1][col] == '-':
                    new_board = copy.deepcopy(board)
                    temp_next_row = list(new_board[row+1])
                    temp_this_row = list(new_board[row])
                    temp_next_row[col] ='w'
                    temp_this_row[col] = '-'
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if board[row+1][col-1] == '-':
                    new_board = copy.deepcopy(board)
                    temp_next_row = list(new_board[row+1])
                    temp_this_row = list(new_board[row])
                    temp_next_row[col-1] = 'w'
                    temp_this_row[col] = '-'
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)

        elif row >= len(board)/2 and row != 2 * first_row_space - 4:
            if board[row+1][col] == '-':
                new_board = copy.deepcopy(board)
                temp_next_row = list(new_board[row+1])
                temp_this_row = list(new_board[row])
                temp_next_row[col] = 'w'
                temp_this_row[col] = '-'
                new_board[row+1] = ''.join(temp_next_row)
                new_board[row] = ''.join(temp_this_row)
                possbile_move.append(new_board)
            if board[row+1][col+1] == '-':
                new_board = copy.deepcopy(board)
                temp_next_row = list(new_board[row+1])
                temp_this_row = list(new_board[row])
                temp_next_row[col+1] = 'w'
                temp_this_row[col] = '-'
                new_board[row+1] = ''.join(temp_next_row)
                new_board[row] = ''.join(temp_this_row)
                possbile_move.append(new_board)
            if row < 2 * first_row_space - 5:
                if board[row+1][col] == 'b': 
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row+1])
                    temp_next_next_row = list(new_board[row+2])
                    temp_this_row[col] = '-'
                    temp_next_row[col] = '-'
                    temp_next_next_row[col] = 'w'
                    new_board[row+2] = ''.join(temp_next_next_row)
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if board[row+1][col+1] == 'b':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row+1])
                    temp_next_next_row = list(new_board[row+2])
                    temp_this_row[col] = '-'
                    temp_next_row[col+1] = '-'
                    temp_next_next_row[col+2] = 'w'
                    new_board[row+2] = ''.join(temp_next_next_row)
                    new_board[row+1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)    
    
    if board[row][col] == 'b':
        #move forward on the diagonal
        #check the chess's position at the 0 or the end
        if row > len(board)/2:
            if col == 0:
                if board[row-1][0] == '-':
                    new_board = copy.deepcopy(board)
                    temp_next_row = list(new_board[row-1])
                    temp_this_row = list(new_board[row])
                    temp_next_row[0] = 'b'
                    temp_this_row[col] = '-'
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
            if col == len(board[row]) - 1:
                if board[row-1][len(board[row-1]) - 1] == '-':
                    new_board = copy.deepcopy(board)
                    temp_next_row = list(new_board[row-1])
                    temp_this_row = list(new_board[row])
                    temp_next_row[len(board[row-1]) - 1] = 'b'
                    temp_this_row[col] = '-'
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
    

            if row > len(board)/2 + 1:
                print("Hey")
                if col == 0 and board[row-1][col] == 'w':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row-1])
                    temp_next_next_row = list(new_board[row-2])
                    temp_this_row[col] = '-'
                    temp_next_row[col] = '-'
                    temp_next_next_row[col] = 'b'
                    new_board[row-2] = ''.join(temp_next_next_row)
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if col == len(board[row]) - 1 and board[row - 1][col - 1] == 'w':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row-1])
                    temp_next_next_row = list(new_board[row-2])
                    temp_this_row[col] = '-'
                    temp_next_row[col-1] = '-'
                    temp_next_next_row[col-2] = 'b'
                    new_board[row-2] = ''.join(temp_next_next_row)
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if col != len(board[row]) - 1 and col != 0:
                    if board[row-1][col - 1] == 'w': 
                        if (col - 1) != 0:
                            new_board = copy.deepcopy(board)
                            temp_this_row = list(new_board[row])
                            temp_next_row = list(new_board[row-1])
                            temp_next_next_row = list(new_board[row-2])
                            temp_this_row[col] = '-'
                            temp_next_row[col-1] = '-'
                            temp_next_next_row[col-2] = 'b'
                            new_board[row-2] = ''.join(temp_next_next_row)
                            new_board[row-1] = ''.join(temp_next_row)
                            new_board[row] = ''.join(temp_this_row)
                            possbile_move.append(new_board)

                    if board[row-1][col] == 'w' :
                        if col != len(board[row-1]) - 1:
                            new_board = copy.deepcopy(board)
                            temp_this_row = list(new_board[row])
                            temp_next_row = list(new_board[row-1])
                            temp_next_next_row = list(new_board[row-2])
                            temp_this_row[col] = '-'
                            temp_next_row[col] = '-'
                            temp_next_next_row[col] = 'b'
                            new_board[row-2] = ''.join(temp_next_next_row)
                            new_board[row-1] = ''.join(temp_next_row)
                            new_board[row] = ''.join(temp_this_row)
                            possbile_move.append(new_board)
    

            if row == len(board)/2 + 1:
                if col == 0 and board[row-1][0] == 'w':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row-1])
                    temp_next_next_row = list(new_board[row-2])
                    temp_this_row[col] = '-'
                    temp_next_row[col] = '-'
                    temp_next_next_row[col+1] = 'b'
                    new_board[row-2] = ''.join(temp_next_next_row)
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if col == 1:
                    if board[row-1][0] == 'w':
                        new_board = copy.deepcopy(board)
                        temp_this_row = list(new_board[row])
                        temp_next_row = list(new_board[row-1])
                        temp_next_next_row = list(new_board[row-2])
                        temp_this_row[col] = '-'
                        temp_next_row[col-1] = '-'
                        temp_next_next_row[col-1] = 'b'
                        new_board[row-2] = ''.join(temp_next_next_row)
                        new_board[row-1] = ''.join(temp_next_row)
                        new_board[row] = ''.join(temp_this_row)
                        possbile_move.append(new_board)
                    if board[row-1][1] == 'w':
                        new_board = copy.deepcopy(board)
                        temp_this_row = list(new_board[row])
                        temp_next_row = list(new_board[row-1])
                        temp_next_next_row = list(new_board[row-2])
                        temp_this_row[col] = '-'
                        temp_next_row[col] = '-'
                        temp_next_next_row[col+1] = 'b'
                        new_board[row-2] = ''.join(temp_next_next_row)
                        new_board[row-1] = ''.join(temp_next_row)
                        new_board[row] = ''.join(temp_this_row)
                        possbile_move.append(new_board)
                if col == 2 and board[row-1][1] == 'w':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row-1])
                    temp_next_next_row = list(new_board[row-2])
                    temp_this_row[col] = '-'
                    temp_next_row[col-1] = '-'
                    temp_next_next_row[col-1] = 'b'
                    new_board[row-2] = ''.join(temp_next_next_row)
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)

    
            if col != 0 and col != len(board[row]) - 1:
                if board[row-1][col] == '-':
                    new_board = copy.deepcopy(board)
                    temp_next_row = list(new_board[row-1])
                    temp_this_row = list(new_board[row])
                    temp_next_row[col] ='b'
                    temp_this_row[col] = '-'
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if board[row-1][col-1] == '-':
                    new_board = copy.deepcopy(board)
                    temp_next_row = list(new_board[row-1])
                    temp_this_row = list(new_board[row])
                    temp_next_row[col-1] = 'b'
                    temp_this_row[col] = '-'
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
    
        
        elif row <= len(board)/2 + 1 and row != 0:
            if board[row-1][col] == '-':
                new_board = copy.deepcopy(board)
                temp_next_row = list(new_board[row-1])
                temp_this_row = list(new_board[row])
                temp_next_row[col] = 'b'
                temp_this_row[col] = '-'
                new_board[row-1] = ''.join(temp_next_row)
                new_board[row] = ''.join(temp_this_row)
                possbile_move.append(new_board)
            if board[row-1][col+1] == '-':
                new_board = copy.deepcopy(board)
                temp_next_row = list(new_board[row-1])
                temp_this_row = list(new_board[row])
                temp_next_row[col+1] = 'b'
                temp_this_row[col] = '-'
                new_board[row-1] = ''.join(temp_next_row)
                new_board[row] = ''.join(temp_this_row)
                possbile_move.append(new_board)
            if row > 1:
                if board[row-1][col] == 'w': 
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row-1])
                    temp_next_next_row = list(new_board[row-2])
                    temp_this_row[col] = '-'
                    temp_next_row[col] = '-'
                    temp_next_next_row[col] = 'b'
                    new_board[row-2] = ''.join(temp_next_next_row)
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
                if board[row-1][col+1] == 'w':
                    new_board = copy.deepcopy(board)
                    temp_this_row = list(new_board[row])
                    temp_next_row = list(new_board[row-1])
                    temp_next_next_row = list(new_board[row-2])
                    temp_this_row[col] = '-'
                    temp_next_row[col+1] = '-'
                    temp_next_next_row[col+2] = 'b'
                    new_board[row-2] = ''.join(temp_next_next_row)
                    new_board[row-1] = ''.join(temp_next_row)
                    new_board[row] = ''.join(temp_this_row)
                    possbile_move.append(new_board)
    return possbile_move





print(movegen(['-----','----', '---', 'ww', 'bbb', '----', '-----'], 'w'))