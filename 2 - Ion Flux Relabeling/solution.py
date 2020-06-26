#Helper function that returns predecessor of 'n' in tree of depth 'p'
def loop(p,n):
    (previous_largest_possible_parent,largest_possible_parent) = (-1,2**p-1)
    running_total = 0
    while n!=largest_possible_parent:
        #print(previous_largest_possible_parent,largest_possible_parent,n)
        if n<2**(p-1)+running_total:
            (previous_largest_possible_parent,largest_possible_parent) = (largest_possible_parent,largest_possible_parent-2**(p-1))
        else:
            (previous_largest_possible_parent,largest_possible_parent) = (largest_possible_parent,largest_possible_parent-1)
            running_total+=2**(p-1)-1
        p-=1
    return(previous_largest_possible_parent)

def solution(p, q):

    return([loop(p,n) for n in q])