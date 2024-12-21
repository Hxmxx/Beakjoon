def sum_of_digits(serial):
    return sum(int(c) for c in serial if c.isdigit())

def serial_key(serial):
    return (len(serial), sum_of_digits(serial), serial)

N = int(input())
serial_numbers = [input().strip() for _ in range(N)]

serial_numbers.sort(key=serial_key)

for serial in serial_numbers:
    print(serial)
