# Cálculo de Média de Notas:
soma_notas = 0

print("Sistema de Cálculo de Média Escolar")
print("Digite 5 notas do aluno:")

for i in range(5): # Laço para entrada e soma das notas
    while True:
        try:
            nota = float(input(f"Digite a nota {i+1}: "))
            
            if 0 <= nota <= 10: # Validação para notas entre 0 e 10
                soma_notas += nota
                break
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError: # Usado quando não atendo o  que foi pedido.
            print("Por favor, digite um número válido.")

media = soma_notas / 5 # Cálculo da média

print(f"\nMédia do aluno: {media:.2f}") # "\n" é usado para fazer uma quebra de linha. "2f" usado para manter no máximo duas casa decimais depois do ponto (float).
if media >= 6: # Caso a média do aluno seja maior ou igual a 6.
    print("Resultado: Aluno aprovado!")
else: # Se a média for inferior a 6.
    print("Resultado: Aluno reprovado!")