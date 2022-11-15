from data import *
from os import system
import time


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