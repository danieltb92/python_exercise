#  Escriba una función que haya dado un número y calcule sus factores primos. La función debe devolver una lista con los números primos que se descomponen el número n.
def factores(n):
  vecf=[]
  fac=2
  while fac <= n:
    if not (n % fac != 0):
      vecf.append(fac)
      n/=fac
    else:
      fac+=1
  return vecf

factores(100)