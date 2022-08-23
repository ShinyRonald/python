'''Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z:
z =(x 2 + y 2 )
     (x-y) 2'''

x = int(input())
y = int(input())
z = int


dividendo = x**2 + y**2
divisor = (x-y)**2

if divisor > 0:
    z = dividendo/divisor
else:
    print("Não é possível dividir por zero")


print(dividendo)
print(divisor)
print(z)