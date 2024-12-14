# Contar Números Positivos e Negativos:
print("Digite 10 números (ou digite 0 para parar):")

# Contadores para números positivos e negativos
positivos = 0
negativos = 0

for i in range(10): # Laço para entrada de 10 números
    try:
        numero = float(input(f"Digite o número {i+1}: ")) # Solicite um número ao usuário
        
        if numero == 0: # Interrompe o loop se número for zero
            print("\nEntrada de zero detectada. Interrompendo...") # "\n" usado para fazer uma quebra de linha.
            break # Usado para parar o loop quando atender a condição solicitada.
        
        # Conta os números positivos e negativos
        if numero > 0:
            positivos += 1
            print(f"{numero} é um número POSITIVO")
        else:
            negativos += 1
            print(f"{numero} é um número NEGATIVO")
    
    except ValueError: # Usando quando não é atendido o que foi solicitado.
        print("Entrada inválida. Por favor, digite um número.")

print("\nResumo:") # "\n" usado para fazer uma quebra de linha.
print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")