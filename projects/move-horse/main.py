pos = input()

pos_let = pos[0]
pos_dig = int(pos[1])

pos_col = ord(pos_let) - ord('a')
pos_row = 8 - pos_dig

board = []
for i in range(8):
    board.append([])
    for j in range(8):
        board[i].append('.')
        
board[pos_row][pos_col] = 'N'

pos_row_offset = [-2, -2, -1, -1, 1, 1, 2, 2]
pos_col_offset = [-1, 1, -2, 2, -2, 2, -1, 1]

for i in range(8):
    new_pos_row = pos_row + pos_row_offset[i]
    new_pos_col = pos_col + pos_col_offset[i]
    if 0 <= new_pos_row < 8 and 0 <= new_pos_col < 8:
        board[new_pos_row][new_pos_col] = '*'
        
for i in range(8):
    line = ''
    for j in range(8):
        if j > 0:
            line += ' '
        line += board[i][j]
    print(line)