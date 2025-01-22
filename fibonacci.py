def fibonacci_sequence(n):
     if n <= 0:
        print("Le nombre de termes doit être supérieur à 0.")
        return []
                
        fibonacci_sequence=[0,1]

     for i in range(2,n):
        j=fibonacci_sequence[i-1]+fibonacci_sequence[i-2]
        fibonacci_sequence.append(j)

        print(fibonacci_sequence[j])

     fibonacci_sequence()   
