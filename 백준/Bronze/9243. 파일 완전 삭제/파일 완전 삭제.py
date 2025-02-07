# 입력 받기
n = int(input())
original_bits = input().strip()
deleted_bits = input().strip()

# n이 홀수일 경우 -> 비트를 반전시켜야 함
if n % 2 == 1:
    # 비트 반전 (0->1, 1->0)
    inverted_bits = ''.join(['1' if bit == '0' else '0' for bit in original_bits])
    if inverted_bits == deleted_bits:
        print("Deletion succeeded")
    else:
        print("Deletion failed")

# n이 짝수일 경우 -> 원래 비트와 동일해야 함
else:
    if original_bits == deleted_bits:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
