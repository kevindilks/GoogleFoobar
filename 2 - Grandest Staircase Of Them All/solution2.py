# Let f(n,m) be the number of strict partitions of n with largest part equal to m
# Desired answer would be f(2N,N), or alternatively, sum_{k=0}^{N-1} f(N,k)
# Recursion should be f(n,m) = sum_{i=1}^{min(n-m,m-1)} f(n-m,i)
# The number of ways we can have a partition of n with largest part m
# is the sum of the ways we can have a partition of n-m whose largest part is less than m
# Initial conditions are f(i,i) = 1.
# I guess we could be more clever and make the only initial condition f(0,0) = 0 
# and have our current initial conditions follow by one more step of recursion.
# Entries f(n,m) are only non-negative if n>m.

def solution(n):    
    L = {} # Dictionary to keep track of computed f(i,j) values. Matrix probably ok but it would be half empty
    for a in range(0,n+1):
        L[(a,a)] = 1
    for i in range(1,n+1):
        for j in range(0,i):
            #print(i,j)
            L[(i,j)] = sum([L[(i-j,k)] for k in range(1,min(i-j+1,j))])
    return(sum([L[(n,k)] for k in range(n)]))
