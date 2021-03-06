import copy
import math

def oskaplayer(board, turn, steps_ahead):
    if turn == 'b':
        player = 1
    else:
        player = 0
    
    val,board =  minimax(steps_ahead, board, player, 0)
    return board

def minimax(steps_ahead, board, turn, depth):
    if depth == steps_ahead:
        return static_eval(board),board

    ## white's turn, choose MAX
    if turn%2 == 0:
        states = movegen(board, 'w')
        max_val = float('-inf') 
        #go through all possible move
        for elements in states:
            #if win, return immediately
            if static_eval(elements) ==  len(board[0]):
                return static_eval(elements), elements
            val, board = minimax(steps_ahead, elements, turn+1, depth + 1)
            #if val is bigger, update the max_val and the board
            if val >= max_val:
                final_board = elements
                max_val = val
        return max_val,final_board

    ## black's turn, choose min
    else:
        states = movegen(board, 'b')
        min_val = float('inf')
        #go thourgh all possible moves
        for elements in states:
            if static_eval(elements) ==  -len(board[0]):
                return static_eval(elements), elements
            val,board = minimax(steps_ahead, elements, turn+1, depth + 1)
            #update
            if val <= min_val:
                final_board = elements
                min_val = val
        return min_val,final_board

##static evaluation:
##if w wins, return len(board[0])
##if b wims, return -len(board[0])
##if tie, return 0
##else retuen number_white - number_black
def static_eval(board):
    num_black = 0
    num_white = 0
    num_black_first_row = 0
    num_white_last_row = 0
    score = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'b':
                num_black += 1
                if row == 0:
                    num_black_first_row += 1
            if board[row][col] == 'w':
                num_white += 1
                if row == len(board)-1:
                    num_white_last_row += 1

    if num_white == 0:
        score = -(len(board[0]))
    elif num_black == 0:
        score = len(board[0])
    elif num_black == num_white and num_black_first_row == num_white_last_row and num_white == num_black_first_row and num_black == num_white_last_row:
        score = 0
    elif num_black != 0 and num_black == num_black_first_row:
        score += -(len(board[0]))
    elif num_white !=0 and num_white == num_white_last_row:
        score = len(board[0])
    else:
        score = num_white - num_black
            
    return score


#return all the unrepeated next possible states 
def movegen(board, turn):
    possible_states = []
    #if static_eval(board) == len(board[0]) or static_eval(board) == -(len(board[0])):
    #    return board
    for row in range(len(board)):
        for col in range(len(board[row])):
            #check if the current position is the piece we want to move
            if board[row][col] == turn:
                states = move(board, row, col)
                #delete the repeat states
                for element in states:
                    if element not in possible_states:
                        possible_states.append(element)
    if len(possible_states) == 0:
        possible_states.append(board)
    return possible_states

