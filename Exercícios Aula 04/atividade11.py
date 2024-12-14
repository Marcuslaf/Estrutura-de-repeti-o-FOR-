# Verificar Múltiplos de 5 e Parar:
for numero in range(1, 31): 
    if numero > 20: # Verifica se o número é maior que 20 e para o loop
        break

    if numero % 5 == 0: # Verifica se o número é múltiplo de 5
        print(f"{numero} é múltiplo de 5")
    else:
        print(numero)
