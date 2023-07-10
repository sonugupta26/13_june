# colors = ["red", "blue", "yellow", "red", "green"]
# # #colors_to_remove = ["blue", "red"]
# for i in colors:
#     if i == "blue" or i == "red":
#         colors.remove(i)
# print(colors)

# # method of sir
# for i in colors:
#     if i in colors_to_remove:
#         colors.remove(i)
# print(colors)

# fruits = ["apple", "grapes", "banana", "mango", "guava"]
# #replace "grapes" and  "banana" with "litch"
# # for i in range(len(fruits)):
# #     if fruits[i] == "grapes" or fruits[i] == "banana":
# #         fruits[i] = "lichi"
# # print(fruits)
# #method of sir
# fruits[1:3]=["litchi"]
# print(fruits)


# take user input and remove it from list if present
# list1 = [1, 2 , 5, 9, 55, 65, 15]
# input = [int(input("Enter your number :"))]
# for i in list1:
#     if i in input:
#         list1.remove(i)
# print(list1)


# #find the sum of odd numbers of between 1 and 100
# total = 0
# for i in range(1,101,2):
#     total = total+i
# print(total)
    
    
   
# num = int(input("Enter your number :"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")
    
# a = "12d57d36d19" #find the sum of 12,57,36 and 19
# b=a.strip().split("d")
# print(b)
# total=0
# for i in b:
#     total=total+int(i)
# print(total)


# total=0
# a = "387$12.45f"

# b=a.split("$")
# print(b)
# c=b.split(".")
# print(c)
# # d=c.("f")
# # print(d)
# for i in a:
#     if i.isnumeric():
#         total = total + int(i)
# print(total)


#questions


# b = "65a4","33535d"
# print(b)


# c = "ds4","3545","ff6556"
# print(c)

# d = "12d45d445d85"
# d="-".join(d)
# print(d)

# d = "12d45d445d85"
# d=d.split("d")
# print(d)

a =[1,2,3,4,5]
a[1:3]=[22]
print(a)