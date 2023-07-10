a = {"name" : "Ram", "contact": 4531654513, "addresh": "ktm"}
# # print(a)
# b=a["contact"]
# # print(b)
# c=a.get("contact")
# # print(c)
# d=a.setdefault("name", "sonu")
# # print(d)
# e=a.setdefault("roll", "25")
# # print(e)
# # print(a)
# f=a.get("gender", "male")
# # print(f)
# print(a)
# b = a.items()
# c = a.values()
# d = a.keys()
# print(b)
# print(c)
# print(d)


# for i in a:
#     print(i)
    
# for i in a.values():
#     print(i)
    
# for k,v in a.items():
#     print(k, v)

# fromkey

# x = ["id", "owner", "addresh", "property",]
# b=dict.fromkeys(x)
# print(x) 

# a.update({"collage2": "xyz collage"})
# print(a)

a.update(fullname = "sita")
# print(a)

b = a.pop("fullname")
# print(b)

c = a.popitem()
print(c)