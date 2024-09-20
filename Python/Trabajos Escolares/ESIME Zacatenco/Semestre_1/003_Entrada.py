
# a="Hola"
# print(type(a))

# b=2
# print(type(b))

# c=1.2
# print(type(c))
# """  """
""" a= int(input("Escribe el valor del largo: "))
print(a*3)

b= float(input("Escribe el valor booleano "))
print(b)
print(a*b)

print(type(a*b)) """

#Los valores que guarda la funcion input() están siempre en tipo "str", 
# para usarlo con numeros primero hay que declarar que es un dato de tipo entero, float, etc y en sus paréntesis encerrar la función input()
#ejemplo: Declaración incorrecta: a = input("Escribe el dato ")
#Declaración correcta: a = int(input("Escribe el dato entero"))
#Otrojs ejemplos: numero_decimal = float(input("Escribe el numero decimal"))

#Ejercicio: Hacer un programa donde el usuario pueda ingresar los valores del largo y ancho de un rectángulo 
# y que el programa dspliege el perímetro y área

#Declaración de variables
largo= float(input("Escribe el largo del rectángulo: "))
ancho = float(input("Escribe el ancho del rectángulo: "))

#Ejecución de la operación y despliege de datos utilizando el formato "f" en la función print()
print(f'Perímetro = ({largo} *2) + ({ancho}*2) = {largo*2 + ancho*2:.2f} cm')
print(f'Área = {largo} * {ancho} = {largo * ancho:.2f} cm²')