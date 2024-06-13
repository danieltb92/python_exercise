N = int(input())
listaDatos =[N]
resultado= []
for i in range(N):
  requisitos= input()
  listaDatos.append(requisitos.split(" "))

  if((int(listaDatos[i+1][0])>=240) and (int(listaDatos[i+1][0]))<=300) and \
    ((int(listaDatos[i+1][1])>=160) and (int(listaDatos[i+1][1]))<=180) and \
    ((int(listaDatos[i+1][2])>=240) and (int(listaDatos[i+1][2]))<=275) and \
    ((int(listaDatos[i+1][3]))<=50):
    resultado.append(listaDatos[i+1][4])
   
  else: 
    if not ("NO DISPONIBLE"in resultado):
     resultado.append("NO DISPONIBLE")
     
if resultado==["NO DISPONIBLE"]:
 print("NO DISPONIBLE")  
elif ("NO DISPONIBLE" in resultado) and ((resultado[0]!="NO DISPONIBLE") or \
     (resultado[1]!="NO DISPONIBLE")):
     resultado.remove("NO DISPONIBLE")
     print(resultado[0])
else: print(resultado[0])