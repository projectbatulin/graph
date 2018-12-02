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
<<<<<<< HEAD
def eiler(graph,rez[],x=0,y=0):
    if Nzero(graph)==0:
        return rez
    while Nzero(graph):
        while x<3:
            while y<3:
                if N[x][y]==1:
                    rez.append([x,y])
                    N[x][y]=0
                    N[y][x]=0
                    x=y
                    break
                y+=1
            
=======
Part2
code blah-blah-blah
Part3
code Ya-ya-ya-ya
>>>>>>> parent of 0916ef0... Update Eulerian path.py
