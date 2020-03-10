n1=float(input("Digite um numero"))
n2=float(input("Digite outro numero"))
op=(input("Digite uma operacao"))
if(op=='+'):
    soma=float(n1+n2)
    print(soma)
    if float(soma) % 2 == 0:
        print("O numero informado e par")
    else:
        print("O numero informado e impar")
    if soma>=0:
        print("positivo")
    else:
        print("negativo")
    if(soma // 1 == soma): 
        print("inteiro")
    else:
        print("decimal")
if(op=='-'):
    sub=float(n1-n2)
    print(sub)
    if float(sub) % 2 == 0:
        print("O numero informado e par")
    else:
        print("O numero informado e impar")
    if sub>=0:
        print("positivo")
    else:
        print("negativo")
    if(sub // 1 == sub): 
        print("inteiro")
    else:
        print("decimal")
if(op=='/'):
    div=float(n1/n2)
    print(div)
    if float(div) % 2 == 0:
        print("O numero informado e par")
    else:
        print("O numero informado e impar")
    if div>=0:
        print("positivo")
    else:
        print("negativo")
    if(div // 1 == div): 
        print("inteiro")
    else:
        print("decimal")
if(op=='*'):
    mult=float(n1*n2)
    print(mult)
    if float(mult) % 2 == 0:
        print("O numero informado e par")
    else:
        print("O numero informado e impar")
    if mult>=0:
        print("positivo")
    else:
        print("negativo")
    if(mult // 1 == mult): 
        print("inteiro")
    else:
        print("decimal")