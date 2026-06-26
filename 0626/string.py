# # # # # # a= "Life is too short"

# # # # # # #slicing
# # # # # # print(a[0:4])  # Output: Life
# # # # # # print(a[5:7])  # Output: is
# # # # # # print(a[8:11]) # Output: too
# # # # # # print(a[12:17])# Output: short

# # # # # # print(len(a))  # Output: 17
# # # # # # print(a[3])   # Output: f
# # # # # # print(a[-1])  # Output: t
# # # # # # print(a[8:-3]) # Output: too

# # # # # # a="pithon"
# # # # # # a[:1]
# # # # # # a[2:]
# # # # # # print(a[:1] + 'y' + a[2:])  # Output: python

# # # # # # print("현재 온도는 {0}도 입니다.".format(18))  # Output: 현재 온도는 18도 입니다.
# # # # # print("I eat %s apples." % "five")  # Output: I eat five apples.

# # # # # number = 10
# # # # # day = "three"
# # # # # print("I ate %d apples. so I was sick for %s days." % (number, day))  # Output: I ate 10 apples. so I was sick for three days.

# # # # # print("rate is %s" % 3.234)  # Output: rate is 3.234

# # # # # print("Error is 98%.")  # Output: Error is 98%.

# # # # # print("%10s" % "hi")  # Output:        hi
# # # # # print("%-10sjane." % "hi")  # Output: hi        jane.

# # # # # print("%0.4f" % 3.42134234)  # Output: 3.4213

# # # # # print("%10.4f" % 3.42134234)  # Output:     3.4213

# # # # # print(1+2)  # Output: 3

# # # # print("I ate {number} apples. soo I was sick for {day} days.".\
# # # # format(number=10, day=3))  # Output: I ate 10 apples. soo I was sick for 3 days.

# # # # print("{0:>10}".format("hi"))  # Output:         hi
# # # # print("{0:<10}".format("hi"))  # Output: hi
# # # # print("{0:^10}".format("hi"))  # Output:     hi
# # # # print("{0:=^10}".format("hi"))  # Output: ====hi====
# # # # print("{0:!^10}".format("hi"))  # Output: hi!!!!!!!! 

# # # y = 3.42134234
# # # print("{0:0.4f}".format(y))  # Output: 3.4213
# # print("{{ and }}")  # Output: { and }

# print("I ate %d apples and %10.1f oranges." % (1 + 2 , 0.5))  # Output: I ate 3 apples and 5.000000 oranges.

# str1 = "Sample python string."
# print(str1)  # Output: Sample python string.
# print("%s" % str1)  # Output: Sample python string.

# d={"name": "홍길동", "age": 30}
# print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}살입니다.")  # Output: 나의 이름은 홍길동입니다. 나이는 30살입니다.

# print(f"{"hi":>10}")  # Output:         hi

# y = 3.42134234
# print(f"{y:0.4f}")  # Output: 3.4213

# print(f"{{ and }}")  # Output: { and }

# print(f"난 {1500000:,}원이 필요해")

# a="hobby"
# print(a.count('b'))  # Output: 2

# a="Python is the best choice"
# print(a.find('b'))  # Output: 14

# print(a.find('k'))  # Output: -1

# a= "Life is too short"
# print(a.index('t'))  # Output: 8
# print(a.index('k'))  # Output: ValueError: substring not found

# print(",".join('abcd'))  # Output: a,b,c,d
# print(",".join(['a', 'b', 'c', 'd']))  # Output: a,b,c,d
# a= "hi"
# print(a.upper())  # Output: HI
# a= " Hi "
# print(a.lstrip())  # Output: Hi
# a= "   hello   Jeju    "
# print(a.strip())  # Output: hello   Jeju
# a= "Life is too short"
# print(a.replace("Life", "Your leg"))  # Output: Your leg is too short

# apple =3
# banana =5
# print(f"사과는 {apple}개, 바나나는 {banana}개 있습니다.")

# a= "Life is too short"
# print(a.split())  # Output: ['Life', 'is', 'too', 'short']
# b= "a:b:c:d"
# print(b.split(':'))  # Output: ['a', 'b', 'c', 'd']

# print(f"I eat 3 apples. and 5 oranges.")
# print(f"I eat {3} apples. and {5} oranges.")

