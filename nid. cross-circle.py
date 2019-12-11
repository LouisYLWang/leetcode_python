
#class Solution:
#    def countCrossCircle(self, A):
#    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14  15  16  17
A = [1,2,3,4,5,6,7,8,9,9,9, 9, 9, 9, 13, 15, 17, 18]
#[0,1,2,3,4,5,6]
#[-1,1], [0,2], [1,3], [1,5], [1,7], [4,6], [3,9]

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    left = [0 for i in range(n)]
    for i in range(n):
        l = max(0, i - A[i])
        left[l] += 1
    print(left)
        #if A[i] - i < 0:
        #    left[]
    for i in range(1,n):
        left[i] += left[i-1] 
    print(left)
    
    count = 0
    left = [0] + left
    print(left)
    for i in range(0,n):
        l = max(0, i - A[i])
        r = min(n -1, i + A[i])
        print(r, l)
        print(left[r+1]- left[l])
        count += (left[r+1] - left[l])
        
    print(count)
    return count - n


def binary_search(A, x):
    l = 0
    r = len(A) -1
    while l <= r:
        m = l + (r - l) // 2
        if A[m] < x:
            l = m + 1
        if A[m] == x:
            return m
        if A[m] > x:
            r = m - 1
    return l 
def binary_search_r(A, x):
        l = -1
        r = len(A) -1
        while r - l > 1:
            m = l + (r - l) // 2
            if A[m] <= x:
                l = m 
            if A[m] > x:
                r = m 
        return l
        
def binary_search_l(A, x):
    l = 0
    r = len(A)
    while r - l > 1:
        m = l + (r - l) // 2
        if A[m] >= x:
            r = m 
        if A[m] < x:
            l = m 
    return r
print(binary_search_l(A, 9))
print(binary_search_r(A, 9))

