def knight_moves(position):
    
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    moves = [
    (2, 1), (2, -1),
    (-2, 1), (-2, -1),
    (1, 2), (1, -2),
    (-1, 2), (-1, -2)
    ]
    valid_moves = []

    row = int(position[1]) - 1
    column = letters.index(position[0])


    for dr, dc in moves:
        new_row = row + dr
        new_col = column + dc

        if 0 <= new_row < 8 and 0 <= new_col < 8:
            new_position = f"{letters[new_col]}{new_row + 1}"
            valid_moves.append(new_position)

    return len(valid_moves)

print(knight_moves("E3"))