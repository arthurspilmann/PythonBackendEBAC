numero = input("Digite um número: ")
print(f"O número que você digitou foi {numero} e o contrário dele é {numero[::-1]}")

if numero == numero[::-1]:
    print("O número é um palíndromo.")
else:
    print("O número não é um palíndromo.")