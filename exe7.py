'''Escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do
novo salário com reajuste de 35%.'''

salario = float(input())
reajuste = (0.035)

salarioAjustado = salario * reajuste
salario += salarioAjustado


print("Salário:",salario)
