def solution(L):
    #Algebraically, there can only be one solution for what the final gear could be, 
    #given peg positions a_1,\ldots,a_n, and first gear being twice as large as final gear
    # [(-1)^n a_n + 2(-1)^(n-1)a_{n-1}+2(-1)^(n-2)a_{n-2}\ldots + 2a_2 + (-1)^(n)a_1]/[2+(-1)^n]
    #So let's compute this solution
    n = len(L)
    final_gear = 0
    for i in range(n):
        if i==0:
            final_gear+=(-1)*L[0]
        elif i==n-1:
            final_gear+= (-1)**(n)*L[n-1]
        else:
            final_gear+=2*(-1)**(i+1)*L[i]
    
    #If n is even, this is the final gear. If n is odd, we need divide to by 3.
    if n%2 == 1:
        final_gear_num = final_gear
        final_gear_den = 1
    else:
        if final_gear%3 == 0:
            final_gear_num = final_gear//3
            final_gear_den = 1
        else:
            final_gear_num = final_gear
            final_gear_den = 3
    #print(final_gear_num,final_gear_den)
    #But we also need to check that all gears lengths end up being non-negative
    #First gear is twice our final gear, and the nth gear length is a_{n}-a_{n-1}-g_{n-1}
    previous_gear = 2*final_gear_num/final_gear_den
    #print(previous_gear)
    for i in range(1,n):
        if previous_gear <= 0:
            return([-1,-1])
        previous_gear = L[i]-L[i-1]-previous_gear
        #print(previous_gear)
    return([2*final_gear_num,final_gear_den])