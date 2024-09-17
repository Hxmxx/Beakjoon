def count_lan_cables(lan_cables, length):
    count = 0
    for cable in lan_cables:
        count += cable // length
    return count

def find_max_lan_length(lan_cables, k, n):
    low, high = 1, max(lan_cables)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        total_cables = count_lan_cables(lan_cables, mid)
        
        if total_cables >= n:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

k, n = map(int, input().split())
d = [int(input()) for _ in range(k)]

max_length = find_max_lan_length(d, k, n)

print(max_length)
