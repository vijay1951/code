msg1=input()
msg2=input()
c1=0
for i in msg2: 
    c1+=1
past=msg2[c1-1]  
count=0
for i in msg1:
    if i==past:
        count+=1
print(count)        
