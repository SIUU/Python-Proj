file = 'data.csv'
Név = []
Pin = []
Számlaszám = []
Egyenleg = []
címsor = ''

def betölt():
    with open(file,'r', encoding='utf-8') as forras:
        global címsor
        címsor = forras.readline()
        for row in forras:
            halmaz = row.split(';')
            Név.append(halmaz[0])
            Pin.append(halmaz[1])
            Számlaszám.append(halmaz[2])
            Egyenleg.append(halmaz[3].strip())

def Mentés():
    with open(file, 'w', encoding='utf-8') as cel:
        cel.write(címsor)
        for i in range(len(Név)):
            cel.write(f'{Név[i]};{Pin[i]};{Számlaszám[i]};{Egyenleg[i]}\n')
        Név.clear()
        Pin.clear()
        Számlaszám.clear()
        Egyenleg.clear()

