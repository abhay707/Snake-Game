#Unlimited positional arguments

# def add(*args):
#     sum = 0
#     for n in args:
#        sum += n
#     return sum
#
# print(add(1, 2, 3, 4))

#Unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():#kwargs takes arguments as tuple and also can put it in key value pairs
    #     print(key)
    #     print(value)

    n += kwargs["add"]#we can apply operations to the selected arguments
    n *= kwargs["multiply"]
    print(n)
    # print(kwargs["add"]) #it is used to get hold of a particular value

calculate(2, add=3, multiply=5)# we can pass unlimited value but n is constant it has to be valued

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")#get is used so if we call this value none is assigned
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="gtr")
print(my_car.model())