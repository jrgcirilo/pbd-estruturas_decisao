print("1-File Duplo\n2-Alcatra\n3-Picanha\n")
tipo = int(input("Escolha um tipo de carne: "))
quantidade = float(input("Escolha a quantidade: "))
cartao = int(input("A compra será realizada com cartao Tabajara? 1 p/ SIM - 2 p/ NAO: "))

if tipo == 1:
    nome = "File Duplo"
    if quantidade <= 5:
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.80
if tipo == 2:
    nome = "Alcatra"
    if quantidade <= 5:
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80
if tipo == 3:
    nome = "Picanha"
    if quantidade <= 5:
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80

if cartao == 1:
    resp = "SIM"
    desconto = ((preco * 5) /100)
    total = preco - desconto
else:
    resp = "NAO"
    total = preco
    
print("\n***CUPOM FISCAL***")
print("* Carne... %s " %nome)
print("* Quantidade... %2.f KG " %quantidade)
print("* Preço... %2.f R$ " %preco)
print("* Cartao Tabajara... %s " %resp)
print("* Total com desconto... %2.f R$ " %total)
print("***")