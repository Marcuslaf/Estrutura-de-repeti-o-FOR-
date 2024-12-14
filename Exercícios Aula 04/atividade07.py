# Contagem de Vogais em uma Palavra:
vogais = 'aeiouAEIOU'

palavra = input("Digite uma palavra: ") # Solicite ao usuário

total_vogais = 0 # Inicializa contador de vogais

for caractere in palavra: # Percorre cada caractere da palavra
    if caractere in vogais: # Verifica se o caractere está na lista de vogais
        total_vogais += 1

print(f"A palavra '{palavra}' contém {total_vogais} vogal(is).")