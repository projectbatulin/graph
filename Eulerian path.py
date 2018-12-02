N=[[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]
def Rebra(N):
    summa=0
    for x in range(len(N)):
        for y in range(len(N)):
            summa+=int(N[x][y])
    if summa==0:
        return False
    else:
        return True
def eiler(graph,rez[],x=0,y=0):
    if Rebra(graph)== False:
        return rez
    while rebra(graph):
        while x<len(graph):
            while y<len(graph):
                if N[x][y]==1:
                    rez.append([x,y])
                    N[x][y]=0
                    N[y][x]=0
                    x=y
                    break
                y+=1
            
