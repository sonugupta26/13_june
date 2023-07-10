# username=input("Enter your username :")
# password=input("Enter your password :")
# while username != "abc@gmail.com" or password != "12345":
#     username=input("Enter your username :")
#     password=input("Enter your password :")
# print("success")
    



# username=input("Enter your username :")
# password=input("Enter your password :")
# if username == "abc@gmail.com" and password == "12345":
#     print("success")
# else:
#     username=input("Enter your username :")
#     password=input("Enter your password :")
    
# n = input(int())
# if n%2==0:
#     print("weird")
# elif n=2 and n=6:
#     print("sonu")


# n = int(input("Enter an integer: "))

# if n % 2 == 0:
#     print("Weird")
# elif n >= 2 and n <= 5:
#     print("Not Weird")
# elif n >= 6 and n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# # Create a list of coordinates using list comprehension
# coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

# # Print the list of coordinates
# print(coordinates)
# x = int(input())
# c = [i for i in range(x + 1)]
# print(c)

class Book:
    def __init__(self, id, code):
        self.id = id
        self.code = code 
    
    
    def oldname(self):
        return self.id
        
    @staticmethod    
    def sumit(name):
        return name
    
    @code.setter
    def code(self, code):
        self.code = code 
    
a = Book("1", "202")
# print(Book.sumit("rahul"))
a.code = "20255"
print(a.code)