#return all the possible next states
#need board and the position of current piece as the arguments
def move(board, row, col):
    possbile_move = []
    first_row_space = len(board[0])
    #check the current moving piece is 'w' or 'b'
    if board[row][col] == 'w':
        #separate the board to three part
        #the first part is row < len(board)/2
        if row < (len(board)-1)/2:
            #check if the current piece at the beginning of the row
            #if it is at the beginning of the row, it can only move right downward
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
            #if it is at the end of the row, it can only move left downward
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
            #capture the opponent in this if statement
            if row < (len(board)-1)/2 - 1:
                #at the beginning of the borad, can only capture one way
                if col == 0 and board[row+1][col] == 'b' and board[row+2][col] == '-':
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
                #at the end of the borad, can only capture one way
                if col == first_row_space - (row + 1) and board[row+1][col - 1] == 'b' and board[row+2][col-2] == '-':
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
                #not at the beginning or the end
                if col != 0 and col != first_row_space - (row + 1) :
                    if board[row+1][col - 1] == 'b': 
                        if (col - 1) != 0 and board[row+2][col-2] == '-':
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

                    if board[row+1][col] == 'b':
                        if col != first_row_space - (row+2) and board[row+2][col] == '-':
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
            #The second part is the row = len(board)/2 - 1, we just have 3 piece at most in this row.
            #this part is only for capturing
            if row == (len(board)-1)/2 - 1:
                #at the begining
                if col == 0 and board[row+1][0] == 'b' and board[row+2][col+1] == '-':
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
                #at the middle
                if col == 1:
                    if board[row+1][0] == 'b' and board[row+2][col-1] == '-':
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
                    if board[row+1][1] == 'b' and board[row+2][col+1] == '-':
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
                #at the end
                if col == 2 and board[row+1][1] == 'b' and board[row+2][col-1] == '-':
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
            #'w' moving and 'w' not at the begining or the end
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

        #the thrid part row >= len(board)/2 and not at the last row
        elif row >= (len(board)-1)/2 and row != 2 * first_row_space - 4:
            #moving left downward
            if board[row+1][col] == '-':
                new_board = copy.deepcopy(board)
                temp_next_row = list(new_board[row+1])
                temp_this_row = list(new_board[row])
                temp_next_row[col] = 'w'
                temp_this_row[col] = '-'
                new_board[row+1] = ''.join(temp_next_row)
                new_board[row] = ''.join(temp_this_row)
                possbile_move.append(new_board)
            #moving right downward
            if board[row+1][col+1] == '-':
                new_board = copy.deepcopy(board)
                temp_next_row = list(new_board[row+1])
                temp_this_row = list(new_board[row])
                temp_next_row[col+1] = 'w'
                temp_this_row[col] = '-'
                new_board[row+1] = ''.join(temp_next_row)
                new_board[row] = ''.join(temp_this_row)
                possbile_move.append(new_board)
            #capturing in this part
            if row < 2 * first_row_space - 5:
                if board[row+1][col] == 'b' and board[row+2][col] == '-': 
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
                if board[row+1][col+1] == 'b' and board[row+2][col+2] == '-': 
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
    
    #if the piece is 'b'
    if board[row][col] == 'b':
        #separate to three part, like above
        if row > (len(board)-1)/2:
            #'b' at the end or at the beginning
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
    
            #'b' captures opponent
            if row > (len(board)-1)/2 + 1:
                if col == 0 and board[row-1][col] == 'w' and board[row-2][col] == '-':
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
                if col == len(board[row]) - 1 and board[row - 1][col - 1] == 'w' and board[row-2][col-2] == '-':
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
                    if board[row-1][col - 1] == 'w' :
                        if (col - 1) != 0 and board[row-2][col-2] == '-': 
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

                    if board[row-1][col] == 'w':
                        if col != len(board[row-1]) - 1 and board[row-2][col] == '-': 
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
    
            #the second part and this part is just for capturing
            if row == (len(board)-1)/2 + 1:
                if col == 0 and board[row-1][0] == 'w' and board[row-2][col+1] == '-':
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
                    if board[row-1][0] == 'w' and board[row-2][col-1] == '-':
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
                    if board[row-1][1] == 'w' and board[row-2][col+1] == '-':
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
                if col == 2 and board[row-1][1] == 'w' and board[row-2][col-1] == '-':
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

            #for 'b' movement, not at the beginnin or end
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
    
        #the third part
        elif row <= (len(board)-1)/2 + 1 and row != 0:
            #for moving left upward
            if board[row-1][col] == '-':
                new_board = copy.deepcopy(board)
                temp_next_row = list(new_board[row-1])
                temp_this_row = list(new_board[row])
                temp_next_row[col] = 'b'
                temp_this_row[col] = '-'
                new_board[row-1] = ''.join(temp_next_row)
                new_board[row] = ''.join(temp_this_row)
                possbile_move.append(new_board)
            #for moving right upward
            if board[row-1][col+1] == '-':
                new_board = copy.deepcopy(board)
                temp_next_row = list(new_board[row-1])
                temp_this_row = list(new_board[row])
                temp_next_row[col+1] = 'b'
                temp_this_row[col] = '-'
                new_board[row-1] = ''.join(temp_next_row)
                new_board[row] = ''.join(temp_this_row)
                possbile_move.append(new_board)
            #for capturing
            if row > 1:
                if board[row-1][col] == 'w' and board[row-2][col] == '-': 
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
                if board[row-1][col+1] == 'w' and board[row-2][col+2] == '-':
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

