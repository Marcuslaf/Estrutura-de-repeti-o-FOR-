# Tabuada de um Número: Multiplicação
numero = int(input("Digite um número: ")) # Solicite um número ao usuário

# Exibe a tabuada de multiplicação usando um laço for
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")