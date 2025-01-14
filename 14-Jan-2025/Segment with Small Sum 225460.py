# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
ls = list(map(int, input().split()))

left = 0
right = 0
ans = 0
sm = 0
while right < n:
    if sm + ls[right] <= s:
        sm += ls[right]
        right += 1
    else:
        ans = max(ans, right - left)
        sm -= ls[left]
        left += 1


ans = max(ans, right - left)
print(ans)