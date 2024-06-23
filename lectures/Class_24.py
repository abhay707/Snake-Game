# Unlimited positional arguments
# import math

# def add(*args):
#     sum = 0
#     for n in args:
#        sum += n
#     return sum
#
# print(add(1, 2, 3, 4))

# #Unlimited keyword arguments
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():#kwargs takes arguments as tuple and also can put it in key value pairs
#     #     print(key)
#     #     print(value)
#
#     n += kwargs["add"]#we can apply operations to the selected arguments
#     n *= kwargs["multiply"]
#     print(n)
#     # print(kwargs["add"]) #it is used to get hold of a particular value
#
# calculate(2, add=3, multiply=5)# we can pass unlimited value but n is constant it has to be valued
#
# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw.get("model")#get is used so if we call this value none is assigned
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")
#
# my_car = Car(make="gtr")
# print(my_car.model())

# import math
#
# minimum = int(input())
# maximum = int(input())
#
# list1 = []
#
# for Number in range(minimum, maximum):
#     Temp = Number
#     Sum = 0
#     while (Temp > 0):
#         Reminder = Temp % 10
#         Factorial = math.factorial(Reminder)
#         Sum = Sum + Factorial
#         Temp = Temp // 10
#
#     if (Sum == Number):
#         list1.append(Number)
#
# print(list1)


# input_str = input()
# my_list = list(map(int, input_str.split()))
#
# if len(my_list) < 2:
#     print(-1)
#
# sorted_numbers= sorted(my_list)
# second_largest = sorted_numbers[-2]
# second_smallest = sorted_numbers[1]
#
# even_numbers = []
# for num in range(second_smallest + 1, second_largest):
#     if num % 2 == 0:
#         even_numbers.append(num)
#
# print(even_numbers)


# input_str = input()
# my_list = list(map(int, input_str.split()))
#
# def is_perfect_square(num):
#     square_root = int(math.sqrt(num))
#     return  square_root * square_root == num
#
# updated_list = []
# for num in my_list:
#     if num < 0:
#         updated_list.append("$")
#     elif is_perfect_square(num):
#         updated_list.append("@")
#     else:
#         updated_list.append("!")
#
# print(updated_list)

n = int(input())
for i in range(1, n + 1):
    line = "1"
    for j in range(1, i + 1):
        line += " " if j + 2 != i else str(j + 1)
        if j == n:
            line += "\n"
        if j == n:
            for k in range(1, n + 1):
                line += str(k)
    if i == 1:
        continue
    print(line)
