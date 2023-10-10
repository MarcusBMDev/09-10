a = float(input('Escreva o primeiro número: '))
b = float(input('Escreva o segundo número: '))
c = float(input('Escreva o terceiro número: '))
maximo = max(a,b,c)
minimo = min(a,b,c)
numero = a + b + c - maximo - minimo
print("Números em ordem decrescente:")
print(maximo)
print(numero)
print(minimo)

#SEGUNDA OPÇÃO
if a >= b and a >= c and b >= c:
    print(f'A ordem decrescente é {a} , {b} e {c}')
elif a >= b and a >=c and c >= b:
    print(f'A ordem decrescente é {a} , {c} e {b}')
elif b >= a and b >= c and a >= c:
    print(f'A ordem decrescente é {b} , {a} e {c}')
elif b >= a and b >= c and c >= a:
    print(f'A ordem decrescente é {b} , {c} e {a}')
elif c >= a and c >= b and a >=b:
    print(f'A ordem decrescente é {c} , {a} e {b}')
elif c >= a and c >= b and b >= a:
    print(f'A ordem decrescente é {c} , {b} e {a}')