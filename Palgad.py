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
      "9. T vaeseimad ja rikkamad inimesed\n",
      "12. Sorteerimine nime järgi (saab anda kasutajale võimaluse valida A-st Z-ni või Z-st A-sse).\n",
      "13. Leia need, kes saavad keskmisest madalamat palka, ja eemalda nad nimekirjadest.\n",
      "14. Redigeerige nimekirju nii, et inimeste nimekirjas oleks nimed kirjutatud suure tähega, palga kohta int formaadis.\n",
      "16. „Nimetage ümber“ iga kolmas inimene. Uued nimed sisestatakse kasutaja poolt.\n",
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
        elif valik==9:
            Top(palgad, inimesed)
        elif valik==12:
            valik_12(palgad, inimesed)
        elif valik==13:
            valik_13(palgad, inimesed)
        elif valik==14:
            valik_14(palgad, inimesed)
        elif valik==16:
            valik_16(palgad, inimesed)
        elif valik==20:
            break
    except ValueError:
        print("valik on arv!")
   
