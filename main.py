from functions import *
from data import *

betölt()
belepve = beleptetes()
Mentés()
if belepve == None:
    print('Hibás név vagy PIN kód.')
if belepve == True:
    valasz = ''
    while valasz != '0':
        betölt()
        valasz = menu()
        if valasz == '0':
            Kilépés()
        elif valasz == '1':
            Egyenlegmegtekintés()
        elif valasz == '2':
            Egyenlegfeltoltes()
        elif valasz == '3':
            Keszpenzfelvetel()
        elif valasz == '4':
            pass
        else:
            system('cls')
            print('Hibás válasz')
            time.sleep(1.5)
        Mentés()