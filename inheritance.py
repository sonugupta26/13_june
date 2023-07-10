# class Animal:
#     pass

# class Dog(Animal):
#     pass


# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password
        
#     def login(self, uname, pwd):
#         if uname == self.username and pwd == self.password:
#             print("Loggin success")
#         else:
#             print("not match")
        
        
# class Person(User):
#     def __init__(self, _id, username, password, name, address):
#         super().__init__(_id, username, password)
#         self.name = name
#         self.address = address
        
# class Teacher(Person):
#     def __init__(self, id, username, password, name, address, designation):
#         super().__init__(id, username, password, name, address)
#         self.designation = designation
        
        
        
# class Student(Person):
#     def __init__(self, _id, username, password, name, address, roll):
#         super().__init__(_id, username, password, name, address)
#         self,roll = roll
        
#     def __str__(self):
#         return self.name
        
# # a = Teacher(1, "suchak123", "abc123", "suchak", "ktm", "10")
# # a.login("suchak1232", "abc123")

# b=Student(2, "sonu", "sonu", "sonu", "bkt", "01")
# b.login("sonu", "sonu")


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     # def __eq__(self, obj):
#     #     return self.price == obj.price
    
#     def __gt__(self, obj):
#         return self.price > obj.price
    
    
# p1 = Product("jacket", 2000)
# p2 = Product("pants", 1600)
# print(p1 == p2)
# print(p1 > p2)

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
class Teacher(Person):
    def __init__(self, name, address, contact):
        super().__init__(name, address)
        self.contact = contact
        b = print(f"{self.name, self.address, self.contact}")
        return b
        
class Student(Teacher):
    def __init__(self, name, address, contact, roll):
        super().__init__(name, address, contact)
        self.roll = roll
       
        
a = Person("sonu", "kathmandu")
b = Teacher()