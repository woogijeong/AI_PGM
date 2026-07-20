START = 2
END = 100

group_start = START

while group_start <= END:
    # 첫 번째 그룹(2~10단)
    if group_start == 2:
        group_end = 10
    else:
        group_end = min(group_start + 9, END)

    # 구구단 출력
    for i in range(1, 10):
        for dan in range(group_start, group_end + 1):
            print(f"{dan:>3} x {i} = {dan*i:<4}", end="   ")
        print()

    print("\n" + "=" * 140 + "\n")

    # 다음 그룹 시작
    group_start = group_end + 1