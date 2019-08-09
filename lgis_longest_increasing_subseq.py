# Longest Increasing Subsequence
n = int(input())
A = [int(i) for i in input().split()]
D = [1] * n
Per = [-1] * n
for i in range(n):
    for j in range(i):
        if A[j] < A[i] and D[i] < D[j] + 1:
            D[i] = D[j] + 1
            Per[i] = j
m = 0
k = 0
for i in range(n):
    if D[i] > m:
        k = i
        m = D[i]
ans = [0] * m
for i in range(m-1,-1,-1):
    ans[i] = A[k]
    k = Per[k]
for i in ans:
    print(i,end=' ')
print()
G = [1] * n
Peri = [-1] * n
for i in range(n):
    for j in range(i):
        if A[j] > A[i] and G[i] < G[j] + 1:
            G[i] = G[j] + 1
            Peri[i] = j
z = G[0]
k = 0
for i in range(n):
    if G[i] > z:
        k = i
        z = G[i]
anst = [0] * z
anst[m - 1] = G[k]
for i in range(z-1,-1,-1):
    anst[i] = A[k]
    k = Peri[k]
for i in anst:
    print(i, end=' ')
