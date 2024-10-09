# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
ls = [int(i) for i in input().split()]
even,odd = 0,0
for i in range(n):
    if ls[i] % 2:
        odd += 1
    else:
        even += 1
if odd != 0 and even != 0:
    print(*sorted(ls))
else:
    print(*ls)