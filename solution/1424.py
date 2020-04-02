x, n = map(int, input().split())
x = x%7
t = 0
while n!=0:
    if not x==0 and not x==6:
        t+=1
    x=(x+1)%7
    n -= 1
print(t*250)
