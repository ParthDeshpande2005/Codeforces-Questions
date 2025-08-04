# %%
a=input()
a=a.lower()
s=""
if "a" or "e" or "i" or "o" or "u" or "y" in a:
    a=a.replace("a","")
    a=a.replace("e","")
    a=a.replace("i","")
    a=a.replace("o","")
    a=a.replace("u","")
    a=a.replace("y","")
    for i in range(len(a)):
        s=s+"."+a[i]
    print(s)    
else:
    for i in range(len(a)):
        s=s+"."+a[i]
    print(s)


# %%
#chat gpt using if any
a = input()
a = a.lower()
s = ""

if any(vowel in a for vowel in "aeiou"):
    for vowel in "aeiou":
        a = a.replace(vowel, "")
        
for i in range(len(a)):
    s += "." + a[i]

print(s)