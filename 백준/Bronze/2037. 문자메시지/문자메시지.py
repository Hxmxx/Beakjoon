def calculate_typing_time(p, w, message):
    keypad = {
        ' ': (1, 1),
        'A': (2, 1), 'B': (2, 2), 'C': (2, 3),
        'D': (3, 1), 'E': (3, 2), 'F': (3, 3),
        'G': (4, 1), 'H': (4, 2), 'I': (4, 3),
        'J': (5, 1), 'K': (5, 2), 'L': (5, 3),
        'M': (6, 1), 'N': (6, 2), 'O': (6, 3),
        'P': (7, 1), 'Q': (7, 2), 'R': (7, 3), 'S': (7, 4),
        'T': (8, 1), 'U': (8, 2), 'V': (8, 3),
        'W': (9, 1), 'X': (9, 2), 'Y': (9, 3), 'Z': (9, 4),
    }

    total_time = 0
    prev_key = None

    for char in message:
        key, presses = keypad[char]
        total_time += presses * p

        # 같은 키 연속 입력 시 대기 시간 추가
        if prev_key == key and key != 1:  # 공백(1)은 연속입력 대기 없음
            total_time += w
        
        prev_key = key
    
    return total_time

# 입력
p, w = map(int, input().split())
message = input().strip()

# 결과 출력
print(calculate_typing_time(p, w, message))
