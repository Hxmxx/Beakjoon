def count_throws(N, M, L):
    counts = [0] * N  
    current = 0  
    throws = 0  
    
    while True:
        counts[current] += 1  
        
        if counts[current] == M:
            break 
        
        if counts[current] % 2 == 1:
            current = (current + L) % N
        else:
            current = (current - L) % N
        
        throws += 1 
    
    return throws

N, M, L = map(int, input().split())
print(count_throws(N, M, L))
