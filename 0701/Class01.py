# class Calculator:
#     def __init__(self):
#         self.result = 0
        
#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))


# class Fourcal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
    
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
        
#     def add(self):
#         result = self.first + self.second
#         return result
    
#     def sub(self):
#         result = self.first - self.second
#         return result
    
#     def multi(self):
#         result = self.first * self.second
#         return result
    
#     def div(self):
#         if self.second !=0 :
#             result = self.first / self.second
#             return result
#         else:    
#             return print("Can't divide by 0")
        

# class MoreFourcal(Fourcal):
#     def pow(self):
#         result = self.first ** self.second
#         return result


# class SafeFourcal(Fourcal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
        

# class Familly:
#     lastname = "kim"
    
# a = Familly()
# b = Familly()
# a.lastname = "park"

# print(a.lastname)
# print(b.lastname)

# import mod01
# print(mod01.add(3,4))

# from mod01 import *
# print(sub(4,2))

# from game.sound import *

# echo.echo_test()

# from game.graphic.render import render_test
# render_test()

# n = int(input("enter a num : "))
# fact = 1
# for i in range(n , 0 , -1):
#     fact *= i

# print(fact)

# n = int(input("enter a num : "))
# fact = 1

# print(f"{n}! = ", end="")
# for i in range(n, 0, -1):
#     print(i,end="")
#     if i != 1:
#         print(" x ", end="")
#     if i == 1:
#         print(" = ", end = "")

        
# for i in range(n, 0 , -1):
#     fact *= i

# print(f"{fact}")


# try:
#     a=[1,2]
#     print(a[3])
#     print(4/0)
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

# try:
#     age =int(input('나이를 입력하세요 : '))
# except:
#     print("입력이 정확하지 않습니다.")
# else:
#     if age <= 18:
#         print("no pass")
#     else:
#         print("welcome")


# students = ['kim', 'lee', 'park', 'choi']

# for student in students:
#     try:
#         with open(f"{student}_score.txt", 'r') as f:
#             score = f.read()
#             print(f"{student} score is : {score}")
#     except FileNotFoundError:
#         print(f"{student} score can't find. skip")
#         continue

# try:
#     with open("file.txt",'r') as f:
#         config = f.read()
# except FileNotFoundError:
#     pass

# print("program success")


# class Bird:
#     def fly(self):
#         print("very fast")
    
    
# class Eagle(Bird):
#     pass

# eagle = Eagle()
# eagle.fly()

# class Myerror(Exception):
#     def __str__(self):
#         return "not allow"

# def say_nick(nick):
#     if nick == 'idiot':
#         raise Myerror()
#     print(nick)
   
# try:
        
#     say_nick("angel")
#     say_nick("idiot")
# except Myerror as e:
#     print(e)

# def get_rect_area(w,h):
#     """Calculate the area of a rectangle."""
#     return w*h

# def main():
#     width = float(input("enter the width of the rectangle: "))
#     height = float(input("enter the height of the rectangle: "))
    
#     area = get_rect_area(width,height)
#     print(f"the area of the rectangle is : {area} ")
    
# if __name__ == "__main__":
#     main()

# def menu():
#     print("1.섭씨 온도 -> 화씨 온도")
#     print("2.화씨 온도 -> 섭씨 온도")
#     print("3. 종료 ")
#     selection = int(input("plz select the menu : "))
#     return selection

# def ctof(c):
#     temp = c * 9 / 5 + 32
#     return temp

# def ftoc(f):
#     temp = (f - 32) * 5 / 9
#     return temp

# def input_f():
#     f= float(input("화씨 온도를 입력하시오: "))
#     return f
    
# def input_c():
#     c = float(input("섭씨 온도를 입력하시오 : "))
#     return c

# def main():
#     while True:
#         index = menu()
#         if index == 1:
#             t = input_c()
#             t2 = ctof(t)
#             print(f"화씨 온도 = {t2} \n")
#         elif index == 2:
#             t = input_f()
#             t2 = ftoc(t)
#             print("섭씨 온도 =", t2, "\n")
#         else:
#             break
# if __name__ == "__main__":
#     main()

# n = 0
# for i in range(999,0,-1):
#     if (i % 3 == 0) or (i % 5 == 0):
#         n += i
#     else:
#         continue

# print("num = " , n)

# import random

# nums = random.sample(range(1,10),3)

# def compare():
#     num1 = input("guess num : ")
#     num_guess = list(map(int, num1))
#     answer=[0]*3
    
#     for i in range(3):
#         if nums[i] == num_guess[i]:
#             answer[i] = "스트라이크"
            
#         else:
#             for j in range(3):
#                 if nums[i] == num_guess[j]:
#                     answer[i] = "볼"
#                     break
#                 else:
#                     answer[i] = "아웃"
    
    
#     dap = random.sample((answer),len(answer))                
#     return dap


# print("play the baseball !")

# while True:
    
#     ball = compare()  
#     if ball == ["스트라이크", "스트라이크", "스트라이크"]:
#         print("congratuation!")
#         break
#     else :
#         print(ball)

# # c:/doit/baseball.py
# import random

# nums = random.sample(range(1, 10), 3)
# count = 0

# while True:
#     question = input("3자리 숫자를 입력하세요: ")
#     guess = list(map(int, question))
#     count += 1

#     strike = 0
#     ball = 0

#     for i in range(3):
#         if guess[i] == nums[i]:
#             strike += 1
#         elif guess[i] in nums:
#             ball += 1

#     if strike == 3:
#         print(f"정답! {count}번 만에 맞혔습니다.")
#         break

#     print(f"{strike}스트라이크 {ball}볼")
