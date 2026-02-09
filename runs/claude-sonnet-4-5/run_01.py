
def check(n, l, r, S):
    # Check if beacon ladder of length n is feasible
    # a_n = l + (n-1)*n/2
    a_n = l + (n - 1) * n // 2
    if a_n > r:
        return False
    
    # sum = n*l + n*(n+1)*(n-1)/6
    total = n * l + n * (n + 1) * (n - 1) // 6
    if total > S:
        return False
    
    return True

def solve(l, r, S):
    left, right = 1, 2000000
    result = 1
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid, l, r, S):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

t = int(input())
for _ in range(t):
    l, r, S = map(int, input().split())
    print(solve(l, r, S))
