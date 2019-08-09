def print_matrix(matrix):
    for i in range(len_str1 + 1):
        for j in range(len_str2 + 1):
            print(matrix[i][j], end=" ")
        print()


def diff(s1, s2):
    if s1 == s2:
        return 0
    else:
        return 1


str1 = input()
str2 = input()
len_str1 = len(str2)
len_str2 = len(str1)
levenst_matrix = [[0 for j in range(len_str2 + 1)] for i in range(len_str1 + 1)]
for i in range(len_str1 + 1):
    levenst_matrix[i][0] = i
for j in range(len_str2 + 1):
    levenst_matrix[0][j] = j
for i in range(1, len_str1 + 1):
    for j in range(1, len_str2 + 1):
        c = diff(str2[i - 1], str1[j - 1])
        levenst_matrix[i][j] = min(levenst_matrix[i - 1][j] + 1, levenst_matrix[i][j - 1] + 1, levenst_matrix[i - 1][j - 1] + c)
print_matrix(levenst_matrix)
res = []
i = len_str1
j = len_str2
while i != 0 or j != 0:
    if levenst_matrix[i][j] == levenst_matrix[i - 1][j]:
        res.append('D')
