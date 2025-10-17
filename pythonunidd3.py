#1
def menor_estricto(a, b, c):
    menor = min(a, b, c)
    if (a == menor) + (b == menor) + (c == menor) == 1:
        return menor
    else:
        return -1

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
z = int(input("Ingrese el tercer número: "))

resultado = menor_estricto(x, y, z)
if resultado == -1:
    print("No hay un menor estricto.")
else:
    print(f"El menor estricto es: {resultado}")

#2
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def dias_del_mes(mes, año):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and es_bisiesto(año):
        return 29
    return dias_por_mes[mes - 1]
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

print(f"El mes {mes} del año {año} tiene {dias_del_mes(mes, año)} días.")

#3
def calcular_vuelto(total, abonado):
    if abonado < total:
        print("Error: el dinero recibido es insuficiente.")
        return
    
    vuelto = abonado - total
    denominaciones = [1000, 500, 200, 100, 50, 10, 5, 2, 1]
    print(f"Vuelto a entregar: ${vuelto}")
    
    for d in denominaciones:
        cantidad = vuelto // d
        if cantidad > 0:
            tipo = "billete" if d >= 10 else "moneda"
            print(f"{cantidad} {tipo}(s) de ${d}")
            vuelto %= d

total = float(input("Total de la compra: $"))
abonado = float(input("Importe abonado: $"))
calcular_vuelto(total, abonado)

#4
def triangulo_normal(n):
    for i in range(1, n + 1):
        print('*' * i)

def triangulo_invertido(n):
    for i in range(n, 0, -1):
        print('*' * i)

n = int(input("Ingrese el número de filas: "))
triangulo_normal(n)
triangulo_invertido(n)

#5
cubo = lambda x: x ** 3
num = int(input("Ingrese un número: "))
print(f"El cubo de {num} es {cubo(num)}")

#6
es_divisible_por_3 = lambda x: x % 3 == 0
num = int(input("Ingrese un número: "))
if es_divisible_por_3(num):
    print(f"{num} es divisible por 3.")
else:
    print(f"{num} no es divisible por 3.")

#7
N = int(input("Ingrese N: "))
pares = [i for i in range(1, N + 1) if i % 2 == 0]

print("Primeros 5:", pares[:5])
print("Últimos 5:", pares[-5:])

#8
nombres1 = ["Ana", "Luis", "Carlos", "María", "Pedro"]
nombres2 = ["Luis", "Pedro", "Sofía"]

conjunto1 = set(nombres1)
conjunto2 = set(nombres2)
resultado = list(conjunto1 - conjunto2)

print("Original:", nombres1)
print("A eliminar:", nombres2)
print("Resultante:", resultado)

#9
def ordenada_desc(lista):
    return lista == sorted(lista, reverse=True)
print(ordenada_desc([9, 7, 5]))   # True
print(ordenada_desc([3, 4, 1]))   # False

#10
import string
def es_palindromo(frase):
    # Quitar signos y espacios, y pasar a minúsculas
    limpia = ''.join(ch.lower() for ch in frase if ch.isalnum())
    return limpia == limpia[::-1]

texto = input("Ingrese una frase: ")
if es_palindromo(texto):
    print("Es palíndromo.")
else:
    print("No es palíndromo.")

#11
texto = input("Ingrese una cadena: ")
print(texto.rjust(80))

#12
import datetime
def fecha_formateada(fecha_tupla):
    dia, mes, año = fecha_tupla
    fecha = datetime.date(año, mes, dia)
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    nombre_dia = dias_semana[fecha.weekday()]
    return f"{nombre_dia} {dia} de {meses[mes]} de {año}"

print(fecha_formateada((8, 10, 2025)))  # Ejemplo: Martes 8 de Octubre de 2025

#13
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()
unicas = sorted(set(palabras))
print(unicas)

#14
def actualizar_precios(diccionario, porcentaje):
    aumento = 1 + porcentaje / 100
    return {producto: round(precio * aumento, 2) for producto, precio in diccionario.items()}

# Ejemplo
precios = {'pan': 100, 'leche': 200}
nuevos = actualizar_precios(precios, 10)
print(nuevos)  # {'pan': 110.0, 'leche': 220.0}

#15
def quitar_numeros(cadena):
    return ''.join(ch for ch in cadena if not ch.isdigit())
texto = input("Ingrese una cadena: ")
print(quitar_numeros(texto))