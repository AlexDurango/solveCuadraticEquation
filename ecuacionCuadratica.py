import math 

try:
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))
except:
    print("Ocurrio un error, recuerde que los valores decimales se escriben con un punto. e.g: 1.23")

if (a == 0):
    print("a debe ser diferente de 0")
    exit()

resultSqrt = 0
subradicalSqrt = (b**2)-(4*a*c)
print("\nSubradical: " + str(subradicalSqrt)+"\n")

if (subradicalSqrt < 0):
    print("El resultado de la raiz no está en los números Reales")
    exit()

resultSqrt = math.sqrt(subradicalSqrt)
positiveResult = ((-1*b) + resultSqrt)/(2*a)
negativeResult = ((-1*b) - resultSqrt)/(2*a)

if(positiveResult == negativeResult):
    print("Solo hay un resultado: "+str(positiveResult))
    input()
else:
    print("Resultado positivo: "+ str(positiveResult))
    print("Resultado negativo: "+ str(negativeResult))
    input()

