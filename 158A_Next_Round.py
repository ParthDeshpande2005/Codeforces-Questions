
a=input()
a=a.split()
b=input()
b=b.split()
 
a=list(map(int,a))
b=list(map(int,b))
 
n=a[0]
k=a[1]
 
cnt=0
for i in range(n):
    if (b[i]>=b[k-1] and b[i]>0):
        cnt+=1
 
print(cnt)