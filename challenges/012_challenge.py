"""
CHALLENGE TWELVE:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""
price = float(input('Product price: R$'))
discount = price * 0.05
new_price = price - discount
print("The discounted price is R${}.".format(new_price))
