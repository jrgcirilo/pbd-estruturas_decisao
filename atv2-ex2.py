n1=float(input("Digite a primeira nota"))
n2=float(input("Digite a segunda nota"))
media=float((n1+n2)/2)
print(media)
if media >= 6:
    if media >= 9 or media == 10:
        print('Conceito:A')
        print('Aprovado')
    if media >= 7.5 and media < 9:
        print('Conceito:B')
        print('Aprovado')
    if media >= 6 and media < 7.5:
        print('Conceito:C')
        print('Aprovado')
else:
    if media >= 4 and media < 6:
        print('Conceito:D')
        print('Reprovado')
    if media >= 0 and media < 4:
        print('Conceito:E')
        print('Reprovado')