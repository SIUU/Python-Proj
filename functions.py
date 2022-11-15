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