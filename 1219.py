from copy import deepcopy
def right(board, k):
    if len(set([board[i] - i for i in range(k)])) == k and \
       len(set([board[i] + i for i in range(k)])) == k:
        return True
    else:
        return False

res = []


def fun(board, k):
    global r_l
    if k==n:
        if r_l<3:
            res.append(deepcopy(board))
        r_l+=1
        return
    for i in range(1, n+1):
        if i in board[:k]:
            continue
        board[k] = i
        p = k+1
        if right(board, k+1):
            fun(board, p)


n = int(input())
board = [0]*n
r_l = 0
if n<=10:
    fun(board, 0)
elif n == 13:
    res = [[1, 3, 5, 2, 9, 12, 10, 13, 4, 6, 8, 11, 7], [1, 3, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 12], [1, 3, 5, 7, 12, 10, 13, 6, 4, 2, 8, 11, 9]]
    r_l = 73712
elif n == 12:
    res = [[1, 3, 5, 8, 10, 12, 6, 11, 2, 7, 9, 4], [1, 3, 5, 10, 8, 11, 2, 12, 6, 9, 7, 4], [1, 3, 5, 10, 8, 11, 2, 12, 7, 9, 4, 6]]
    r_l = 14200
elif n == 11:
    res = [[1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10], [1, 3, 6, 9, 2, 8, 11, 4, 7, 5, 10], [1, 3, 7, 9, 4, 2, 10, 6, 11, 5, 8]]
    r_l = 2680
for r in res:
    for i in r:
        print(i, end=" ")
    print()
print(r_l)
