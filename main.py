# komentarz
'''
też komentarz ale wieloliniowy
'''

'''
ZAKRĘT
'''
from cmath import cos, tan
from math import pi, sqrt

g = 9.81
rho  = 1,225


''' TEMPLATKA FUNKCJI
<(wartość zwracana 1, w.zw. 2, ...)> [nazwa funkcji] (argumenty)
---
    opis
---
'''

'''
<promień zakrętu>  obliczPromien ()
---
    funkcja obliczająca promień zakrętu w zależności 
    od prędkości i kąta przechylenia
---
'''
def radiusCount(Vmax):
    V = range(1, Vmax, 1)
    phi = range(10, 80, 1)
    rows, cols = (len(V), len(phi))
    R = []
    for i in range(cols):
        col = []
        for j in range(rows):
            col.append(V[j]*V[j]/(g*tan(phi[i]*pi/180)))
        R.append(col)

    return (R, V, phi)

'''
<wart. V> minV(m, S, Czmax)
---
    funkcja obliczająca minimalną wartość prędkości niezbędnej do lotu
    przy ustalonym przechyleniu
---
'''
def minV (m, S, CzMax):
    phi = range(10, 80, 1)
    V = []
    for i in range(len(phi)):
        V[i] = sqrt((2*m*g)/(CzMax*cos(phi[i]*rho*S)))
    return V
'''
<współczynnik siły nośnej> obliczWspSNosnej (wek. pr, wekt, kątów, m, s, q)  
'''

'''
<moc niezbędna do zakrętu> minN (wektor prędkości, wektor mocy niezbędnej l.p., wektor kątów, )
---
    funkcja obliczająca moc niezbędną do wykonania zakrętu
---
'''

'''
<wartość wspolczynika> wspObciazen (wek. pr., masa, pow. nośna, Czmax)
---
    funckja obliczająca wartość współczynnika obciążeń samolotu podczas zakrętu
--
'''
R, V, phi = radiusCount(80)
for value in R[0]:
    print(value)
