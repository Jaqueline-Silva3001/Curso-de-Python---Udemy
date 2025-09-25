# Exemplo utilizando for:

lista = ['Cookie', 'Milk-shake','Danone', 'Granola','Peixe']

for item in lista:
    print(item)


for item in lista:
    if item == 'Cookie':
        print(f'{item}! Minha comida favorita')
    elif item == 'Peixe':
        print(f'{item}! Eu odeio peixe')
    else:
        print(f'{item}! Eu não gosto tanto assim.')