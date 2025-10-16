# Cadastro de Produtos
# Peça o nome e preço de 5 produtos usando um laço for.
# Ao final, exiba o nome de todos e a soma total dos preços.

nomes = []
total = 0

for i in range(5):
    nome = (input("Nome do produto: "))
    preco = float(input("Preço: "))
    nomes.append(nome)
    total += preco

print("Produtos:", nomes)
print("Soma dos preços:", total)