def merge_sort(L):
    """Sorts w/ merge sort"""
    # Base case - a list of 1 or 0 items is already sorted
    if len(L) < 2: 
        return L

    # Recursive case - sort left and right halves, then merge them
    L_left = merge_sort(L[:len(L)//2])
    L_right = merge_sort(L[len(L)//2:])
    merge(L, L_left, L_right)

    # Return statement necessary for recursive cases
    return L

def merge(L, L_left, L_right):
    """Merges sorted lists L_left and L_right into L"""
    i, j = 0, 0

    while i < len(L_left) and j < len(L_right):
        # For stability, write from L_left if items are equal
        if L_left[i] <= L_right[j]:
            L[i+j] = L_left[i]
            i+=1

        else:
            L[i+j] = L_right[j]
            j+=1

    # Append the rest of L_left or L_right, whichever is not finished yet
    L[i+j:] = L_left[i:] + L_right[j:]