distMet, velMax, tiempSeg, = input () .split()
distMet = float(distMet)
velMax= float(velMax)
tiempSeg= float(tiempSeg)
vel_Media= (distMet / 1000) / (tiempSeg / 3600)

if vel_Media < velMax: 
  print ("OK")
elif vel_Media < (velMax*1.2):
    print ("MULTA")
elif (distMet < 0 or velMax < 0 or tiempSeg < 0):
      print ("ERROR")
else: print ("CURSO SENSIBILIZACION")