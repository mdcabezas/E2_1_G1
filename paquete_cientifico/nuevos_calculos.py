from utils import PI
#circunferencia
def areaC(radioC):
    #pi = 3.141592
    areaCE = PI * (radioC * radioC)
    return areaCE

def perimetroC(radioC):
    #pi = 3.141592
    perimetroCE = 2 * PI *radioC
    return perimetroCE

#triángulo equilatero
def areaT(baseT, alturaT):
    areaTE = (baseT * alturaT) / 2
    return areaTE

def perimetroT(baseT, alturaT):
    perimetroTE = baseT + baseT + baseT
    return perimetroTE

#rectángulo
def areaR(baseR, alturaR):
    areaRE = baseR * alturaR
    return areaRE

def perimetroR(baseR, alturaR):
    perimetroRE = 2 * baseR + 2 * alturaR
    return perimetroRE

#distancia
def distanciaR(tiempo, velocidad):
    distanciaRE = tiempo * velocidad
    return distanciaRE


def imprimemelo():
        print (__name__)
#zona pruebas
if __name__ =="__main__": #Es este el script principal o es un script que estoy importando?
    print("Calcularemos área y perímetro de un rectángulo")
    print("Ingrese centímetros de base del rectángulo: ")
    baseR = int(input())
    print("ingrese centímetros de altura del rectángulo: ")
    alturaR = int(input())
    print ("El área del rectángulo es: ", areaR(baseR, alturaR), "cms^2")
   
     
imprimemelo()
    