def userchoice():
    n = raw_input("Entrer le nombre max de la suite : ")
    try:
        n = int(n)
        if n < 2:
            n = raw_input("Entrer le nom max de la suite supérieur ou égale à deux ")
            userchoice()
    except:
        userchoice()
    return int(n)


def fibo(a):
    tab=range(0,a)
    tab[0]=1
    tab[1]=1

    for i in range(2,a) :
        tab[i] = tab[i-1] + tab[i-2]

    for i in range (0,a):
        print tab[i] 

fibo(userchoice())
