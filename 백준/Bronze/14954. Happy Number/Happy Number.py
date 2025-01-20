def is_happy_number(n):
    def sum_of_squares(num):
        """Calculate the sum of squares of the digits of the number."""
        return sum(int(digit) ** 2 for digit in str(num))

    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)

    return n == 1

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())

    if is_happy_number(n):
        print("HAPPY")
    else:
        print("UNHAPPY")
