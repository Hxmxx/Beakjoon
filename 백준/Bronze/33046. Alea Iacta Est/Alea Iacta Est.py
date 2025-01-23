def determine_jindong(A, B, C, D):
    """
    Determine which player becomes 'jindong' based on the dice rolls.

    Args:
        A, B: Results of the first dice roll (two integers).
        C, D: Results of the second dice roll (two integers).

    Returns:
        The player number (1 to 4) who becomes 'jindong'.
    """
    first_sum = A + B
    second_sum = C + D

    gadong = (first_sum - 1) % 4 + 1

    jindong = (gadong + second_sum - 2) % 4 + 1

    return jindong

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    A, B, C, D = map(int, data)

    print(determine_jindong(A, B, C, D))