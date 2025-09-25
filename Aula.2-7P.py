# Exercício proposto na aula feito pelo professor:

salario = float(input('Digite seu salário mensal: R$ '))
soma = 0

while True:
    despesa = input("Digite a descrição da despesa (ou 'sair' para encerrar): ")

    if despesa.lower() == 'sair':
        break
    valor = float(input(f'Digite o valor da despesa {despesa}: R$ '))
    soma += valor

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