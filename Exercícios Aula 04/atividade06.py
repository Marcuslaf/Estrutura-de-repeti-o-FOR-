# Soma de Números Paresde 1 a 50
soma_pares = 0

for numero in range(1, 51):
    if numero % 2 == 0:  # Verifica se o número é par.
        soma_pares += numero

print(f"A soma de todos os números pares de 1 a 50 é: {soma_pares}")