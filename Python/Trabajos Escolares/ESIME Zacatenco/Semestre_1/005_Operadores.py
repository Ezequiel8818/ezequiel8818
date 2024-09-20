"""
*Operadores Lógicos
"""


a = int(input("Ingresa un número sin su parte decimal: "))
b = int(input("Ingresa un número sin su parte decimal: "))

c = a+b
d = a-b
e = a*b
f = a/b
g = a//b
h = a%b
i = a**b

# \t es un formato de tabulación horizontal
print( ' a       =',a,'\ttype(a)       =', type(a))
print( '      b  =',b,'\ttype(b)       =', type(b))
print( ' a +  b  =',c,'\ttype(a + b)   =', type(c))
print( ' a -  b  =',d,'\ttype(a -  b)  =', type(d))
print( ' a *  b  =',e,'\ttype(a *  b)  =', type(e))
print(f' a /  b  ={f:.2f}\ttype(a /  b)  = {type(f)}')
print( ' a // b  =',g,'\ttype(a // b)  =', type(g))
print( ' a %  b  =',h,'\ttype(a %  b)  =', type(h))
print( ' a ** b  =',i,'\ttype(a ** b)  =', type(i))


#Ahora para datos tipo float
a = float(input("Ingresa un número sin su parte decimal: "))
b = float(input("Ingresa un número sin su parte decimal: "))

c = a+b
d = a-b
e = a*b
f = a/b
g = a//b
h = a%b
i = a**b

print( ' a       =',a,'\ttype(a)       =', type(a))
print( '      b  =',b,'\ttype(b)       =', type(b))
print( ' a +  b  =',c,'\ttype(a + b)   =', type(c))
print( ' a -  b  =',d,'\ttype(a -  b)  =', type(d))
print( ' a *  b  =',e,'\ttype(a *  b)  =', type(e))
print(f' a /  b  ={f:.2f}\ttype(a /  b)  = {type(f)}')
print( ' a // b  =',g,'\ttype(a // b)  =', type(g))
print( ' a %  b  =',h,'\ttype(a %  b)  =', type(h))
print( ' a ** b  =',i,'\ttype(a ** b)  =', type(i))


#Siempre las imprtanciones van al inicio del codigo

import os #libreria para modificar los archivos
import math

os.system('cls') #borra todo lo que se ejecutó hasta ese momento

grados = float(input('Ingresa un ángulo en grados: '))

radianes = grados * math.pi / 180

seno= math.sin(radianes)
coseno= math.cos(radianes)
tangente= math.tan(radianes)

cotangente= math.atan(radianes)
secante= math.acos(radianes)
cosecante=math.asin(radianes)



