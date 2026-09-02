# Proograma para média de calculo de notas
# Autor: Carlos Marcelo Silva

# Entrada
nome = input("digite o nome do aluno: ")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

# Processamento
media = (nota1 + nota2) / 2

# Saída
print(f"\nAluno: {nome}")
print(f"media: {media:.2f}")

if media >= 6:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")