# s= "python"
# print(s.isalpha())
# s= "python123"
# print(s.isalpha())
# s="Hello World"
# print(s.isalpha())

# s= "Life is too short"
# print(s.startswith("Life"))  # Output: True
# print(s.startswith("life"))  # Output: False

# print(f"i eat{{3}} apples.")  # Output: i eat{3} apples.

# s= "Life is too short"
# print(s.index("t",10))

# text = "banana"
# target = "a"

# pos = -1

# for _ in range(3):
#     pos = text.find(target,pos+1)
    
# print(pos)  # Output: 5

# a="hi"
# a.upper()
# print(a)

# a= input("enter first number: ")
# b= input("enter second number: ")
# print(f"your entered numbers are {a} and {b}")
# print(f"{a} + {b} = {int(a)+int(b)}")
# print(f"{a} - {b} = {int(a)-int(b)}")
# print(f"{a} * {b} = {int(a)*int(b)}")
# print(f"{a} / {b} = {int(a)/int(b):0.2f}")    #input은 문자열로 받는다.

# a= [1,2,3]
# print(a)
# print(a[0] + a[2])  # Output: 4

# print(a[-1])  # Output: 3
# # a=[1,2,3,['a','b','c']]
# # # print(a[0])  # Output: 1
# # # print(a[-1])  # Output: ['a', 'b', 'c']
# # # print(a[3])

# # print(a[3][0])  # Output: a

# # a= [1,2,['a','b',['Life','is']]]
# # print(a[2][2][0])  # Output: Life

# # a=[1,2,3,[4,5,['a','b','c']]]
# # print(a[2:5])  # Output: [3, [4, 5, ['a', 'b', 'c']]]

# # a= [1,2,3,4,5]
# # # b=[6,7,8,9,10]
# # # print(a+b)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # print(a*3)  # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# # print(len(a))  # Output: 5

# # a= [1,2,3]
# # print(str(a[2]) + "hi")

# # a= [1,2,3]
# # del a[1]
# # print(a)  # Output: [1, 3]

# # 1. 두 개의 정수를 입력받아 사칙연산 결과 출력
# num1 = int(input("첫 번째 정수를 입력하세요: "))
# num2 = int(input("두 번째 정수를 입력하세요: "))

# print("덧셈:", num1 + num2)
# print("뺄셈:", num1 - num2)
# print("곱셈:", num1 * num2)
# print("나눗셈:", num1 / num2)

# # 2. 다섯 개의 정수를 입력받아 리스트에 저장하고 합, 평균, 최소값, 최대값 출력

# numbers = []

# for i in range(5):
#     num = int(input(f"{i+1}번째 정수를 입력하세요: "))
#     numbers.append(num)

# print("리스트:", numbers)
# print("합:", sum(numbers))
# print("평균:", sum(numbers) / len(numbers))
# print("최소값:", min(numbers))
# print("최대값:", max(numbers))

# # 3. 과일명이 있는 리스트를 정의하고 첫 번째와 마지막 문자열 출력

# fruits = ["사과", "바나나", "포도", "딸기", "오렌지"]

# print("첫 번째 과일:", fruits[0])
# print("마지막 과일:", fruits[-1])


# a= input("enter first number: ")
# b= input("enter second number: ")
# print(f"{a} + {b} = {int(a)+int(b)}")
# print(f"{a} - {b} = {int(a)-int(b)}")
# print(f"{a} * {b} = {int(a)*int(b)}")
# print(f"{a} / {b} = {int(a)/int(b)}")

# arr = list(range(5))
# for i in range(5):
#     arr[i] = int(input(f"{i+1}번째 정수를 입력하세요: "))

# print("리스트 :", arr)
# print("합 :", sum(arr))
# print("평균 :", sum(arr) / len(arr))
# print("최소값 :", min(arr))
# print("최대값 :", max(arr))

# arr = ['사과', '바나나', '포도', '딸기', '오렌지']
# print("첫 번째 과일 :", arr[0])
# print("마지막 과일 :", arr[-1])

# arr = [int(input(f"{i+1}번째 정수를 입력하세요: ")) for i in range(5)]

