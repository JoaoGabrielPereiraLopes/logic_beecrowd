numero=int(input())
if numero%2==0:
    for x in range(numero+1,numero+12):
        if x%2==1:
            print(x)
else:
    for x in range(numero,numero+11):
        if x%2==1:
            print(x)