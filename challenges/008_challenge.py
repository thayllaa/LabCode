"""
CHALLENGE EIGHT:
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
"""
meter = float(input("Meter value: "))
cm = meter * 100
mm = meter * 1000
km = meter / 1000
hm = meter / 100
dam = meter / 10
dm = meter * 10

print("Analysing the meter {:.2f}:".format(meter))
print("In centimeters: {:.2f} cm".format(cm))
print("In millimeters: {:.2f} mm".format(mm))
print("In kilometers: {:.2f} km".format(km))
print("In hectometers: {:.2f} hm".format(hm))
print("In decameters: {:.2f} dam".format(dam))
print("In decimeters: {:.2f} dm".format(dm))
