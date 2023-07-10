


# def calculator(operator):
#     def addition(a, b):
#         return a+b
#     def difference(a,b):
#         return a-b
#     def product(a,b):
#         return a*b
#     def division(a,b):
#         return a/b
#     if operator =="+":
#         return addition
#     elif operator == "-":
#         return difference
#     elif operator == "*":
#         return product
#     elif operator == "/":
#         return division
# a=calculator("-")
# print(a(9,5))

# def increase_by(num):
#     def factor(func, x,y):
#         return func(x,y) + num
#     return factor

# def exponent(x,y):
#     return x**y

# def addition(x,y):
#     return x+y

# increase_by_ten = increase_by(10)
# increase_by_twenty = increase_by(20)
# # print(increase_by_ten(exponent, 2,5))
# print(increase_by_twenty(addition, 3,4))



# def addition(a, b):
#     return a+b

# total = addition(5, 8)
# print(total)

# def outer():
#     print("i am outer")
#     def inner():
#         print("i an inner")
#     inner()
# outer()

###################################################################

# def outer():
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#     return inner

# a = outer()
# a()

#####################################################################

# def outer(n):
#     def first_child():
#         print("I am first child")
#     def second_child():
#         print("I am second child")
#     if n==1:
#         return first_child
#     elif n==2:
#         return second_child
    
# a=outer(2)
# a()

#####################################################################

# def a1(b):
#     b()
    
# def a2():
#     print("Hii i am a2")
    
# def a3():
#     print("Hii i am a3")
    
# a1(a3)

######################################################################

# def decurator(a):
#     def wrap():
#         print("hii  i am first")
#         a()
#         print("hii  i  am third")
#     return wrap

    # def wrap2():
    #     print("hii i am 1st")
    #     a()
    #     print("hii i am 3rd")
    # return wrap2


# def sonu():
#     print("hii  i am second")

# a=decurator(sonu)
# a()
# a()

##################################################################################################
def smart_division(func):

    def wrapper(a, b):
        if b == 0:
            return "could not divide by zero"
        return func(a, b)
    return wrapper



def division(a, b):
    return a/b

print(division(10,5))
result = division(10,5)
print(result)