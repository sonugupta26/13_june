# def func():
#     print("this is function")
# a=func #b = 10
# a()
# func()
# ########################################################################


# def addition(a, b):
#     return a+b 
# # print(addition(5,5))
# total = addition
# print(total(30,55))

# #######################################################################

# def outer():
#     print("i am outer function")
#     def inner():
#         print("i an inner function")
#     inner()
# outer()

# ############################################################################

# def outer():
#     print("this is outer")
#     def inner():
#         print("this is inner")
#     return inner


# i = outer()
# i()

#################################################################################

# def outer(n):
#     def first_child():
#         print("i am first child")
#     def second_child():
#         print("i am second child")
#     if n == 1:
#         return first_child
#     elif n == 2:
#         return second_child
# first = outer(1)
# second = outer(2)
# first()
# second()

##################################################################################

# def greet(func):
#     func()
    
# def welcome():
#     print("welcome Ram")
    
# def bye():
#     print("bye bye ram")
    
# greet(welcome)
# greet(bye)

########################################################################################

# def decurator_function(func):
#     def wrapper():
#         print("Something can be done before")
#         func()
#         print("Something can be done after")
#     return wrapper

# # @decurator_function

# def example():
#     print("I an example function")
    
# a=decurator_function(example)
# a()
    
# example()

#################################################################################

# # import time
# # def Show_timing(func):
# #     def wrapper():
# #         start_time = time.time()
# #         result = func()
# #         elapsed_time = time.time() - start_time
# #         print(f"Total time taken by {func}: {elapsed_time}")
# #         return result
# #     return wrapper

#############################################################################


# # @Show_timing
# # def multiple_of_five():
# #     a = []
# #     for i in range(5, 100000, 5):
# #         a.append(i)
# #     return a

# # print(multiple_of_five())


###############################################################################################
# def smart_division(func):
#     def wrapper(a, b):
#         if b == 0:
#             return "could not divide by zero"
#         return func(a, b)
#     return wrapper

# @smart_division
# def division(a, b):
#     return a/b

# print(division(10,5))
# print(division(20, 0))
############################################################################################
#  def wrapper(a, b):
#         if b == 0:
#             return "could not divide by zero"
#         return func(a, b)
#     return wrapper


# def division(a, b):
#     return a/b

# print(division(10,5))
# result = division(10,5)
# print(result)











####################################################################################################

#lamda function

# a = lambda x,y,z:x+y+z
# print(a(5,5,6))

# map, filter

# a = lambda n:n, range(1,100)
# print(a)

# numbers = map(lambda x: x, range(1, 101))
# print(numbers)

###################################################################################################

# alist=[1, 2, 3, 4, 5, 6, 7, 8]

# blist = []
# for i in alist:
#     blist.append(i+1)
    
# print(blist)
# def increment(n):
#     return n+1

# res = map(lambda n:n+1, alist)
# print(tuple(res))
# print(list(res))

#################################################################################################

# names = ["ram", "syam", "hari", "gita", "sita"]
 
# result = map(lambda name:name.capitalize(), names)
# print(tuple(result))

#################################################################################################

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(list(filter(lambda n:n%2!=0, numbers)))

#################################################################################################


# emails = ["1@gmail.com", "2@gmail.com", "3@gmail.com", "4@yahoo.com"]
# print(list(filter(lambda email:email.endswith("1@gmail.com"), emails)))

##################################################################################################
print(sum(filter(lambda n : n%3==0 or n%5==0 or n%15==0, range(1, 101))))
 
####################################################################################################
