from itertools import permutations

def gerar_anagramas(palavra):
    return {"".join(p) for p in permutations(palavra)}

print(gerar_anagramas("roma"))
