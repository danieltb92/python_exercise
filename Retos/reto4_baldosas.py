def leer_datos():
    n, k =[int(x) for x in list (input().split(" "))]
    baldosa = [int(x) for x in list (input().split(" "))]
    return n, k, baldosa
n, k, baldosa = leer_datos()


def verificar_fallas(baldosa, k):
  fallas_totales = 0
  fallas_detectadas = 0
  diccionario = dict()
  for count, value in enumerate(baldosa):
    if (value in diccionario and count - diccionario.get(value) <= k):
      fallas_detectadas += 1
    if (value in diccionario):
      fallas_totales += 1
    diccionario[value] = count 
  return fallas_totales, fallas_detectadas

fallas_totales, fallas_detectadas = verificar_fallas(baldosa, k)
print(fallas_totales, fallas_detectadas, len(baldosa))
