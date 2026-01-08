s="aaabbbccd"
#output=a3b3c2d

i=0
while i<len(s):
    count=1
    while i+1<len(s) and s[i]==s[i+1]:
        count+=1
        i+=1
    if count>1:
        print(s[i],count,sep='',end='')
    else:
        print(s[i],end='')
    i+=1
print('\n')   
        