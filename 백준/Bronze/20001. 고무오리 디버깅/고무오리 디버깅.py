d = {
    "문제": 0
}

while True:
    l = input()
    if l == "고무오리 디버깅 끝":
        break
    elif l == "문제":
        d["문제"] += 1
    elif l == "고무오리":
        if d["문제"] > 0:
            d["문제"] -= 1  # 문제가 있을 경우 해결
        else:
            d["문제"] += 2  # 문제가 없을 경우 문제 2개 추가

if d["문제"] == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")