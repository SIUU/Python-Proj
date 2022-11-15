from data import *
from os import system
import time
index = -1

def menu():
    choice = ''
    system('cls')
    print('0 - Kilép')
    print('1 - Egyenleg megtekintése')
    print('2 - Egyenlegfeltöltés')
    print('3 - Készpénzfelvétel')
    print('4 - Átutalás')
    choice = input('Válasszon egy menüpontot: ')
    return choice

def beleptetes():
    system('cls')
    bekertNev = input('Kérem a nevét: ')
    bekertPin = input('Kérem a PIN kódját: ')
    for i,nevek in enumerate(Név):
        if bekertNev == nevek:
            if bekertPin == Pin[i]:
                global index
                index = i
                return True


def Kilépés():
    system('cls')
    print("Kilépés.")
    time.sleep(0.5)
    system('cls')
    print("Kilépés..")
    time.sleep(0.5)
    system('cls')
    print("Kilépés...")
    time.sleep(0.5)
    system('cls')

def Egyenlegmegtekintés():
    system('cls')
    print(f'Az ön egyenlege: {Egyenleg[index]}')
    input('\nNyomjon ENTERT a továbblépéshez!')

def Egyenlegfeltoltes():
    system('cls')
    bekertOsszeg = input('Adja meg a feltölteni kívánt összeget: ')
    if int(bekertOsszeg) > 0:
        Egyenleg[index] = int(Egyenleg[index]) + int(bekertOsszeg)
        print('Sikeres tranzakció')
        time.sleep(1.5)
    else:
        system('cls')
        print('Írjon be egy létező összeget')
        time.sleep(1.5)

def Keszpenzfelvetel():
    system('cls')
    lekertOsszeg = input('Adja meg a felvenni kívánt összeget: ')
    if not int(lekertOsszeg) > int(Egyenleg[index]):
        Egyenleg[index] = int(Egyenleg[index]) - int(lekertOsszeg)
        print('Sikeres tranzakció')
        time.sleep(1.5)
    else:
        system('cls')
        print('A bankszámnlán nincs elég pénz a tranzakcióhoz.')
        time.sleep(1.5)