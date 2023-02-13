from MinuMoodul import *

palgad=[1200,2500,750,395,2500,470,3000,1900,1990]
inimesed=["A","B","C","L","A","G","Z","D","i"]

while True:
    print()
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n 1-Lisa andmed\n 2-Kustuta andmed\n 3-Otsin Suurim palk\n 4-Otsin minimum palk\n 5-sorteerin palgad\n 6-Otsin paarit palk\n 7-Otsin palk nime järgi\n 8-leida kõik inimesed, kelle palk on suurem/väiksem kui sisestatud palk.\n 9-näidata 3 väikseimat ja suurimat palka\n 10-Arvutab keskmise palga ja selle saaja nime.\n 11-Arvutage töötasu, mida inimene saab pärast tulumaksu arvutamist.\n 0-Break"))
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
       inimesed,palgad =every3(inimesed,palgad)


