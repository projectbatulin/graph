N=[[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]
def Nzero(N):
    summa=0
    for x in range(len(N)):
        for y in range(len(N)):
            summa+=int(N[x][y])
    if summa==0:
        return False
    else:
        return True
