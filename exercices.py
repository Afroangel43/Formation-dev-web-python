def fibo(x):

    x=int
    x[0]=0
    x[1]=1

    x=int(input("Entrez un nombre: "))

    for i in x:
        x[i]=x[i-1]+x[i-2]

        print(x[i])

    
