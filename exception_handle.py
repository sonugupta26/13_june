# try:
#     a = int(input("Enter your number : "))
#     b = int(input("Enter your aother number : "))
#     print(a+b)
# except ValueError:
#     print("only integer is accepted")
    
# name = input("enter your name")
# print(name)

# a = [1,2,3,4]
# try:
#     print(a[4])
# except IndexError:
#     print("index is not found")

while True:
    try:
        a = int(input("Enter number : "))
        b = int(input("Enter number : "))
        print(a+b)
        break
    except ValueError:
        print("asknlniojas")
        continue

    

    