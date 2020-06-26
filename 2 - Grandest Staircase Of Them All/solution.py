L = {} # A global dictionary caching computed values of
       # f(x,y) to avoid redundant recursive calls
def f(boxes_left,largest_part):
    # The function f returns the number of strict partitions
    # of size 'boxes_left', where the largest part must be
    # strictly less than 'largest_part'.
    #
    # Recursively adds up all values of f(boxes_left-i,i)
    # Which we can think of as considering all ways we could
    # tack on a new part 'i' to a strict partition being built.
    global L
    if boxes_left <0:
        return 0
    if boxes_left == 0:
        L[(boxes_left,largest_part)] = 1
        return 1
    else:
        ct = 0
        for i in range(1,min(boxes_left,largest_part-1)+1):
            if (boxes_left-i,i) not in L:
                ct += f(boxes_left-i,i)
            else:
                ct += L[(boxes_left-i,i)]
        L[(boxes_left,largest_part)] = ct
        return ct

def solution(n):
    return(f(n,n))