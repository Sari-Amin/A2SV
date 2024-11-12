# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
left = 0
ans = []
right = 0
while left < n and right < m:
    if a[left] < b[right]:
        ans.append(a[left])
        left += 1
    else:
        ans.append(b[right])
        right += 1
while left < n:
    ans.append(a[left])
    left += 1
while right < m:
    ans.append(b[right])
    right += 1
print(*ans)