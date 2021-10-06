n =  int(input("prosze podac liczbe: "))

def silnia_rek(n):
    if n > 1 :
        return n * silnia_rek(n-1)
    elif n in (0, 1):
        return 1;

print(silnia_rek(n))