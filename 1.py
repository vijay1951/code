a=int(input())
if a<0:
    s1="-"
else:
    s1=" "
a=abs(a) 
if a<3:
    print(int(a))
    exit(0)
s=''
while a!=0:
    s=str(a%3)+s 
    a=a//3
print(int(s1+s))    
    
