def form(arr,i,j):
    if arr[i][j]==0:
            if len(tl)==0:
                tl.append(i)
                tl.append(j)
            else:
                tl[0]=min(i,tl[0])
                tl[1]=min(j,tl[1])
            if len(tr)==0:
                tr.append(i)
                tr.append(j)
            else:
                tr[0]=min(i,tr[0])
                tr[1]=max(j,tr[1])
            if len(bl)==0:
                bl.append(i)
                bl.append(j)
            else:
                bl[0]=max(i,bl[0])
                bl[1]=min(j,bl[1])
            if len(br)==0:
                br.append(i)
                br.append(j)
            else:
                br[0]=max(i,br[0])
                br[1]=max(j,br[1])
arr=[]
for i in range(256):
    l1=list(map(int,input().split(" ")))
    arr.append(l1)
tl=[]
tr=[]
bl=[]
br=[]
for i in range(256):
    for j in range(256):
        form(arr,i,j)
print(tuple(tl),tuple(tr),tuple(bl),tuple(br))
