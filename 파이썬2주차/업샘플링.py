
exbig1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print('올릴 배율을 선택하세요')
K=int(input('세로> '))
L=int(input('가로> '))

ex=[[0,1],[1,0]]

for k in range(len(ex)):
    for b in range(len(ex[k])):
        print(ex[k][b],end=' ')
    print()

for i in range(len(ex)):
    for j in range(len(ex[i])): 
        exbig1[i*K][j*L]=ex[i][j]
        exbig1[i*K][j*L+1]=ex[i][j]
        exbig1[i*K+1][j*L]=ex[i][j]
        exbig1[i*K+1][j*L+1]=ex[i][j]

for k in range(len(exbig1)):
    for b in range(len(exbig1[k])): 
        print(exbig1[k][b],end=' ')
    print()

ex2=[[1,0,1],[0,0,0],[1,0,1]]

exbig2=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

print('올릴 배율을 선택하세요')
K=int(input('세로> '))
L=int(input('가로> '))

for i in range(len(ex2)):
    for j in range(len(ex2[i])): 
        exbig2[i*K][j*L]=ex2[i][j]
        exbig2[i*K][j*L+1]=ex2[i][j]
        exbig2[i*K][j*L+2]=ex2[i][j]

        exbig2[i*K+1][j*L]=ex2[i][j]
        exbig2[i*K+1][j*L+1]=ex2[i][j]
        exbig2[i*K+1][j*L+2]=ex2[i][j]
        
        exbig2[i*K+2][j*L]=ex2[i][j]
        exbig2[i*K+1][j*L+1]=ex2[i][j]
        exbig2[i*K+2][j*L+2]=ex2[i][j]

for k in range(len(exbig2)):
    for b in range(len(exbig2[k])): 
        print(exbig2[k][b],end=' ')
    print()
