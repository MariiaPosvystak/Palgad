from multiprocessing import Value


p=[]
i=[]

#1
def valik_1(p:list, i:list):
    """
    """
    while True:
        try:
            kogus=int(input("Сколько людей ты хочешь добавить: "))
            break
        except ValueError:
            print("Kogus on arv!")
    for k in range(kogus):
        while True:
            try:
                nimi=input("Sisesta nimi: ")
                if nimi.isalpha():break
            except:
                print("Имя должно состоять только из букв!")
        while True:
             try:
                palk=float(input("Введите его зарплату: "))
                break
             except ValueError:
                print("Palk on arv!")
    p.append(palk)
    i.append(nimi)
    print("Человек добавлен!")

#2
def valik_2(p:list, i:list):
    """
    """
    while 1:
        try:
            nimi=str(input("Sisesta nimi: "))
            if nimi.isalpha():
                if nimi in i:
                    break
                else:
                    print("Имени нет в списке!(имя должно быть в списке)")
        except:
            print("Имя лоджно состоять из букв!")
    k=i.count(nimi)
    if k>0:
        for j in range(k):
            ind=i.index(nimi)
            i.pop(ind)
            i.pop(ind)
            print("Имя удалено из списка")

#3
def valik_3(p:list, i:list):
    """
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
    """
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
    """
    """
    v=input("Vali märk: > (kasvav) või < (kahanev)")
    for n in range(0, len(i)):
        for m in range(n, len(i)):
            if eval (str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    print(i, p)

#6
def valik_6(p:list, i:list):
    """
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

#7
def valik_7(p:list, i:list):
    """
    """
    while True:
        try:
            nimi=input("Sisetsa nimi: ")
            if nimi.isalpha():
                break
        except:
            print("Имя должно быть из букв!")
    k=i.count(nimi)
    if k>0:
        for ind in range(len(i)):
            if i[ind]==nimi:
                print(i[ind], p[ind])

#8
