n=int(input())
list=[]
for i in range(n):
    a=input()
    if(len(a)<10):
        list.append(a)
    else:
        b=a[0]+str(len(a)-2)+a[-1]
        list.append(b)
for item in list:
    print(item)