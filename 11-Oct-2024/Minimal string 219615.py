# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

from collections import Counter
s = input()
dict = Counter(s)
t,u = [],[]

for ch in s:
    t.append(ch)
    dict[ch]-=1
    if dict[ch]==0:
        del dict[ch]
        
    while t and (not dict or min(dict) >= t[-1]):
        u.append(t.pop())
        
print(''.join(u))



