# Problem: Twin Permutations - https://codeforces.com/contest/1831/problem/A

for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    ans = sorted(ls)
    for i in range(n):
        ans[i] = n + 1 - ls[i]
        
    print(*ans)
        