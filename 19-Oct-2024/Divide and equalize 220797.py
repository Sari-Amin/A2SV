# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import defaultdict


def add_divs(x, divs):
    i = 2
    while i * i <= x:
        while x % i == 0:
            divs[i] += 1
            x //= i
        i += 1
    if x > 1:
        divs[x] += 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    divs = defaultdict(int)
    for i in range(n):
        add_divs(a[i], divs)
    for e in divs.values():
        if e % n != 0:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print("YES" if solve() else "NO")

