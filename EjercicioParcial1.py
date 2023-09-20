listaN = []
#Mi código de estudiante es 2221874 por lo tanto n = 4 + 3
n = 7
for i in range(n):
    number = int(input("Ingresa el valor: "))
    listaN.append(number)
for i in range (n):
    suma = sum(listaN)
    promedio = int(suma/n)
print("El número entero calculado es:", promedio)

while promedio != 1:
    if promedio % 2 == 0:
        print("Par ->", int(promedio) , "/2 =", int((promedio/2)))
        promedio /= 2
    else:
        print("Impar ->", int(promedio), "*3+1 =", int((promedio*3+1)))
        promedio = promedio*3+1
print("Finalmente, verificamos que el resultado fnal es", promedio)