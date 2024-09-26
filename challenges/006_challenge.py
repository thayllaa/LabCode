"""
CHALLENGE SIX:
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
number = int(input("A number, please: "))
print("Analysing the value {0}: \nIts double is equal to {1}. " .format(number, (number*2)))
print("Its triple is equal to {0}. \nAnd also the square root is {1}" .format( (number*3), (number**(1/2))))