import random

l =["X", "O"]
x = random.sample(l, 1)[0]

board = [[],[],[]]

for i in range(3):
    for j in range(3):
        board[j].append(random.sample(l, 1)[0])

#printar o tabuleiro
for i in board:
    print(i)

'''board = [["X","X","O"],
         ["X","O","O"],
         ["O","X","O"]]

''''''
referencia de posições
board = [[00,01,02],
         [10,11,12],
         [20,21,22]]
'''
# lista com as linhas que devem ser verificadas para a vitória
all_lines = []  
# pega as listas dentro de board e separa em listas (row) e coloca no all_lines para conferencia
for row in board:
    all_lines.append(row)
'''
referência linhas
r1 = board[0]
r2 = board[1]
r3 = board[2]
'''
# pega os elementos dentro de board (board[row][col]) e coloca em listas column
for col in range(3):
    column = []
    for row in range(3):
        column.append(board[row][col])
    all_lines.append(column)
'''
referência colunas
c1 = [board[0][0], board[1][0], board[2][0]]
c2 = [board[0][1], board[1][1], board[2][1]]
c3 = [board[0][2], board[1][2], board[2][2]]
'''

'''
referência diagonais
d1 = [board[0][0], board[1][1], board[2][2]]
d2 = [board[0][2], board[1][0], board[2][1]]
'''
d1 = []
for i in range(3):
    d1.append(board[i][i])
all_lines.append(d1)

d2 = []
for i in range(3):
    d2.append(board[i][2 - i])
all_lines.append(d2)


# verifica se cada elemento(lista) dentro de all_lines possui 3 valores iguais
# se não cair nas condições vai o else do for, que é empate
for line in all_lines:
    if line.count("X") == 3:
        print("X venceu!")
        break
    elif line.count("O") == 3:
        print("Bola venceu!")
        break
else:
    print("Empate.")