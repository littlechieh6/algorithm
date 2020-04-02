a_l = map(int, input().split())
t = int(input())
h = t+30
s = 0
for i in a_l:
    if i<=h:
        s+=1
print(s)
