salario = float(input('Digite o salário do funcionário: '))

aumento = salario * 0.15

salario_final = aumento + salario

print('Seu salario de {}, com aumento de 15%, vai para {:.2f}'.format(salario,salario_final))