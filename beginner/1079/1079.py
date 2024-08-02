valores=[]
for x in range(int(input())):
        valores+=[[round(float(x),1) for x in input().split(' ')]]
for x in valores:
    media=(x[0]*2 + x[1]*3 + x[2]*5)/10
    print(round(media,1))