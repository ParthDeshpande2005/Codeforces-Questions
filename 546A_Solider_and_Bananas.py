a=input()
a=a.split(" ")
# print(a)
c=0
for i in range(1,int(a[2])+1):
    c=c+int(a[0])*i

if(c>int(a[1])):
    c=c-int(a[1])
    print(c)
else:
    print(0)