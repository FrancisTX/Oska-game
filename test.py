string_new = 'abcd'

for element in range(len(string_new)):
    print("Hey!")


"""         elif board[row+1][col] == 'b' and row <= len(board) - 2:
            new_board = copy.deepcopy(board)
            temp_this_row = list(new_board[row])
            temp_next_row = list(new_board[row+1])
            temp_next_next_row = list(new_board[row+2])
            if row < len(board)/2 - 1:
                temp_this_row[col] = '-'
                temp_next_row[col] = '-'
                temp_next_next_row[col] = 'w'
            if row == len(board)/2 - 1:
                temp_this_row[col] = '-'
                temp_next_row[col] = '-'
                temp_next_next_row[col+1] = 'w'
            if row >= len(board)/2:
                temp_this_row[col] = '-'
                temp_next_row[col+1] = '-'
                temp_next_next_row[col+2] = 'w'
            new_board[row+2] = ''.join(temp_next_next_row)
            new_board[row+1] = ''.join(temp_next_row)
            new_board[row] = ''.join(temp_this_row) """


"""             if board[row+1][col+1] == 'b' and row == len(board)/2 - 1:
                new_board = copy.deepcopy(board)
                temp_this_row = list(new_board[row])
                temp_next_row = list(new_board[row+1])
                temp_next_next_row = list(new_board[row+2])
                temp_this_row[col] = '-'
                temp_next_row[col] = '-'
                temp_next_next_row[col+1] = 'w'
                new_board[row+2] = ''.join(temp_next_next_row)
                new_board[row+1] = ''.join(temp_next_row)
                new_board[row] = ''.join(temp_this_row) """