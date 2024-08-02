intermediaio=input().split(' ')
print(intermediaio)
n=int(intermediaio[0])
m=int(intermediaio[1])
resultados=[]
resposta=''
while not resposta=='0':
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
for x in resposta:
    print(x)