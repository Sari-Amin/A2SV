# Problem: Small GCD - https://codeforces.com/contest/1900/problem/D

N = int(1e5 + 5)

def solve():
    n = int(input())
    ls = sorted(int(x) for x in input().split())

    count = [0] * N
    index = [[] for _ in range(N)]

    for i in range(n):
        index[ls[i]].append(i)

    ans = 0
    temp = [[] for _ in range(N)]
    for i in range(N - 1, 0, -1):
        for c in range(i, N, i):
            temp[i].extend(index[c])
        for j in range(len(temp[i])):
            count[i] += (n - temp[i][j] - 1) * j
        for j in range(2 * i, N, i):
            count[i] -= count[j]
        ans += i * count[i]
    print(ans)

t = int(input())
for _ in range(t):
    solve()