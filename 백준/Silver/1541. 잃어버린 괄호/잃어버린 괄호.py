expression = input().strip()

total = 0
current_number = 0
is_negative = False

for char in expression:
    if char.isdigit():
        current_number = current_number * 10 + int(char)
    else:
        if is_negative:
            total -= current_number
        else:
            total += current_number

        current_number = 0
        
        if char == '-':
            is_negative = True

# 마지막 숫자 처리
if is_negative:
    total -= current_number
else:
    total += current_number

print(total)
