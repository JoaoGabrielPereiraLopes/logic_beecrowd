entrada1=input().split(' ')
n=int(entrada1[0])
x=int(entrada1[1])
tamanhos=[x for x in input()]
escalas=[int(x) for x in input().split(' ')]
escalas={'P':escalas[0],'M':escalas[1],'G':escalas[2]}
muralhas=[x]
if escalas['P']>=x and 'P' in muralhas or escalas['M']>=x and 'M' in muralhas or escalas['G']>=x and 'G' in muralhas:
    pass
else:
    for y in tamanhos:
        suficiente=False
        for z in range(0,len(muralhas)):
            if escalas[y]<=muralhas[z]:
                muralhas[z]-=escalas[y]
                suficiente=True
                break
            else:
                pass
        if(not suficiente):
            muralhas+=[x-escalas[y]]
print(len(muralhas))