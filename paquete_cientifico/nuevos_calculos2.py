def pitagoras(a, b):
    hipotenusa = a**2 + b**2
    return hipotenusa

def relatividad(m, c):
    energia = m * c**2
    return energia

def gravity (g, r, m, m2):
    fuerza = g ((m * m2)/r**2 )
    return fuerza






#zona pruebas
if __name__ =="__main__": #Es este el script principal o es un script que estoy importando?
    print("Calcularemos el teorema de Pitágoras")
    print("Ingrese centímetros de base del triángulo: ")
    a = int(input())
    print("ingrese centímetros de altura del triángulo: ")
    b = int(input())
    print ("La hipotenusa^2 del triángulo mide: ", pitagoras(a, b) , "cms^2")