# Problem: Maximal AND - https://codeforces.com/problemset/problem/1669/H

for _ in range(int(input())):
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    count = [0 for  i in range(31)]
    for num in ls:
        for i in range(31):
            if  num & (1 << i):
                count[i] += 1
    ans = 0
    for i in range(30, -1, -1):
        temp = n - count[i]
        if temp <= k:
            k -= temp
            ans += (1 << i)
    print(ans)