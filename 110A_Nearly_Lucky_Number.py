a=input()
b=0
for i in range(len(a)):
    if(a[i]=="4" or a[i]=="7"):
        b=b+1
if(b==4 or b==7):
    print("YES")   
else:
    print("NO") 