""" OPERAÇÕES ARITMÉTICAS """
# Caso vá usar o resultado da cont adepois em outro lugar, é mais viável que o uso das variáveis.
# Se não for o caso, o modo abaixo, sem variável, é somente para mostrar na tela
'''
value1 = int(input("Write a value: "))
value2 = int(input("Write another value: "))
print("The sum is equal to {}" .format(value1+value2))
'''

num1 = int(input("Number one: "))
num2 = int(input("Number two: "))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2
print("The sum is equal to {0}, the product is {1} and the division is {2:.3f}" .format(s, m, d), end=" ")
print("Entire division {0} and power {1}" .format(di, e))