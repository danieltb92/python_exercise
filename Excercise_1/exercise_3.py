x=0
num= int(input("escriba un numero" ))
while num < 100:
  sum= x + num
  num= int(input("escriba un numero" ))
print (sum)


#Funciones for y in

for x in "banana":
  print (x)


print ("comienzo")
for i in ["Alva", "Amigo", 1]:
  print(f"Hola ahora",{i})


for num in range (6):
  print (num)


for x in range (2, 30, 3):
  print ("\t",(x),end="")


estd= float(input())
n= float(input())

# Operaciones con String
mensaje1= "hola " *3
mensaje2= "Mundo "
print (mensaje1 + mensaje2)


# Codigo ASCII y UNICODE
# Funcion ord
print (ord("a"))


string= "Python!"
for ch in string:
  print (ch + "=" + str(ord(ch)))

# Funcion Subcadena: slice
frase="Curso de Python"
frase[0:5]
frase[0:15:2]
frase[:5]
frase[6:]
frase[6::3]


# Funciones len,count,find
frase="Curso de Python"
x=len(frase)
y=frase.count("o")
z=frase.count("o",0,8)
w=frase.find("rso")
print(x)
print(y)
print(z)
print(w)


# Funciones 
frase="Curso de Python"
x=frase.upper()
y=frase.lower()
print(x)
print(y)