def bs_slice(item, L):
    n = len(L)
    mid = n//2
    
    if n == 0:
        return False
    if L[mid] == item:
        return True
    
    if L[mid] > item:
        return bs_slice(item,L[:mid])
    if L[mid] < item:
        return bs_slice(item, L[mid+1:])
    
    #because we are slicing, this does not take O(logn)
    #geo series, O(n)
    return False
    

def bs_iter(item, L):
    low = 0
    high = len(L)
    mid = high//2

    while low <= high:
        if L[mid] == item:
            return True
        if L[mid] > item:
            high = mid
        if L[mid] < item:
            low = mid+1

    return False

def bs_better(item, L, left=0, right=None):
    if right is None:
        right = len(L)-1
    mid = (left + right)//2
    
    if left >= right:
        return False
    
    if L[mid] == item:
        return True
    elif L[mid] > item:
        return bs_better(item,L, left, right=mid)
    else: 
        return bs_better(item, L, left=mid+1, right)
    
    #o(logn)