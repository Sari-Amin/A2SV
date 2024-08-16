# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score, name])
    records.sort()
    curr = records[0][0]
    for val in records:
        if curr != val[0]:
            curr = val[0]
            break
    for val in records:
        if curr == val[0]:
            print(val[1])
    
        