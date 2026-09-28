

# Ejercicio 1. Listas: control de notas
# - Crea una lista llamada notas con cinco calificaciones: 6, 8, 5, 9 y 7.
# - Guarda en una variable primera_nota el primer elemento de la lista.
# - Guarda en una variable ultima_nota el último elemento de la lista.
# - Cambia la segunda nota de la lista por un 10.
# - Añade una nueva nota, 8, al final de la lista.
# - Guarda en una variable total_notas la cantidad de notas que hay en la lista.
# - Muestra por consola la lista final, la primera nota, la última nota y el total de notas


print("\n")
print("solucion de el ejercicio 1")
notas =  [ 6, 8, 5, 9, 7]

primera_nota = notas[0]
ultima_nota = notas[4]
notas[1] = 10
notas.append(8)
total_notas = len(notas)


print(primera_nota)
print(ultima_nota)
print(total_notas)
print(notas)

# Ejercicio 2. Tuplas: datos fijos de un producto
# - Crea una tupla llamada producto con tres datos: nombre del producto, precio y unidades disponibles.
# - Por ejemplo: ("teclado", 25.50, 12).
# - Guarda cada dato de la tupla en una variable diferente: nombre, precio y unidades.
# - Calcula el valor total del stock multiplicando precio por unidades.
# - Muestra por consola el nombre del producto, el precio, las unidades y el valor total del stock.


print("\n")
print("solucion de el ejercicio 2")
producto = ("teclado", 25.50,12)
nombre = producto[0]
precio = producto[1]
unidades = producto[2]
stock = precio*unidades

print(nombre)
print(precio)
print(unidades)
print(stock)


# Ejercicio 3. Diccionarios: ficha de alumno
# - Crea un diccionario llamado alumno.
# - El diccionario debe tener estas claves: nombre, edad, curso y nota.
# - Usa valores concretos, por ejemplo: "Ana", 16, "IA" y 7.5.
# - Muestra por consola el nombre del alumno usando la clave nombre.
# - Muestra por consola la nota del alumno usando la clave nota.
# - Cambia la nota del alumno por otro valor.
# - Añade una nueva clave llamada aprobado. Su valor debe ser el resultado de comprobar si la nota es mayor o igual que 5.
# - Muestra por consola el diccionario completo al final.

print("\n")
print("solucion de el ejercicio 3")
Alumno = {
    "nombre":"Ana",
    "edad":16,
    "curso":16,
    "nota":7.5
}

print(Alumno["nombre"])
print(Alumno["nota"])
Alumno["nota"] = 10
# para decidir si esta aprobado o no usamos un booleano falso/true

Alumno["aprobado"] = True


# Ejercicio 4. Conjuntos: usuarios registrados
# - Crea un conjunto llamado usuarios con estos nombres: Ana, Luis, Marta, Ana y Pedro.
# - Crea una variable nuevo_usuario con el valor "Luis".
# - Crea una variable usuario_existe que compruebe si nuevo_usuario está dentro del conjunto.
# - Añade el usuario "Clara" al conjunto.
# - Crea una variable total_usuarios con el número de usuarios únicos.
# - Muestra por consola el conjunto final, usuario_existe y total_usuarios.

print("\n")
print("solucion de el ejercicio 4")
usuarios = {"Ana", "Luis", "Marta", "Ana", "Pedro"}

nuevo_usuario = "Luis"

usuario_existe = nuevo_usuario in usuarios

usuarios.add("Clara")

total_usuarios = len(usuarios)
print(usuarios)
print(usuario_existe)

print(total_usuarios)


# Ejercicio 5. Condiciones con and, or y not
# - Crea las variables edad, tiene_permiso, es_socio y sancionado.
# - Asigna valores concretos a esas variables.
# - Crea una variable acceso_por_edad que sea True si la persona tiene al menos 16 años y tiene permiso.
# - Crea una variable acceso_por_socio que sea True si la persona es socio y no está sancionada.
# - Crea una variable puede_acceder que sea True si se cumple acceso_por_edad o acceso_por_socio.
# - Muestra por consola las tres variables: acceso_por_edad, acceso_por_socio y puede_acceder.

