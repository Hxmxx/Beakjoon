def is_valid_sudoku(grid):
    for i in range(9):
        if len(set(grid[i])) < 9 or len(set(row[i] for row in grid)) < 9:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if len(set(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3))) < 9:
                return False
    return True


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n\n')

    for idx, case in enumerate(data, 1):
        grid = [list(map(int, line.split())) for line in case.split('\n')]
        print(f"Case {idx}: {'CORRECT' if is_valid_sudoku(grid) else 'INCORRECT'}")


if __name__ == "__main__":
    main()
