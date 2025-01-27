def count_unique_alphabets():
    while True:
        line = input().strip()
        if line == "#":
            break
        unique_chars = set(c.lower() for c in line if c.isalpha())
        print(len(unique_chars))

count_unique_alphabets()