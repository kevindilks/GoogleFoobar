def solution(g):
    from itertools import product
    m = len(g) + 1 # number of rows, length of a column
    n = len(g[0]) + 1 # number of columns, length of a row
    dict = {} # dictionary mapping tuples (representing column vectors) to a list whose ith entry
              # is number of potential preimages with that tuple as its ith column
    for a in product([0,1], repeat=m):
        dict[a] = [1] + [0]*(n-1)
    def compatible(x,y,gg): #function that checks if the 2x2 squares formed by attaching column y to column x
                           # yield the correct booleans from our input
        for i in range(len(x)-1):
            if ((x[i]+y[i]+x[i+1]+y[i+1] == 1) and (gg[i] == False)) or ((x[i]+y[i]+x[i+1]+y[i+1] != 1) and (gg[i] == True)):
                return False
        return(True)
    for col in range(n-1):
        for x in dict:
            for y in dict:
                if compatible(x,y,[a[col] for a in g]):
                    dict[x][col+1] += dict[y][col]
    return(sum(dict[a][n-1] for a in dict))