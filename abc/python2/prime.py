s=list(range(1,101))
for x in s:
    if s[x]>1:
        z=x+s[x]
        while z<=len(s):
            s[z]=0
            z=z+s[x]
print filter(lambda x:x!=0,s)
