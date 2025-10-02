# 1) Hola Mundo
print("¡Hola Mundo!")

# 2) Suma 3 + 5
print("La suma de 3 + 5 es:", 3 + 5)

# 3) Saludo
nombre_persona = input("¿Cuál es tu nombre? ")
print("Hola,un placer conocerte", nombre_persona)

# 4) Suma de dos números
primero = int(input("Escribí el primer número: "))
segundo = int(input("Escribí el segundo número: "))
print("El resultado de la suma es:", primero + segundo)

# 5) Comparar dos números
nro1 = int(input("Ingresá un número: "))
nro2 = int(input("Ingresá otro número: "))
if nro1 > nro2:
    print("El mayor es:", nro1)
elif nro2 > nro1:
    print("El mayor es:", nro2)
else:
    print("Son iguales")

# 6) Mayor de tres números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))
print("El número más grande es:", max(a, b, c))

# 7) Divisible por 2
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("Sí, es divisible por 2")
else:
    print("No, no es divisible por 2")

# 8) Divisible por 2, 3, 5 o 7
n = int(input("Ingresa un número:  "))
if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("Es divisible por 2, 3, 5 o 7")
else:
    print("No entra en ninguno de esos divisores")

# 9) Mostrar todos los divisores (2,3,5,7)
n = int(input("Ingresa un número para comprobar divisibilidad: "))
divs = []
for d in [2, 3, 5, 7]:
    if n % d == 0:
        divs.append(d)
if divs:
    print("Este número se puede dividir por:", divs)
else:
    print("No es divisible ni por 2, ni 3, ni 5, ni 7")

# 10) Divisores de un número
num = int(input("Número para calcular sus divisores: "))
print("Los divisores de", num, "son:")
for i in range(1, num+1):
    if num % i == 0:
        print(i)

# 11) Comprobar si es primo
num = int(input("Ingresa un número para saber si es primo: "))
es_primo = True
if num <= 1:
    es_primo = False
else:
    for i in range(2, num): 
        if num % i == 0:
            es_primo = False
            break
print(num, "es primo" if es_primo else "no es primo")

# 12) Notas
nota = float(input("Ingresá tu nota (0 a 10): "))
if 0 <= nota < 3:
    print("Muy deficiente")
elif nota < 5:
    print("Insuficiente")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
elif nota <= 10:
    print("Sobresaliente")
else:
    print("Error intenta de nuevo")

# 13) Pirámide 1 al 30
for i in range(1, 31):
    print(str(i) * i)

# 14) Pirámide inversa
num = int(input("¿Hasta qué número querés la pirámide inversa? "))
for i in range(num, 0, -1):
    print(str(i) * i)

# 15) Del 1 al 500
for i in range(1, 501):
    texto = str(i)
    if i % 4 == 0:
        texto += " (Múltiplo de 4)"
    if i % 9 == 0:
        texto += " (Múltiplo de 9)"
    print(texto)
    if i % 5 == 0:
        print("-" * 50)
