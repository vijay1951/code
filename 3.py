def check(a) :
	for i in range(len(a)) :
		if (a[i] == '4' or a[i] == '6' or a[i] == '7') :
			return False;
	return True;

n=int(input())
count=0
l1=[]
for i in range(1,1000000):
    if (check(str(i))) :
        count+=1
        l1.append(i)
print(l1[n-1])

n=int(input())
dic={0:0,1:1,2:2,5:5,6:9,8:8,9:6}
ans=0
i=1
c=0
def valid(s):
    s1=str(s)
    s1=s1[::-1]
    res=""
    for i,v in enumerate(s1):
        if int(v) not in dic:
            return -1
        else:
            res+=str(dic[int(v)])
    return int(res)

while(c!=n):

    if i in dic:
        ans=dic[i]
        c+=1
    else:
        s1=valid(i)
        if s1!=-1:
            ans=s1
            c+=1
    i += 1
print(ans)
	    



