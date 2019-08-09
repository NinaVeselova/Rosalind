import math
str = input()
a = str.count('A')
c = str.count('C')
res = math.factorial(a) * math.factorial(c)
print(res)