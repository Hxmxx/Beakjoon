t = int(input())

for _ in range(t):
    li = list(map(int, input().split()))

    hp = li[0] + li[4]
    mp = li[1] + li[5]
    atk = li[2] + li[6]
    de = li[3] + li[7]

    if hp < 1: hp = 1
    if mp < 1: mp = 1
    if atk < 0: atk = 0

    combat_power = (1 * hp) + (5 * mp) + (2 * atk) + (2 * de)

    print(combat_power)