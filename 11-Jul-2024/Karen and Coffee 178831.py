# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = map(int, input().split())
arr = [0] * 200002
for _ in range(n):
    l,r = map(int, input().split())
    arr[l] += 1
    arr[r + 1] -= 1
for i in range(1,200002):
    arr[i] += arr[i - 1]
for i in range(200002):
    if arr[i] >= k:
        arr[i] = 1
    else:
        arr[i] = 0

for i in range(1,200002):
    arr[i] += arr[i - 1]

for _ in range(q):
    l,r = map(int, input().split())
    print(arr[r] - arr[l - 1])