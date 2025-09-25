# Usando os Operadores Básicos

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

soma = a + b
mult = a * b
div = a / b
divs = a // b
resto = a % b
elev = a**b

print(f'A soma dos números {a} e {b} é igual a {soma}')
print(f'A multiplicação entre os números {a} e {b} é igual a {mult}')
print(f'A divisão entre os números {a} e {b} é igual a {div}')
print(f'A divisão arredondada entre os números {a} e {b} é igual a {divs}')
print(f'O resto entre os números {a} e {b} é igual a {resto}')
print(f'O número {a} elevado a {b} é igual a {elev}')