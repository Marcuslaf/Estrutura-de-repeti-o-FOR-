# Soma de Números com Desconto:
total = 0

for i in range(5):
    preco = float(input(f"Insira o preço do produto {i + 1}: "))
    total += preco

    if total > 100: # Somente quando o valor ultrapassar o valor de 100 que será dado o desconto de 10%.
        print("O total ultrapassou 100. Aplicando desconto de 10%.")
        total *= 0.9
        break

print(f"O total final é: R$ {total:.2f}") # "2f" é usado para definir que serão duas casa decimais depois do ponto (float).

'''
Se o cliente pode levar no máximo 5 produtos como está descrininado na range.
Porém, se o valor ultrapassar 100, será dado o desconto de 10%.
Independente do cliente ter pegado 5 produtos.
Sendo assim, se atingir valor acima com apenas um produto. A compra será finalizada.
'''