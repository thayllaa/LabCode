"""
CHALLENGE TEN:
Faça um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dolares ela pode comprar. Considere US$1.00=R$5.48
"""
br = float(input('Value you have in your wallet: R$'))
us = br / 5.48
print('With R${:.2f}, you can buy US${:.2f}'.format(br, us))