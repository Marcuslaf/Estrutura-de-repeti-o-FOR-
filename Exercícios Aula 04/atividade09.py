# Verificar Números Pares e Impares com Interrupção:
print("Verificando números de 1 a 40:")

# Contadores para números pares e ímpares
total_pares = 0
total_impares = 0

for numero in range(1, 41): # Laço para percorrer números de 1 a 40
    if numero == 20: # Interrompe o loop quando chegar ao número 20
        print(f"\nInterrompido no número 20!") # "\n" usado para quebrar a linha.
        break
    
    if numero % 2 == 0: # Verifica se o número é par ou ímpar
        print(f"{numero} é PAR")
        total_pares += 1
    else: # Caso o número não seja PAR.
        print(f"{numero} é ÍMPAR")
        total_impares += 1

print("\nResumo:") # "\n" usado para quebrar a linha.
print(f"Total de números pares: {total_pares}")
print(f"Total de números ímpares: {total_impares}")