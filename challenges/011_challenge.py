"""
CHALLENGE ELEVEN:
Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
"""
height = float(input('Wall height: '))
width = float(input('Wall width: '))
area = height * width
paint = area / 2
print("The wall dimensions are {0}m x {1}m.".format(height, width), end=" ")
print('The area is {0:.2f}m² and {1:.2f} liters of paint will be needed.'.format(area, paint))