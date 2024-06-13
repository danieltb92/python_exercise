Sal, HoraExt, Bon, = input () .split()
Sal= float(Sal)
Bon= int(Bon)
HoraExt= float(HoraExt)
UnaHorTra= Sal/192
ValorHorTra= UnaHorTra*HoraExt
RecarHorExt= ValorHorTra*1.25
Bonifi= Sal*0.05
if Bon<1: 
  Bonifi= 0
else: Bonifi= Bonifi
SalTotalSin= Sal+RecarHorExt+Bonifi
SalTotalCon= SalTotalSin-((SalTotalSin*0.035)+(SalTotalSin*0.04)+(SalTotalSin*0.01))
print(round(SalTotalCon,1))