# class Car:
#     pass
# #print(Car())
# c = Car()
# print(c)


# class Car:
#     def __init__(self):#initializer function
#         pass

# c=Car()
# c.color="red"
# c.year="2020"
# print(c.color)
# print(c.year)


# class Car:
#     def __init__(self, colors, years):
#         self.color=colors
#         self.year=years
# c = Car("red", "2020")
# print(c.color)
# print(c.year)

# class Bike:
#     def __init__(self, name, mfd):
#         self.name = name
#         self.mfd = mfd
        
#     def abc(self):
#         print(f"the name of bike is {self.name}, and manufactures on {self.mfd}")
        
        
# a = Bike("bmw", "2023")
# a.abc()


# class Printer:
#     def __init__(self, num_of_pages, model):
#         #instance variable
#         self.model = model
#         self.num_of_pages = num_of_pages
        
#     def paper_print(self):#instance method
#         print(f"{self.model} is printing {self.num_of_pages} pages.")
        
# p = Printer(10, "Brother DW4")
# p.paper_print()

# class Laptop:
#     company = "lenevo" #class variable
#     def __init__(self, color, model, ram_size):
#         self.color = color
#         self.model = model
#         self.ram_size = ram_size
        
#     def start(self):
#         print(f"the color of laptor is {self.color}")
        
        
#     def shut_down(self):
#         print(f"the ram_size is {self.ram_size}.")
        
# a=Laptop("black", "2022", "10gb")
# a.start()
# a.shut_down()
        
# class Calculator:
#     def __init__(self, x: float, y: int) -> None:
#         self.x = x
#         self.y = y
        
        
#     def add(self):
#         return self.x + self.y

#     def product(self):
#         return self.x * self.y
    
#     @staticmethod    
#     def square_root(num):
#         return num ** 0.5
    
# a = Calculator(10, 20)
# print(a.add())
# print(a.product())

# print(Calculator.square_root(25))

class ProductPriceError(Exception):
    pass
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price <= 0:
           raise ProductPriceError("could not set price less than zero")
        self.__price = price
        
    
if __name__ == "__main__":
    p = Product("Tshirt", 1000)
    print(p.name)
    print(p.__dict__)
    try:
        p.price = -1
    except ProductPriceError as err:
        print(err)
        
    # print(p.price)
    # print(p.__dict__)
    
         
