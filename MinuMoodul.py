
def Lisa_andmed(i:list,p:list):
    """Choose name and add it for list 
    ::param: List i: Inimeste jдrjend
    ::param: List p: Palgade jдrjend
    :rtype: list, list
    """
    n=int(input("Mittu innimest"))
    for j in range (n):
        nimi=input("Siseta nimi")
        palk=int(input("Siseta palka"))
        i.append(nimi)
        p.append(palk)
    return i,p


def  Kusutamine(i:list,p:list):
    """Choose name and delete it from list
    ::param: List i: Inimeste jдrjend
    ::param: List p: Palgade jдrjend
    :rtype: list, list
    """
    nimi=input("Siseta nimi")
    n=i.count(nimi)
    if nimi in i:
        n=i.count(nimi)
        for jj in range (n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
    return i,p
    

def maksimum(i:list,p:list):
    """Found max Palg
    ::param: List i: Inimeste jдrjend
    ::param: List p: Palgade jдrjend
    :rtype: int, str
    """

    palk = max(p)
    n = p.count(palk)
    nimi = []
    if palk in p:
        for jj in range(n):
            ind = p.index(palk)
            nimi.append(i[ind])
            p[ind] = -1

    return palk, nimi




def minimum(i:list,p:list):
    """Found min Palg
    ::param: List i: Inimeste jдrjend
    ::param: List p: Palgade jдrjend
    :rtype: int, str
    """

    palk = min(p)
    n = p.count(palk)
    nimi = []
    if palk in p:
        for jj in range(n):
            ind = p.index(palk)
            nimi.append(i[ind])
            p[ind] = -1

    return palk, nimi


def Sorteerimine(i:list,p:list):
    """Found min Palg
    ::param: List i: Inimeste jдrjend
    ::param: List p: Palgade jдrjend
    :rtype: int, str
    """
    v=int(input("palk 1-kananeb, 2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi =p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi =i[j]
                    i[j]=i[k]
                    i[k]=abi
    else:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                   abi =p[j]
                   p[j]=p[k]
                   p[k]=abi
                   abi =i[j]
                   i[j]=i[k]
                   i[k]=abi
    return i,p

def doubl(i:list,p:list):
    """Found min Palg
    ::param: List i: Inimeste jдrjend
    ::param: List p: Palgade jдrjend
    :rtype: int, str
    """
    dublikatid=[x for x in p if p.count(x)>1]
    dublikatid =list(set(dublikatid))
    for palk in dublikatid:
        n=p.count(palk)
        k=-1
        print(f"{palk} saavad kдtte jдrgmised inimesed")
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi)

    
def palkbynimi(i:list, p:list):
    """
    Leiab isiku palga tema nime alusel
    ::param: List i: Inimeste jдrjend
    ::param: List p: Palgade jдrjend
    :::rtype: int, str
    """
    nim=input("Print nimi")
    list1 = []
    for jj in range(len(i)):
        if i[jj] == nim:
            list1.append(p[jj])
    
    print (f"{nim} palgad on {list1} ") 


def palgadfilter(i:list, p:list):
    """
    leida kхik inimesed, kelle palk on suurem/vдiksem kui sisestatud palk.
    ::param: List i: Inimeste jдrjend
    ::param: List p: Palgade jдrjend
    :::rtype: int, str
    """
    v=int(input("palk 1-surem, 2-vдhem?"))
    palk1=int(input("print palk"))
    list1 = []
    if v ==1:
        for jj in range(len(i)):
            if palk1<p[jj]:
                list1.append((i[jj], p[jj]))
        print(f"kхik inimesed, kes teenivad rohkem kui {palk1} on {list1}")
    elif v ==2:
        for jj in range(len(i)):
            if palk1>p[jj]:
                list1.append((i[jj], p[jj]))
        print(f"kхik inimesed, kes teenivad vдhem kui {palk1} on {list1}")
  
def top3 (i:list, p:list):
    """
    nдidata 3 vдikseimat ja suurimat palka
    ::param: List i: Inimeste jдrjend
    ::param: List p: Palgade jдrjend
    :::rtype: int, str
    """
    list1=[0,0,0]

    ii=len(i)+1
    for jj in range (ii):
        if list1[0] +list1[1] +list1[2] < list1[1] +list1[2] + p[jj-1]:
            list1.remove(min(list1))
            list1.append(p[jj-1])
    print(f"suurem kolm on {list1}")
    for gg in range (len(i)):
        if list1[0] +list1[1] +list1[2] > list1[1] +list1[2] + p[gg]:
                list1.remove(max(list1))
                list1.append(p[gg])
    print(f"vдiksem kolm on {list1} ")

def average(i: list, p: list):
    """
    Calculates the average salary and the name of the person who receives it.
    :param: List i: People's list
    :param: List p: Salaries list
    """
    total = sum(p)
    keskmine = total / len(p)
    print(keskmine)
    if keskmine in p :
        index = p.index(keskmine)
        nimi = i[index]
        print(f"{nimi} on keskmine palka ")
    else:
        p.append (keskmine)
        index = p.index(keskmine)
        KES = input("print keskmise palgaga isiku nimi")
        i.insert(index,KES)
        nimi = i[index]
        print(f"{nimi} on keskmine palka ")

def Tulumaks(i: list, p: list):
    """
    Arvutage tццtasu, mida inimene saab pдrast tulumaksu arvutamist.
    :param: List i: People's list
    :param: List p: Salaries list
    :rtype: float, str
    """
    print(i)
    nimi = int(input("Valige selle isiku ametikoht, kelle palka soovite teada saada: "))
    nimi2 = nimi - 1
    palg = p[nimi2]
    if palg <= 1200:
        palg = palg - 654
        if palg < 0:
            palg = 0
            palg += p[nimi2]
            print(f"{palg}")
        else:
            palg = palg * 0.8

            palg += 654


            print(f"{palg}")
    elif palg > 1200 and palg < 2100:
        tulemaks = 500-0.55556*(palg-1200)
        palg = palg-tulemaks
        palg = palg * 0.8
        palg += tulemaks
        palg= round(palg,1)
        print(f"{palg}")
    else:
        palg=palg*0.8
        print(f"{palg}")



        

def nimisorter (p: list, i: list):
    """
    Arvutage tццtasu, mida inimene saab pдrast tulumaksu arvutamist.
    :param: List i: People's list
    :param: List p: Salaries list
    :rtype: float, str
    """
    v=int(input("if we want sorter A-Z print 1; Z-A print 2"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi =p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi =i[j]
                    i[j]=i[k]
                    i[k]=abi
    else:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                   abi =p[j]
                   p[j]=p[k]
                   p[k]=abi
                   abi =i[j]
                   i[j]=i[k]
                   i[k]=abi
    return i,p




def deleate_maloimushii (i: list,p: list):
    copy = p.copy()
    copyi= i.copy()
    total = sum(p)
    keskmine = total / len(p)
    print(keskmine)
    v=int(input("palk 1-surem, 2-vдhem?"))
    if v == 1:
        for palk in p:
            if palk>keskmine:
                ind=copy.index(palk)
                copy.remove(palk)
                copyi.pop(ind)
                print (f"{copy},{copyi}")
    else:
        for palk in p:
            if palk<keskmine:
                ind=copy.index(palk)
                copy.remove(palk)
                copyi.pop(ind)


def redakt (i: list,p: list):
    copyi= i.copy()
    copyp = []
    upper = [a.isupper()for a in copyi]
    if upper != True: 
        copyi = [word.upper() for word in copyi]
        i = copyi.copy()
        
    for jj in range(len(p)):
       g =int(p[jj])
       copyp.append(g)
       print (g)
    p=copyp
    return i,p


def plussmoney (i: list,p: list):
    years = int(input("how many years"))
    while years > 0:
        years -= 1
        copyp=[]
        for jj in range(len(p)):
           float(p[jj])
           p[jj]+=(p[jj]*0.05)
           rez = p[jj]
           float(rez)
           copyp.append(rez)
    return i,p


def every3(i: list, p: list):
    for jj in range(len(i)):
        if (jj + 1) % 3 == 0:
            replace = input("print any name: ")
            i[jj] = replace
    return i, p


def foundtulumakls (i: list,p: list):
    print(i)
    nimi = int(input("Valige selle isiku ametikoht, kelle palka soovite teada saada: "))
    nimi2 = nimi - 1
    palg = p[nimi2]
    if palg <= 1200:
        palg = palg - 654
        if palg < 0:
            print(f"{i[nimi2]} ei ole tulumaks")
        else:
            palg2 = palg * 0.8
            tulumaks=palg-palg2
            tulumaks=round(tulumaks,1)
            print(f"{i[nimi2]} tulumaks on {tulumaks}")
    elif palg > 1200 and palg < 2100:
        eitulumaks = 500-0.55556*(palg-1200)
        palg = palg-eitulumaks
        palg2 = palg * 0.8
        tulumaks=palg-palg2
        tulumaks=round(tulumaks,1)
        print(f"{i[nimi2]} tulumaks on {tulumaks}")
    else:
        palg2 = palg * 0.8
        tulumaks=palg-palg2
        tulumaks=round(tulumaks,1)
        print(f"{i[nimi2]} tulumaks on {tulumaks}")




        



            
               
        