print("\n")
print("solucion de el ejercicio 5")
edad = 22
tiene_permiso = True
es_socio = False
sancionado = False

acceso_por_edad = edad >= 16 and tiene_permiso == True
acceso_por_socio = es_socio and not sancionado == True # ponemos el not aqui para que de true pase a false la comparacion
puede_acceder = acceso_por_edad or acceso_por_socio

print(acceso_por_edad)
print(acceso_por_socio)
print(puede_acceder)


# Ejercicio 6. if, elif y else: clasificación de matrícula
# - Crea las variables nota_media, renta_baja y familia_numerosa.
# - Asigna valores concretos a esas variables.
# - Crea una variable mensaje.
# - Si la nota_media es menor que 5, mensaje debe ser No admitido.
# - Si la nota_media es mayor o igual que 9, mensaje debe ser Beca completa.
# - Si la nota_media es mayor o igual que 7 y además renta_baja o familia_numerosa es True, mensaje debe ser Beca parcial.
# - Si la nota_media es mayor o igual que 5, mensaje debe ser Admitido sin beca.
# - En cualquier otro caso, mensaje debe ser Revisar solicitud.
# - Muestra por consola el valor final de mensaje.

print("\n")
print("solucion de el ejercicio 6")
nota_media = 6
renta_baja = True
familia_numerosa = False
mensaje = ""

if (nota_media < 5):
  mensaje = "No admitido"

elif (nota_media >=9):
  mensaje = "Beca completa"
elif (nota_media >= 7 and (renta_baja == True or familia_numerosa == True)):
  mensaje = "Beca Parcial"
elif(nota_media >=5):
  mensaje = "Admitido sin beca"

print(mensaje)


# Ejercicio 7. Ternaria: mensaje de resultado
# - Crea una variable nota con un valor numérico.
# - Usa un condicional ternario para guardar en resultado el texto Aprobado si la nota es mayor o igual que 5, o Suspenso en caso contrario.
# - Usa otro condicional ternario para guardar en tipo_nota el texto Alta si la nota es mayor o igual que 8, o Normal en caso contrario.
# - Muestra por consola la nota, el resultado y el tipo de nota.


print("\n")
print("solucion de el ejercicio 7")
nota = 7

resultado = "Aprobado" if nota >=5 else "Suspenso"
tipo_nota = "Alta" if nota >=8 else "Normal"

print(nota)
print(resultado)
print(tipo_nota)


# Ejercicio 8. match-case: menú de aplicación
# - Crea una variable opcion con un texto: crear, editar, borrar, listar u otra opción.
# - Crea una variable mensaje.
# - Usa match-case para asignar un mensaje distinto según la opción elegida.
# - Si opcion es "crear", mensaje debe ser Creando registro.
# - Si opcion es "editar", mensaje debe ser Editando registro.
# - Si opcion es "borrar", mensaje debe ser Borrando registro.
# - Si opcion es "listar", mensaje debe ser Mostrando registros.
# - Para cualquier otro valor, mensaje debe ser Opción no reconocida.
# - Muestra por consola el valor de mensaje.


print("\n")
print("solucion de el ejercicio 8")

opcion = input(" crear, editar, borrar, listar u otra opción ")
mensaje = ""
match opcion:
  case "crear":
    mensaje = "Creando registro"

  case "editar":
    mensaje = "Editando registro"

  case "borrar":
    mensaje = "Borrando registro"

  case "listar":
    mensaje = "Mostrando registro"

  case _:
    mensaje = "opcion no reconocida"

print(mensaje)


