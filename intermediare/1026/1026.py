entrada=[int(x) for x in input().split(' ')]
entrada=[str(bin(x))[2::] for x in entrada]
resultado=''
for x in range(0,2):
    inicio=''
    while len(entrada[x])<32:
        entrada[x]='0'+entrada[x]
for x in range(1,32):
    if int(entrada[0][x])+int(entrada[1][x])==1:
        resultado+='1'
    else:
        resultado+='0'
saida=0
for x in range(len(resultado)-1,-1,-1):
    saida+=int(resultado[x])*2**(len(resultado)-x-1)
print(saida)