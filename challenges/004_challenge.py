"""
CHALLENGE FOUR:
Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possiveis sobre ele.
"""
data = input("Write something: ")
print("Its primitive type's {}" .format(type(data)))
print("Are there spaces? {}" .format(data.isspace()))
print("Is it a number? {}" .format(data.isnumeric()))
print("Is it an alphabetic? {}" .format(data.isalpha()))
print("Is it an alphanumeric? {}" .format(data.isalnum()))
print("Is it in uppercase? {}" .format(data.isupper()))
print("Is it in lowercase? {}" .format(data.islower()))
print("Is it a titled? {}" .format(data.istitle()))
print("Is it an empty string?", data.isprintable())
print("I'm gonna split it: {}" .format(data.split(sep=None)))