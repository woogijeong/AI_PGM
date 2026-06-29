# score = 85
# result = "pass" if score >= 60 else "fail"
# print(result)

# grade = input("enter your grade : ")
# if grade == 'A':
#     print("excellent!")
# elif grade == 'B':
#     print("good job!")
# elif grade == 'C':
#     print("you need to work harder.")
# else:
#     print("Invaild grade entered.")

# prompt = """
# 1. Add
# 2, Del
# 3. List
# 4. Quit

# Enter number"""

# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

# coffee = 10
# while True:
#     money = int(input("insert coin : "))
#     if money == 300:
#         print("give some coffee")
#         coffee -= 1
#     elif money > 300:
#         print(f"change {money - 300} won and give some coffee")
#         coffee -= 1
#     else:
#         print("give back your change and not give coffee")
#         print(f"remain coffee is {coffee} gae")
#     if coffee == 0:
#         print("coffee is gone. close the menu")
#         break

# count = 0
# while count < 3:
#     print(f"count : {count}")
#     count += 1
    
# else:
#     print("while fuction is shut down")

# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(f"{i} * {j} = {i * j}")
#         j += 1
#     j = 1
#     i += 1

# a = [1,2,3,4]
# result = [num * 3 for num in a]
# print(result)

# fruits = ['apple', 'banana' , 'orange']
# for i, fruit in enumerate(fruits):
#     print(f"{i} : {fruit}")

# names = ['gildong' , 'chulsu', 'younghe']
# scores = [85, 92, 78]
# for name, score in zip(names, scores):
#     print(f"{name} : {score}점")

# a = 3
# b = 4


# def add(a,b):
#     return a + b

# c = add(a, b)
# print(c)

# def say():
#     return 'Hi'

# a = say()
# print(a)

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# result = add_many(1,2,3,4,5)
# print(result)

# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result = add_mul("add", 1,2,3,4)
# print(result)
# # result = add_mul("mul", 1,2,3,4)
# # print(result)

# def print_kwargs(**kwargs):
#     print(kwargs)
    
# print_kwargs(a = 1)
# print_kwargs(name = 'foo', age = 3)
# print_kwargs(name = 'gildong', age = 25, city = 'seoul', job = 'programmer')

# def create_profile(**info):
#     print("=== profile information ===")
#     for key, value in info.items():
#         print(f"{key}: {value}")
        
# create_profile(name = 'kim', age = 30, job = 'programmer', hobby = 'read')

# def mixed_function(name, *args ,**kwargs ):
#     print(f"name : {name}")
#     print(f"keyword args : {kwargs}")
#     print(f"extra args: {args}")
    
    
# mixed_function('gildong', 1,2,3, age = 25, city = 'seoul')

# def add_and_mul(a,b):
#     return a+b , a*b


# # default2.py
# def say_myself(name,age, man=True): 
#     print(f"나의 이름은 {name}입니다.") 
#     print(f"나이는 {age}살입니다.") 
#     if man: 
#         print("남자입니다.") 
#     else: 
#         print("여자입니다.")
        

# say_myself("park", 25 , True)

# a = 1
# def vartest():
#     global a
#     a = a + 1
    
# vartest()
# print(a)

# a = 1
# def vartest(a):
#     a = a + 1
#     return a

# a = vartest(a)
# print(a)

# def change_list(my_list):
#     my_list.append(4)
    
# a = [1,2,3]
# change_list(a)
# print(a)

# for i in [1,2,3,4,5,6,7,8,9]:
#     print(i , end = "!")

# add = lambda a, b : a+b
# result = add(3,4)
# print(result)

# def add(a,b):
#     """
#     add two numbers

#     Args:
#         a (int, float): first num
#         b (int, float): second num
#     """
#     return a + b

# # print(add.__doc__)
# #1.
# result = 0
# for i in range(1,101):
#     result += i
    
# print(f"sum : {result}")

# #2.
# result2 = 0
# for i in range(1,101):
#     if i % 2 == 0 :
#         continue
#     else :
#         result2 += i
        
# print(f"odd sum : {result2}")

# #.3.
# result3 = 0
# for i in range(1,101):
#     if i % 6 == 0 :
#         result3 += i
#     else:
#         continue
# print(f"6 sum : {result3}")

# total = sum(i for i in range(1,101) if i % 6 == 0)
# print(total)

# total = sum(i for i in range(1, 100, 2))
# print(total)

# #1.
# number = int(input("enter a number : "))

# for i in range(1, number + 1):
#     print(" " * (number - 1) + "*" * (i))
#     number -=1
# print()
    
    
# #2.
# number = int(input("enter a number : "))

# for i in range(0, number):
#     print(" " * (number -1) + "*" * (i * 2 + 1) + " " * (number -1))
#     number -= 1

#3.
# number = int(input("enter a number : "))
# j  = number - 1

# for i in range(0, number*2-1):
#     if i < j + 1  :
#         print(" " * (number -1) + "*" * (i * 2 + 1)
#         if number != 0:
#             number -= 1
#     else :
#         print(" " * (number + 1) + "*" * (j * 2 - 1)
#         j -= 1


# #gpt.
# n = int(input("enter a number : "))

# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
     