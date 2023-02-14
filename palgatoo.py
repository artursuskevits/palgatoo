from MinuMoodul import *

palgad=[1200,2500,750,395,2500,470,3000,1900,1990]
inimesed=["A","B","C","L","A","G","Z","D","i"]

while True:
    print()
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n 1-Lisa andmed\n 2-Kustuta andmed\n 3-Otsin Suurim palk\n 4-Otsin minimum palk\n 5-sorteerin palgad\n 6-Otsin paarit palk\n 7-Otsin palk nime jдrgi\n 8-leida kхik inimesed, kelle palk on suurem/vдiksem kui sisestatud palk.\n 9-nдidata 3 vдikseimat ja suurimat palka\n 10-Arvutab keskmise palga ja selle saaja nime.\n 11-Arvutage tццtasu, mida inimene saab pдrast tulumaksu arvutamist.\n 12 sorteeri nime järgi \n 13 Leidke üles need, kes teenivad alla keskmise palga, ja eemaldage nad nimekirjadest. \n 14 numbrid = int, suurtähtedega sõnad \n 15 tõsta igal aastal 5 % võrra \n 16 muuta nime üks kolmest \n 17 -leida maksude summa \n 0-Break"))
    if menu==0:
        break
    elif menu==1:
        inimesed,palgad=Lisa_andmed(inimesed,palgad)
    elif menu==2:
        inimesed, palgad=Kusutamine(inimesed,palgad)
    elif menu==3:
        palk, nimi=maksimum(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}")
    elif menu==4:
        palk, nimi=minimum(inimesed,palgad)
        print(f"Minimum palk on {palk} {nimi}")
    elif menu==5:
        inimesed, palgad=Sorteerimine(inimesed,palgad)
    elif menu==6:
       doubl(inimesed,palgad)
    elif menu==7:
       palkbynimi(inimesed,palgad)
    elif menu==8:
         palgadfilter(inimesed,palgad)
    elif menu==9:
        top3(inimesed,palgad)
    elif menu==10:
        average(inimesed,palgad)
    elif menu ==11:
        Tulumaks(inimesed,palgad)
    elif menu ==12:
        inimesed, palgad=nimisorter(inimesed,palgad)
        print(inimesed, palgad)
    elif menu==13:
       deleate_maloimushii(inimesed,palgad)
    elif menu==14:
       inimesed,palgad =redakt(inimesed,palgad)
    elif menu==15:
       inimesed,palgad = plussmoney (inimesed,palgad)
    elif menu == 16:
        inimesed,palgad = every3 (inimesed,palgad)
    elif menu == 17:
        foundtulumakls (inimesed,palgad)



