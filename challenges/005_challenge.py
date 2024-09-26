"""
CHALLENGE FIVE:
Faça um programa que leia um número inteiro e mostre o seu sucessor e antecessor.
"""
number = int(input("Write a number: "))
print("Analysing the value {0}, its predecessor is {1} and successor is {2}."
      .format(number, (number-1), (number+1)))