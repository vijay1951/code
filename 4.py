
def form(arr,i,j):
    if arr[i][j]==0:
            if len(tl)==0:
                topl.append(i)
                topl.append(j)
            else:
                topl[0]=min(i,topl[0])
                topl[1]=min(j,topl[1])
            if len(tr)==0:
                topr.append(i)
                topr.append(j)
            else:
                topr[0]=min(i,topr[0])
                topr[1]=max(j,topr[1])
            if len(bottoml)==0:
                bottoml.append(i)
                bottoml.append(j)
            else:
                bottoml[0]=max(i,bottoml[0])
                bottoml[1]=min(j,bottoml[1])
            if len(bottomr)==0:
                bottomr.append(i)
                bottomr.append(j)
            else:
                bottomr[0]=max(i,bottomr[0])
                bottomr[1]=max(j,bottomr[1])
arr=[]
for i in range(256):
    l1=list(map(int,input().split(" ")))
    arr.append(l1)
topl=[]
topr=[]
bottoml=[]
bottomr=[]
for i in range(256):
    for j in range(256):
        form(arr,i,j)
print(tuple(topl),tuple(topr),tuple(bottoml),tuple(bottomr))
