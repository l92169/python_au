n = int(input())
lst = [[0 for i in range(n)] for j in range(n)]
count = 1
d = 0
lst[n//2][n//2] = n*n
for i in range(n//2):
    for j in range(n - d):
        lst[i][j + i] = count
        count += 1
    for j in range(i + 1, n - i):
        lst[j][-i - 1] = count
        count += 1
    for j in range(i + 1, n - i):
        lst[-i - 1][-j - 1] = count
        count += 1
    for j in range(i + 1, n - (i + 1)):
        lst[-j - 1][i] = count
        count += 1
    d += 2
print(lst)