# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n,t = map(int, input().split())
ls = list(map(int,input().split()))
ptr = 0
while ptr < t - 1:
    ptr += ls[ptr]


if ptr == t - 1:
    print("YES")
else:
    print("NO")