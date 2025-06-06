from multiprocessing import Value

p=[]
i=[]

#1
def valik_1(p:list, i:list):
    """ Lisama inimesed ja nende palgad
    :param p: palkade nimekiri
    :param i: nimede nimekiri
    """
    while True:
        try:
            kogus=int(input("Mitu inimest soovid lisada: "))
            break
        except ValueError:
            print("Kogus on arv!")
    for k in range(kogus):
        while True:
            try:
                nimi=input("Sisesta nimi: ")
                if nimi.isalpha():break
            except:
                print("Nimi peab koosnema ainult tähtedest!")
        while True:
             try:
                palk=float(input("Sisesta tema palk: "))
                break
             except ValueError:
                print("Palk on arv!")
    p.append(palk)
    i.append(nimi)
    print("Inimene lisatud!")

#2
def valik_2(p:list, i:list):
    """ Kustutame inimese ja tema palga
    :param p: palkade nimekiri
    :param i: nimede nimekiri
    """
    while 1:
        try:
            nimi=str(input("Sisesta nimi: "))
            if nimi.isalpha():
                if nimi in i:
                    break
                else:
                    print("Nime ei ole nimekirjas! (nimi peab olema nimekirjas)")
        except:
            print("Nimi peab koosnema ainult tähtedest!")
    k=i.count(nimi)
    if k>0:
        for j in range(k):
            ind=i.index(nimi)
            i.pop(ind)
            i.pop(ind)
            print("Nimi eemaldatud nimekirjast")

#3
def valik_3(p:list, i:list):
    """ Leida kes saab kätte suurim palk
    :param p: palkade nimekiri
    :param i: nimede nimekiri
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    ind=p.index(suurim)
    for i in range(k):
        ind=p.index(suurim,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1

#4
def valik_4(p:list, i:list):
    """ Leida kes saab kätte väikseim palk
    """
    väiksem=min(p)
    print(f"Väiksem palk on {väiksem}")
    k=p.count(väiksem)
    ind=p.index(väiksem)
    for i in range(k):
        ind=p.index(väiksem,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1

#5
def valik_5(p:list, i:list):
    """ Järjestada palgad kasvavas ja kahanevas järjekorras koos nimedega
    """
    v=input("Vali märk: > (kasvav) või < (kahanev)")
    for n in range(0, len(i)):
        for m in range(n, len(i)):
            if eval (str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n] #Меняет местами зарплаты
                i[n],i[m]=i[m],i[n] #Меняет местами соответствующие имена.
    print(i, p)

#6
def valik_6(p:list, i:list):
    """ Leida, kes saavad võrdset palka, leida, kui palju neid on ja kuvada nende andmed ekraanile
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for n in range (k):
                ind=p.index(palk, ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1

#9-Top() - T vaeseimad ja rikkamad inimesed/ Т самых бедных и самых богатых человека
def Top(p: list, i: list):
    """ Valib T vaeseimad ja rikkamad inimesed
    """
    while True:
        try:
            T = int(input("Sisestage nende inimeste arv, kelle palka soovite näha: "))
            if T > 0:
                break
            else:
                print("Arv peab olema suurem kui null!")
        except ValueError:
            print("Sisesta arv!")
    combined = sorted(zip(p, i), key=lambda x: x[0])
    poorest = combined[:T]
    richest = combined[-T:]
    print(f"{T} kõige vaesemat inimest:")
    for palk, nimi in poorest:
        print(f"{nimi}: {palk}")
    print(f"{T} kõige rikkamat inimest:")
    for palk, nimi in richest:
        print(f"{nimi}: {palk}")


#12- Осуществить сортировку по имени (можно предостваит пользователю выбор от А до Я или от Я до А)
def valik_12(p: list, i: list):
    """ Sorteerib nimekirja nime järgi
    """
    order = input("Vali sorteerimise järjekord: A-Z või Z-A: ").strip().upper()
    if order == "A-Z":
        combined = sorted(zip(i, p), key=lambda x: x[0])
    elif order == "Z-A":
        combined = sorted(zip(i, p), key=lambda x: x[0], reverse=True)
    else:
        print("Vale valik! Proovi uuesti.")
        return
    i[:], p[:] = zip(*combined)
    print("Sorteeritud nimekiri:", i)


#13- Находить тех кто получает зарплату ниже средней и удалить их из списков.
def valik_13(p: list, i: list):
    """ Eemaldab nimekirjast inimesed, kelle palk on alla keskmine
    """
    if not p:
        print("Palkade nimekiri on tühi!")
        return
    avg_salary = sum(p) / len(p)
    print(f"Keskmine palk on: {avg_salary}")
    indices_to_remove = [index for index, palk in enumerate(p) if palk < avg_salary]
    for index in sorted(indices_to_remove, reverse=True):
        del p[index]
        del i[index]
    print("Uuendatud nimekiri:", i, p)


#14- Отредактировать списки таким образом, чтоб в списке людей имена были написаны с большой буквы, о зарплаты в формате int.
def valik_14(p: list, i: list):
    """ Formaatib nimed ja palgad
    """
    i[:] = [nimi.capitalize() for nimi in i]
    p[:] = [int(palk) for palk in p]
    print("Formaaditud nimekiri:", i, p)


#16 - "Переименовать" каждого третьего человека. Новые имена вводит пользователь.
def valik_16(p: list, i: list):
    """ Uuendab iga kolmanda inimese nime
    """
    for index in range(2, len(i), 3):
        new_name = input(f"Sisesta uus nimi inimesele {i[index]}: ")
        i[index] = new_name.capitalize()
    print("Uuendatud nimekiri:", i)
