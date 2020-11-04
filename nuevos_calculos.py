def areaC(radioC):
    pi = 3.141592
    areaCE = pi * (radioC * radioC)
    return areaCE

def perimetroC(radioC):
    pi = 3.141592
    perimetroCE = 2 * pi *radioC
    return perimetroCE


def areaT(baseT, alturaT):
    areaTE = (baseT * alturaT) / 2
    return areaTE

def perimetroT(baseT, alturaT):
    perimetroTE = baseT + baseT + baseT
    return perimetroTE


def areaR(baseR, alturaR):
    areaRE = baseR * alturaR
    return areaRE

def perimetroR(baseR, alturaR):
    perimetroRE = 2 * baseR + 2 * alturaR
    return perimetroRE

def distanciaR(tiempo, velocidad):
    distanciaRE = tiempo * velocidad
    return distanciaRE