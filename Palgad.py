from module1 import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

print("Palgad")
print("MENU\n",
      "1. Lisada mitu inimest ja nende palgad;\n",
      "2. Isiku ja tema palga kustutada(nimi sisestab kasutaja);\n",
      "3. Leida kes saab kätte suurim palk;\n",
      "4. Leida kes saab kätte kõige väiksem palk ja milline ta on;\n",
      "5. Järjestada palgad kasvavas ja kahanevas järjekorras koos nimedega;\n",
      "6. Teada saada, kes saavad võrdset palka, leida, kui palju neid on ja kuvada nende andmed ekraanile;\n",
      "7. Teha palgaotsing isiku nime järgi. Pange tähele, et nimed võivad korduda;\n",
      "",
      "20. Väljumine.")
while 1:
    try:
        valik=int(input("Valik: "))
        if valik==1:
            valik_1(palgad, inimesed)
        elif valik==2:
            valik_2(palgad, inimesed)
        elif valik==3:
            valik_3(palgad, inimesed)
        elif valik==4:
            valik_4(palgad, inimesed)
        elif valik==5:
            valik_5(palgad, inimesed)
        elif valik==6:
            valik_6(palgad, inimesed)
        elif valik==7:
            valik_7(palgad, inimesed)
        elif valik==20:
            break
    except ValueError:
        print("valik on arv!")
   
