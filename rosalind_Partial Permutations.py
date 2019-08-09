import math
n = int(input())
k = int(input())
res = math.factorial(n) / math.factorial(n - k)
res = res % 1000000
print(res)