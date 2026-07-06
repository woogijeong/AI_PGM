while True:
    print("\n=== 계산기 ===")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("0. 종료")

    menu = input("메뉴를 선택하세요: ")

    if menu == "0":
        print("프로그램을 종료합니다.")
        break

    if menu not in ["1", "2", "3", "4"]:
        print("잘못된 입력입니다.")
        continue

    num1 = float(input("첫 번째 숫자: "))
    num2 = float(input("두 번째 숫자: "))

    if menu == "1":
        print(f"결과: {num1 + num2}")
    elif menu == "2":
        print(f"결과: {num1 - num2}")
    elif menu == "3":
        print(f"결과: {num1 * num2}")
    elif menu == "4":
        if num2 == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print(f"결과: {num1 / num2}")