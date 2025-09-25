# Exercício proposto na aula:

salario = float(input('Digite seu salário mensal: R$ '))
soma = 0
acab = 'sair'
despesa = 0
valor = 0

while despesa != acab:
    despesa = input('Digite a descrição da sua despesa (ou sair para encerar): ')
    if despesa != acab:
        valor = float(input(f'Digite o valor da despesa {despesa}: R$ '))
        soma = soma + valor
    else:
        print("")
        print('------ RESUMO ------')
        print(f'Salário mensal: R$ {salario}')
        print(f'Total de despesas: R$ {soma}')

        diferenca = abs(salario - soma)

        if soma > salario:
            print(f'Você está no vermelho! Faltam R$ {diferenca} para cobrir as suas despesas.')

        elif soma == salario:
            print('Você está no limite dos seus gastos! Não pode gastar mais.')

        else:
            print(f'Você está no verde! Seu saldo: R$ {diferenca}')



