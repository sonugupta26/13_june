a = {
    "fullname": "Ram",
    "contact": "541512",
    "school": [
        {"name": "ABC School", "year": "2003"},
        {"name": "XYZ Collage", "year": "2047"},
    ],
    "addresh":[
        {"city": "ktm", "from": "2010", "to": "2015"},
        {"city": "lalitpur", "from": "2017", "to": "2023"},
        
    ]
}
#Full Name: Ram
# Contact : 541512
# school 1: ABC Collage, year:2020
# School 2: XYZ Collage, year:2023
# Addresh 1: ktm(2010 to 2015)
# Addresh 2: Lalitpur(2017 to 2023)

print(f"Fullname : {a.get('fullname')}")
print(f"Contact : {a.get('contact')}")
schools = a.get("school")
print(schools)
# for idx, school in enumerate(schools, 1):
#     print(f"School {idx}: {school.get('name')}, {school.get('year')}")
# addreshes = a.get("addresh")
# for idx, addresh in enumerate(addreshes, 1):
#     print(f"Addresh {idx}: {addresh.get('city')}({addresh.get('from')} to {addresh.get('to')})")
