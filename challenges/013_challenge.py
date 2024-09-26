"""
CHALLENGE THIRTEEN:
Faça um algoritmo que leia o salário de um fundionário e mostre seu novo salário, com 15% de aumento.
"""
wage = float(input('Wage: R$'))
increase = wage * 0.15
new_wage = wage + increase
print("Its increase is R${}.".format(new_wage))