'''
print("  #  ")
print(" ### ")
print("#####")
'''

linhas = 3

for i in range(linhas):
    espacos = linhas - i - 1
    cruz = 2 * i + 1
    print(" " * espacos + "#" * cruz)
                    #2