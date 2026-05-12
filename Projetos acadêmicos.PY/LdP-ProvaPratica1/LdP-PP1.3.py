import math

x1 = float(input("P(x1):"))
y1 = float(input("P(y1):"))
x2 = float(input("Q(x2):"))
y2 = float(input("Q(y2):"))


distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("A distância entre os pontos é:",distancia)