# num1 = int(input("첫 번째 정수를 입력하세요: "))
# num2 = int(input("두 번째 정수를 입력하세요: "))
# num3 = int(input("세 번째 정수를 입력하세요: "))
# num4 = int(input("네 번째 정수를 입력하세요: "))
# num5 = int(input("다섯 번째 정수를 입력하세요: "))
# numbers = [num1, num2, num3, num4, num5]
# print(f"sum = {sum(numbers)}")
# print(f"average = {sum(numbers)/len(numbers)}")
# print(f"min = {min(numbers)}")
# print(f"max = {max(numbers)}")

# fruit1 = input("첫 번째 과일을 입력하세요: ")
# fruit2 = input("두 번째 과일을 입력하세요: ")
# fruit3 = input("세 번째 과일을 입력하세요: ")
# fruit4 = input("네 번째 과일을 입력하세요: ")
# fruits = [fruit1, fruit2, fruit3, fruit4]

# print(f"입력한 과일 리스트: {fruits}")
# print(f"첫 번째 과일: {fruits[0]}")
# print(f"마지막 과일: {fruits[-1]}")

# 사용자로부터 두 정수 입력받기
# num1 = int(input("첫 번째 정수를 입력하세요: "))
# num2 = int(input("두 번째 정수를 입력하세요: "))

# # 사칙연산 수행 및 결과 출력
# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")
# print(f"{num1} / {num2} = {num1 / num2}")

# #chatgpt
# num1 = int(input("첫 번째 정수를 입력하세요: "))
# num2 = int(input("두 번째 정수를 입력하세요: "))

# print("덧셈:", num1 + num2)
# print("뺄셈:", num1 - num2)
# print("곱셈:", num1 * num2)
# print("나눗셈:", num1 / num2)


# numbers = []

# for i in range(5):
#     num = int(input(f"{i+1}번째 정수를 입력하세요: "))
#     numbers.append(num)
#     sum = 0
#     for i in numbers:
#         sum += i


# print("리스트:", numbers)
# print("합:", sum)
# print("평균:", sum / len(numbers))
# print("최소값:", min(numbers))
# print("최대값:", max(numbers))

# list1 = list()
# list2 = []

# str1 = "abcd"
# str2 = ['a','b','c','d']

# print(str2[0:5:2]) #step

# a = {1 : 'a'}
# # a[2] = 'b'
# # print(a)

# a['name'] = 'pay'
# print(a)

# del a[1]
# print(a)

# a = {'name' : 'pay', 'phone' : '010-9999-1234' , 'birth' : '1118'}
# # # b = list(a.keys())
# # # print(a[b[1]])

# # for k in a.keys():
# #     print(k)

# # print('name' in a)

# s4 = {'a', 'b', 'c'}
# print(s4)

# a= 3
# b= 5
# a,b = b,a
# print(f"a = {a} , b = {b}")

# a = [1,2,3]
# b = a[:]
# a[1] = 4
# print(a)
# print(b)

# a = [1,2,3]
# b = a.copy()
# print(b)

# money = 2000
# if money >= 3000:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# grade = 'b'
# match grade:
#     case 'a':
#         print("good")
#     case 'b':
#         print("better")
#     case 'c':
#         print("normal")
#     case _:
# #         print("loser")
            
# score = 85
# result = "합격" if score >= 60 else "불합격"
# print(result)

# treehit = 0
# while treehit < 10:
#     treehit += 1
#     print(f"나무를 {treehit}번 때렸습니다")
#     if treehit == 10: print("나무 넘어갑니다.")

# score = []
   
# for i in range(5):
#     s = int(input("학생 의 {0}점수를 입력하세요 : ".format(i + 1)))
#     score.append(s)
    
#     if score[i] >= 60:
#         print("pass")
#     else :
#         print("fail")
# print(score)


# score = [0] * 5

# for i in range(5):
#     score[i] = int(input("학생 {0}의 점수 입력 : ".format(i + 1))) 
    
#     if score[i] >= 60:
#         print("pass")
#     else:
#         print("fail")
# print(score)

# add = 0
# for i in range(1, 11):
#     add += i
    
# print(add)

# for i in range(10):
#     for j in range(10):
#         print(f"{i} * {j} = {i * j}")

moon = int(input("연도를 입력하시오 : "))

if (moon % 4 == 0) and (moon % 100 != 0) or (moon % 400 == 0)  :
    print("pass")
else:
    print("fail")

