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
	    



