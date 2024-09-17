# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

def solve():
    m,s = map(int, input().split())
    if s == 0 and m == 1:
        return print(0,0)
    max_num = ["0"] * m
    min_num = ["0"] * m
    if s < 1:
        return print(-1,-1)
    min_num[0] = str(1)
    temp = s - 1
    for i in range(m - 1, 0,-1):
        if temp >= 9:
            min_num[i] = str(9)
            temp -= 9
        else:
            min_num[i] = str(temp)
            temp = 0
            break
    if temp > 0 and temp + int(min_num[0]) > 9:
        return print(-1,-1)
    else:
        min_num[0] = str(int(min_num[0]) + temp)

    temp = s
    for i in range(m):
        if temp >= 9:
            max_num[i] = str(9)
            temp -= 9
        else:
            max_num[i] = str(temp)
            temp = 0
            break
    if temp:
        return print(-1,-1)
        
    return print("".join(min_num), "".join(max_num))



solve()