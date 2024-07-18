# Problem: Z-Sort - https://codeforces.com/problemset/problem/652/B


def main():

    n = int(input())
    m = n
    a = list(map(int, input().split()))
    b = [0] * n

    a.sort(reverse=True)

    j = 1
    i = 0
    while j < n:
        b[j] = a[i]
        i += 1
        j += 2

    j = 0
    while j < n:
        b[j] = a[i]
        i += 1
        j += 2

    for i in range(1, n, 2):
        if b[i] < b[i - 1]:
            print("Impossible")
            return

    for i in range(2, n, 2):
        if b[i] > b[i - 1]:
            print("Impossible")
            return

    for i in range(n):
        print(b[i], end=' ')

if __name__ == "__main__":
    main()