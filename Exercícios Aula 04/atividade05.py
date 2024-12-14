# Contagem de Números Positivos e Negativos:
positivos = 0
negativos = 0

print("Digite 10 números:")

for i in range(10):
    try:
        numero = float(input(f"Digite o número {i+1}: "))
        
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        # Números zero são ignorados na contagem
    
    except ValueError: # Quando um valor não atenteder os requisitos, enviará a mensagem abaixo.
        print("Entrada inválida. Por favor, digite um número válido.")

# Resultado
print(f"\nResumo:") # O "\n" serve para fazer uma quebra de linha.
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")