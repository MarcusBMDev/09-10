valor = []

for i in range(3):
    preco = float(input(f"Digite o valor do produto:"))
    valor.append(preco)

indice_mais_barato = 0

for i in range( len(valor)):
    if valor[i] < valor[indice_mais_barato]:
        indice_mais_barato = i

print(f"Voce deve comprar o que custa R${valor [indice_mais_barato]}")
