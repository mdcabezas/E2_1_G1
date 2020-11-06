import paquete_cientifico

print("Calcularemos área y perímetro de una circunferencia")
print("Ingrese centímetros de radio de la circunferencia: ")
radioC = int(input())
print ("El área de la circunferencia es: ", areaC(radioC), "cms^2")
print ("El perímetro de la circunferencia es: ", perimetroC(radioC), "cms")


print("Calcularemos área y perímetro de un triángulo equilátero")
print("Ingrese centímetros de base del triángulo: ")
baseT = int(input())
print("ingrese centímetros de altura del triángulo equilatero: ")
alturaT = int(input())
print ("El área del triángulo es: ", areaT(baseT, alturaT), "cms^2")
print ("El perímetro del triángulo es: ", perimetroT(baseT, alturaT), "cms")


print("Calcularemos área y perímetro de un rectángulo")
print("Ingrese centímetros de base del rectángulo: ")
baseR = int(input())
print("ingrese centímetros de altura del rectángulo: ")
alturaR = int(input())
print ("El área del rectángulo es: ", areaR(baseR, alturaR), "cms^2")


print("Calcularemos distancia recorrida con valores velocidad en km y tiempo en horas")
print("Ingrese tiempo en horas: ")
tiempo = int(input())
print("ingrese distancia en kilometros: ")
velocidad = int(input())
print ("La distancia recorrida es de: ", distanciaR(tiempo, velocidad), "km/h")

#probando el if main
from nuevos_calculos import imprimemelo
imprimemelo()