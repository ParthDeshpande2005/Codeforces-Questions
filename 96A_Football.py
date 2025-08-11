#%%
a=1
b=[]
s=input()
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        a=a+1
        if(a==7):
            b.append(a)

    else:
        b.append(a)
        a=1

b.sort(reverse=True)
if(b[0]>=7):
    print("YES")
else:
    print("NO")