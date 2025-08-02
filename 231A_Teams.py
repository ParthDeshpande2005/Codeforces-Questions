a=int(input())
cnt=0
for i in range(a):
    b=input()
    b=b.split()
    if((int(b[0])+int(b[1])+int(b[2]))>1):
        cnt=cnt+1
print(cnt)