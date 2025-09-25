# Exemplo utilizando o if:

idade = int(input('Digite sua idade: '))

# == -> igual.
# != -> diferente.
# <,> -> menor,maior.
# <=,>= -> menor ou igual, maior ou igual.

if idade > 18:
    print('Sua compra foi aprovada! Você é maior de 18 anos')
elif idade == 18:
    print('Sua compra foi aprovada! Por pouco! Você tem 18 anos')
else:
    print('Sua compra foi REPROVADA! Você é menor de 18 anos e não pode comprar bebida alcoólica')