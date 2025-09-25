# Exemplo utilizando o while:

comida_fav = 'japa'

comida = input('Digite meu tipo de comida favorita: ')

while comida != comida_fav:
    print(f'ERROU! {comida} não é minha comida favorita!')
    print('Tente novamente!')
    comida = input('Digite meu tipo de comida favorita:')

print(f'Você acertou! {comida} é minha comida favorita')