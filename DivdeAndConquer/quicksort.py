def quick_good(L, left = 0, right = None):
    if right == None:
        right = len(L)
    if right - left <=1:
        return None
    pivot = right -1

    i=left
    j = right -2

    while i<j:
        while L[i]< L[pivot]:
            i+=1
        while L[j]>= L[pivot] and i<j:
            j-=1    
        if i<j:
            L[i], L[j]= L[j], L[i]
    
    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[j],L[i]
        pivot = i

    quick_good(L,left, pivot)
    quick_good(L,pivot+1, right)
