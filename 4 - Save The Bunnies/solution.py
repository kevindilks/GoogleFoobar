def solution(times, time_limit):
    #Rough psuedo-code
    #
    # Step 1: Use Bellman-Ford algorithm to find shortest path between all pairs of vertices in the graph
    # (typically Bellman-Ford done with a single source node in mind, we want to do all nodes as possible source in parallel)
    # 
    # Step 2: Iterate over all possible subsets of bunnies we could save, in reverse shortlex
    #
    # Step 3: Consider all possible permutations of this subset of bunnies we are attempting to save.
    # (Since it may not be optimal to save them in increasing pr)
    # (maybe say it's abcd)
    # Step 4: look at sp(start,a)+sp(a,b)+sp(b,c)+sp(c,d)+sp(d,bulkhead) and see if that satisfies the time requirement
    def Bellman_Ford(M):
        # Takes in adjacency matrix of real-weighted complete digraph
        # and gives weight of shortest path between any pair of vertices
        #
        # I suppose this would work for a general real-weighted digraph
        # By replacing non-existing edges with an edge of weight 'inf'
        #
        # Can easily be modified to additionally give the shortest paths
        # themselves by recording in the (i,j) entry the first edge taken
        # along some minimal length path
        #
        # Haha, jk, going to leave the code returning the tuple
        n = len(M)
        distance = [[float('inf') for j in range(n)] for i in range(n)]
        for i in range(n):
            distance[i][i] =0
        # Initialize shortest distance from vertex i to vertex j as 'Inf' if i!j, and 0 otherwise
        predecessor = [[i for j in range(n)] for i in range(n)]
        # Initialize the predecessor of shortest path from i to j as being i 
        # (directly following edge from i to j)
        for q in range(1,n): # we do one |V|-1 rounds of relaxing edges, q not used
            for i in range(n): # Iterate over all possible edges i!=j
                for j in range(n):
                    if i!=j:
                        for s in range(n): #Do the update for each possible source vertex 's'
                            if distance[s][i] + M[i][j] < distance[s][j]:
                                distance[s][j] = distance[s][i] + M[i][j]
                                # If our best path from s to i, and then following i-j edge is better
                                # than our best path from s to j, we have a new best path from s to j
                                predecessor[s][j] = i
        for i in range(n):
            for j in range(n):
                if i!=j:
                    for s in range(n):
                        if distance[s][i] + M[i][j] < distance[s][j]:
                            return("Freedom!")
        return(distance,predecessor)
    n = len(times)
    from itertools import chain, combinations, permutations
    bunny_subsets = list(chain.from_iterable(combinations(range(n-2),k) for k in range(n-1,0,-1)))
    BF = Bellman_Ford(times)
    if BF == "Freedom!":
        return(range(n-2))
    SP = BF[0]
    for LL in bunny_subsets:
        for L in permutations(LL):
            total_time = 0
            total_time += SP[0][L[0]+1]
            for a in range(len(L)-1):
                total_time+= SP[L[a]+1][L[a+1]+1]
            total_time += SP[L[-1]+1][n-1]
            if total_time <= time_limit:
                return(LL)