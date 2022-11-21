def check(a) :
	for i in range(len(a)) :
		if (a[i] == '4' or a[i] == '6' or a[i] == '7') :
			return False;
	return True;

n=int(input())
count=0
l1=[]
i=1
while count!=n:
    if (check(str(i))) :
        count+=1
        l1.append(i)
    i+=1
print(l1[n-1])
