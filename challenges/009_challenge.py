"""
CHALLENGE NINE:
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""
number = int(input("Write a number: "))
print("Here's your multiplication table:")
for i in range(1, 11):
    res = number * i
    m = "{} x {} = {}".format(number, i, res)
    print(m)