# Ejercicio 9. Caso completo: pedido online
# - Crea una lista llamada productos con tres productos.
# - Crea una lista llamada precios con tres precios, en el mismo orden que los productos.
# - Crea un diccionario llamado cliente con las claves nombre, es_socio y saldo.
# - Crea un conjunto llamado cupones_validos con tres códigos de cupón.
# - Crea una variable cupon_usado con uno de esos códigos o con un código inventado.
# - Calcula el total del pedido sumando los tres precios.
# - Crea una variable tiene_descuento que sea True si el cliente es socio o si el cupón usado está en cupones_validos.
# - Si tiene_descuento es True, calcula total_final aplicando un descuento del 10%. Si no, total_final será igual al total.
# - Si el saldo del cliente es mayor o igual que total_final, el mensaje será Pedido aceptado. En caso contrario, será Saldo insuficiente.
# - Muestra por consola el nombre del cliente, productos, total_final y mensaje.

print("\n")
print("solucion de el ejercicio 9")


productos = ["producto1","producto2","producto3"]

precios = [20,30,40]

cliente = { "nombre": "Alex",
           "es_socio":True,
            "saldo":1200}

cupones_validos = {100,200,300}
cupon_usado = 150
pedido = precios[0]+precios[1]+precios[2]

tiene_descuento = cliente["es_socio"] or cupon_usado in cupones_validos

if (tiene_descuento == True):
  total_final = pedido-pedido*0.1 # esto equivale a restar un 10%

else:
  total_final = pedido

if (total_final < cliente["saldo"]):
  mensaje = "Pedido acceptado"

else:
  mensaje = "Saldo insuficiente"

print(cliente["nombre"])
print(productos)
print(total_final)
print(mensaje)



# Ejercicio 10. Caso completo: evaluación de acceso
# - Crea una tupla llamada requisitos con tres valores: edad mínima, nota mínima y si se requiere permiso.
# - Ejemplo: requisitos = (18, 6, True).
# - Crea un diccionario llamado candidato con las claves nombre, edad, nota y permiso.
# - Crea un conjunto llamado cursos_disponibles con tres cursos.
# - Crea una variable curso_elegido.
# - Crea una variable curso_existe que compruebe si curso_elegido está en cursos_disponibles.
# - Crea una variable cumple_edad comparando la edad del candidato con la edad mínima.
# - Crea una variable cumple_nota comparando la nota del candidato con la nota mínima.
# - Crea una variable cumple_permiso. Si el requisito de permiso es True, debe comprobarse el permiso del candidato. Si no se requiere permiso, debe valer True.
# - Usa if, elif y else para crear un mensaje final: Acceso concedido, Curso no disponible, No cumple requisitos o Solicitud incompleta.
# - Usa una ternaria para crear un estado breve: Apto si el mensaje final es Acceso concedido, o No apto en caso contrario.
# - Muestra por consola el nombre del candidato, el curso elegido, el estado breve y el mensaje final.

print("\n")
print("solucion de el ejercicio 10")

requisitos = (18,6,True)

candidato = {"nombre":"Alex", "edad":21, "nota":7, "permiso":True}

cursos_disponibles = {"curso1","curso2","curso3"}

curso_elegido = "curso4"

curso_existe = curso_elegido in cursos_disponibles

cumple_edad = candidato["edad"] >= requisitos[0]
cumple_nota = candidato["nota"] >= requisitos[1]

mensaje_final = ""

if (requisitos[2] == True):
  cumple_permiso = candidato["permiso"]

else:
  cumple_permiso = True

  if (cumple_permiso == True and curso_existe == True and cumple_edad == True and cumple_nota == True):
    mensaje_final = "Acceso concedido"

  elif(curso_existe == False):
    mensaje_final = "Curso no disponible"

  elif (cumple_edad == False or cumple_nota == False): # no queda claro en el enunciado si no cumple requisitos es para ambos o solo uno y si el else es para el otro
  # ya que curso existe si tiene mensaje personalizado, he decidido agrupar asi el elif
    mensaje_final = "No cumple requisitos"

  else:
    mensaje_final = "Solicitud incompleta"


estado_breve = "Apto" if mensaje_final == "Acceso concedido" else "No apto" # ternaria

print(candidato["nombre"])
print(curso_elegido)
print(estado_breve)
print(mensaje_final)