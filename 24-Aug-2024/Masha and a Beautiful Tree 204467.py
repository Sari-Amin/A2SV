# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def solve():
    m = int(input())
    ls = [int(i) for i in input().split()]
    res = [0] 
    def merge(left_hand, right_hand):
        
        left = 0
        right = len(right_hand) - 1
        if left_hand[left] > right_hand[right]:
            res[0] += 1
            return right_hand + left_hand
        return left_hand + right_hand
    


    def mergeSort(left, right, arr):
        if left >= right:
            return [arr[left]]

        mid = left + (right - left) // 2

        left_hand = mergeSort(left, mid, arr)
        right_hand = mergeSort(mid + 1, right, arr)

        return merge(left_hand, right_hand)

    temp = mergeSort(0, len(ls) - 1, ls)
    if temp == sorted(temp):
        return res[0]
    
    return -1


for _ in range(int(input())):
    print(solve())