k=int(input())
intermediaio=input().split(' ')
n=int(intermediaio[0])
m=int(intermediaio[1])
resultados=[]
k=k
while not k==0:
    for x in range(k):
        resposta=input()
        if not resposta=='0':
            resposta=[int(x) for x in resposta.split(' ')]
            if resposta[0]<n and resposta[1]>m:
                resultados+=['NO']
            elif resposta[0]>n and resposta[1]>m:
                resultados+=['NE']
            elif resposta[0]<n and resposta[1]<m:
                resultados+=['SO']
            elif resposta[0]>n and resposta[1]<m:
                resultados+=['SE']
            else:
                resultados+=['divisa']
    k=int(input())
for x in resultados:
    print(x)