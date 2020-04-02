n = float(input())
s = 2
a = 0
i = 0
while a<n:
    i+=1
    a+=s
    s=s*0.98
print(i)
