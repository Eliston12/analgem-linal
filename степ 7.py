
def duty(u, v):
    res = 0
    for i in range(len(v)):
        res += u[i] * v[i]
    return res


n = int(input('Количество ? '))
print('Ввод векторов')
V = [list(map(float, input().split())) for i in range(n)]
m = len(V[0])

for i in range(n):
    if m != n or m != n:
        print('Ввод некорректный')
        exit(0)

Ort = [[V[j][i] for i in range(len(V))]for j in range(len(V))]
for i in range(1, n):
    for j in range(0, i):
        proj = [i for i in range(m)]
        for n in range(m):
            proj[n] = (duty(V[j], Ort[i]) / duty(V[j], V[j])) * V[j][n]
        for n in range(m):
            Ort[i][n] -= proj[n]
for k in Ort:
    print(k)
