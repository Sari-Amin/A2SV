# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())
ans = 0
for i in range(n):
    ans += input().count("1")
print(ans // 2)