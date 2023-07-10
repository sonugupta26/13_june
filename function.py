# def abc(name, contact):
#     print(f"NAME:{name}")
#     print(f"CONTACT:{contact}")
# abc("sonu", 776757757)
4
##################################################################################

#function with and without return tupe

# def addition(num1, num2):
#     total = num1 + num2
#     return total 
# result = addition(5,8)
# print(result)

# def fac(num1, num2):
#     r = num1*num2
#     print("this is factorial")
#     return r

# a=fac(5,5)
# print(a)

#########################################################################################

# def sub(num1, num2):
#     a=num1-num2
#     print(a)
# sub(10,5)

#####################################################################################################


# def compare(num1, num2, num3):
#     if num1 > num2:
#         return num1
#     elif num2 > num3:
#         return num2
#     else:
#         return num3
          
# result=compare(5,8,9)
# print(f"{result} is greater")

######################################################################################


# def simpleinterest(p, t, r):
#     si=p*t*r/100
#     return si
# result = simpleinterest(10000,2,4)
# print(result)

###################################################################################

# def odd_even(input):
#     if num % 2 == 0:
#         return "true"
#     else:
#         return "false"
# input=int(input("Enter your number"))  
# result = odd_even(input)
# print(f"The number is {result}")


########################################################################################

# user_input_val = int(input("Enter your val :"))
# def factorial(user_input_val):
#     fac=1
#     for i in range(user_input_val,1,-1):
#         fac = fac * i
#     return fac

# result = factorial(user_input_val)
# print(f" The factorial of {user_input_val} is {result}")
   
######################################################################################### 
    
# def fibbonaci(n):
#     a=0
#     b=1
#     for i in range(n):
#         c=a+b
#         a=b
#         b=c
#     return c
# n=int(input("Enter your number: "))        
# result = fibbonaci(n)
# print(result)

###########################################################################################

# def display_profile(name, contact, addresh):
#     print(f"Name:{name}")
#     print(f"Contact:{contact}")
#     print(f"Addresh:{addresh}")
    
# display_profile("sonu", "ktm", 97121519715)#position argument
# display_profile(name="monu", addresh="birgunj", contact=874411584)#keyword argument

###############################################################################################

# def exponent(base, power=2):
#     return base ** power

# print(exponent(5,3))
# print(exponent(6))

##############################################################################################

# def odd_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# num1=int(input("Enter your number :"))  
# result = odd_even(num1)
# print(f"The number is {result}")

##############################################################################################

# def calculate(cost, sell):
#     r=sell-cost
#     if sell > cost:
#         return "profit:"
# a=int(input("Enter your cost price :"))
# b=int(input("Enter your sell price"))
# result = calculate(a,b)
# print(f"")

###############################################################################################

# def prifit_or_loss(cost_price, sale_price):
#     if cost_price > sale_price:
#         print(f"Loss :{cost_price-sale_price}")
#         # loss = cost_price - sale_price
#         # print(f"Loss Rs.{loss}")
#     else:
#         print(f"Profit : {sale_price - cost_price}")
#         # Profit = sale_price - cost_price
#         # print(f"Profit Rs.{Profit}")
# prifit_or_loss(200, 500)
# prifit_or_loss(300,100)

################################################################################################

# def example(*args):
#     print(args)
# example(1,2,2,54,5)

# def example2(**k):
#     print(k)
# example2(name = "ram", addresh = "ktm")
   
   
# def example3(*args, **kwargs):
#     print(args)
#     print(kwargs)

# example3(1,2,3,5,3,5, name="ram", contact=656323)




