# Soma de Números de 1 a 100:
soma = 0 # Inicializa a variável para armazenar a soma

# Usa um laço for para somar os números de 1 a 100
for numero in range(1, 101): 
    soma += numero

print(f"A soma de todos os números de 1 a 100 é: {soma}")

'''
Se fosse digitado (1, 100) a soma dos números seriam feitas do 1 ao 99. 
Sempre que desejar um número específico no final, digite um número a mais.
Pois o Python conta o número 1 sendo o index 0 e o 99 será o index 100.
Sendo assim, o número 100 será o index 101.
'''