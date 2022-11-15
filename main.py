from functions import *
from data import *

betölt()
belepve = beleptetes()
print(belepve)
Mentés()
if belepve == True:
    betölt()
    valasz = ''
    while valasz != '0':
        valasz = menu()
        if valasz == '0':
            Kilépés()
        elif valasz == '1':
            pass
        elif valasz == '2':
            pass
        elif valasz == '3':
            pass
        elif valasz == '4':
            pass
        Mentés()