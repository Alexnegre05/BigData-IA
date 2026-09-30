# Ejercicio 1. Control de notas 
# Crea una lista llamada notas con al menos 10 calificaciones numéricas. 
# El programa debe: 
# - Mostrar todas las notas. 
# - Calcular cuántas notas están aprobadas y cuántas suspendidas. 
# - Calcular la nota media. 
# - Mostrar la nota más alta y la nota más baja. 
# - Indicar si la media final está aprobada o suspendida. 
# Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales.


print("solucion ejercicio 1")

notas = [8,2,4,5,10,9,0,3,6,1] 

print(notas)

aprovados = 0
suspendidos = 0
sumatorio = 0 # para la media necesitamos primero sumar todas las notas
for i in range(0, len(notas)):

    if(notas[i] >= 5):
        aprovados = aprovados + 1
    
    else:
        suspendidos = suspendidos + 1

    sumatorio = sumatorio + notas[i]

media = sumatorio/len(notas)

max = 0 # variable que contiene la nota maxima actual
min = 0 # lo mismo para min

for i in range(0, len(notas)):
    
    if (notas[i] > max): # si la nota es superior al max actual la nota pasa a ser el nuevo max
        max = notas[i]
    
    if (notas[i] < min):
        min = notas[i]

print("nota mas alta: " ,max)

print("nota mas baja: ", min)

if (media >= 5):
    print("media aprovada")

else:
    print("media suspendida")


# Ejercicio 2. Carrito de la compra 
# Crea dos listas: una con nombres de productos y otra con sus precios. 
# productos = ["pan", "leche", "arroz", "huevos"] 
# precios = [1.20, 0.95, 2.10, 2.80]



# El programa debe: 
# - Mostrar cada producto con su precio. 
# - Calcular el precio total de la compra. 
# - Aplicar un descuento del 10% si el total supera 20 euros. 
# - Mostrar el total final que debe pagarse. 
# Condición: Debe utilizar zip, un acumulador, if y operadores aritméticos. 


print("solucion ejercicio 2")

productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 0.95, 2.10, 2.80]

for producto,precio in zip(productos, precios):
    print("el producto", producto , "tiene de precio", precios)


sum = 0
for i in range(0, len(precios)):
    sum = sum + precios[i]

if (sum > 20):
    sum = sum - sum*0.1 # aplicamos el 10% solo y solo si el precio es > a 20

print("total", sum)





# Ejercicio 3. Registro de alumno 
# Crea un diccionario llamado alumno con los siguientes datos: 
# nombre 
# edad 
# curso 
# nota_media 
# faltas


# El programa debe: 
# - Mostrar todos los datos del alumno. 
# - Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5. 
# - Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas. 
# - Mostrar un mensaje final combinando el resultado académico y el aviso por faltas. 
# Condición: Debe utilizar diccionarios, if, elif, else y operadores lógicos.


print("solucion ejercicio 3")

alumno = {
    "nombre": "Alex",
    "edad":21,
    "curso": "IA+BD",
    "nota_media":10,
    "faltas":0
}

for key, value in alumno.items(): # con .items podemos ver las keys y los values
    
    print(key, ":", value)



if (alumno["nota_media"] >=5 and alumno["faltas"] >=10):

    print("alumno aprobado pero con avisos")


elif (alumno["nota_media"] >=5 and alumno["faltas"] <10):

    print("alumno aprobado y sin avisos")


elif (alumno["nota_media"] < 5 and alumno["faltas"] >=10):
   
   print("alumno suspendido y con avisos")

else:
    print("alumno suspendido pero sin avisos")





# Ejercicio 4. Números pares, impares y múltiplos 
# Usando range, recorre los números del 1 al 50. 
# El programa debe: 
# - Contar cuántos números son pares. 
# - Contar cuántos números son impares. 
# - Contar cuántos números son múltiplos de 5. 
# - Mostrar los tres resultados finales. 

print("solucion ejercicio 4")

pares = 0
impares = 0
mul_5 = 0

for i in range(1, 51): # 51 para que llegue hasta 50, para saber si es par, impar o multiplo de 5 usamos %
    
    if (i % 2 == 0):
        pares = pares + 1

    else:
        impares = impares + 1

    if (i % 5 == 0):
        mul_5 = mul_5 + 1


print("numero de pares: ",pares ," impares: ",impares, " multiplos de 5: ",mul_5)




# Ejercicio 5. Validación de contraseña 
# Crea una variable llamada password con una contraseña de prueba. 
# El programa debe: 
# - Comprobar si la contraseña tiene al menos 8 caracteres. 
# - Comprobar si contiene el símbolo @. 
# - Comprobar que no sea igual a 12345678. 
# - Si cumple todas las condiciones, mostrar Contraseña válida. 
# - En caso contrario, mostrar Contraseña no válida


print("solucion ejercicio 5")

password = input("introduce una contraseña: ")

if(len(password) < 8):

    print("Contraseña no valida")

else:
    
    contiene_arroba = 0 
    # comprovamos con un for que recorre caracter por caracter si hay arriba
    for i in range(0, len(password)):

        if (password[i] == "@"):
            contiene_arroba = 1  # si la tiene cambiamos de 0 a 1

    if (contiene_arroba == 1):

        if (password != "12345678"):
            print("contraseña valida")

        else:
            print("Contraseña no valida")
    

    else: # si no tiene arroba contraseña invalida
        print("Contraseña no valida")


# Ejercicio 6. Inventario de productos 
# Crea un diccionario donde las claves sean nombres de productos y los valores sean las unidades disponibles. 
# inventario = { 
#  "ratón": 12, 
#  "teclado": 5, 
#  "monitor": 0, 
#  "cable": 25 
# }



# El programa debe: 
# - Mostrar todos los productos y sus unidades. 
# - Mostrar qué productos están agotados. 
# - Calcular cuántas unidades hay en total. 
# - Mostrar cuántos productos tienen menos de 10 unidades.

print("solucion ejercicio 6")

inventario = {  
 
 "ratón": 12, 
 "teclado": 5, 
 "monitor": 0, 
 "cable": 25 

}

print(inventario)

for key in inventario.keys(): # recorremos todas las keys de el diccionario

    if (inventario[key] == 0):
        print(key, "is agotado")

sum = 0

for value in inventario.values():
    sum = sum + value

print("total unidades: ", sum)

for key,value in inventario.items():
    if (value < 10):
        print(key, " tiene menos de 10 productos")