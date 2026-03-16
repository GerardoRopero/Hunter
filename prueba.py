a = 10
b = 3
print("=== ARITMETICA ===")
print("Suma:          ", a + b)
print("Resta:         ", a - b)
print("Multiplicacion:", a * b)
print("Division:      ", a / b)
print("Division entera:", a // b)
print("Modulo:        ", a % b)
print("Potencia:      ", a ** b)
print("=== CONDICIONALES ===")
nota = 85
if nota >= 90:
    print("Calificacion: A")
elif nota >= 80:
    print("Calificacion: B")
elif nota >= 70:
    print("Calificacion: C")
else:
    print("Calificacion: F")
print("=== WHILE ===")
contador = 1
suma = 0
while contador <= 10:
    suma += contador
    contador += 1
print("Suma del 1 al 10:", suma)
print("=== FOR RANGE ===")
for i in range(1, 6):
    print(i * i)
print("=== FUNCIONES ===")
def factorial(n):
    resultado = 1
    k = 2
    while k <= n:
        resultado *= k
        k += 1
    return resultado
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
print("5! =", factorial(5))
print("7! =", factorial(7))
print("¿4 es par?", es_par(4))
print("¿7 es par?", es_par(7))
print("=== LISTAS ===")
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
maximo = numeros[0]
minimo = numeros[0]
for n in numeros:
    if n > maximo:
        maximo = n
    if n < minimo:
        minimo = n
print("Lista:  ", numeros)
print("Maximo: ", maximo)
print("Minimo: ", minimo)
print("=== BOOLEANOS ===")
x = True
y = False
print("True and False:", x and y)
print("True or  False:", x or y)
print("not True:      ", not x)
