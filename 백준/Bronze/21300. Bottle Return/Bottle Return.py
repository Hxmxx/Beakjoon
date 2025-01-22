def calculate_refund(containers):
    """Calculate the total refund for the given number of containers."""
    refund_per_container = 5 
    total_containers = sum(containers)
    return total_containers * refund_per_container

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    containers = list(map(int, input().strip().split()))

    print(calculate_refund(containers))
