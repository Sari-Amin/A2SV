# Problem: Cover in Water - https://codeforces.com/problemset/problem/1900/A

for _ in range(int(input())):
    n = int(input())
    s = input()
    left = s.find(".")
    ans = 0
    right = left
    pos = False
    while right < n:
        if s[right] == ".":
            right += 1
        else:
            if right - left  >= 3:
                pos = True
            else:
                ans += right - left
            right += 1
            left = right
    if right - left  >= 3:
        pos = True
    else:
        ans += right - left  
    if pos:
        print(2)
    else:
        print(ans)