# while True:
#     print("this is python")

# a=1
# while a < 10:
#     print("this is python ")
#     a = a+1

# a=1
# while a<6:
#     input("Enter your name :")
#     a =a+1


# username = input("enter your username :")
# password = input("enter your password :")
# while username!="ram@gmail.com" or password != "abc@gmail.com":
#     username = input("please enter your username :")
#     password = input("please enter your password :")
# print("match your username and password")


main = []
odd = []
even = []
duplicate = []
# for i in range(5):
#     num = int(input("enter your number :"))
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
#     main.append(num)
#     if 
for i in range(6):
    num = int(input("Enter number :"))
    if num not in main:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    else:
        duplicate.append(num)
    main.append(num)
print(even)
print(odd)
print(duplicate)
print(main)
    