results = [
    {
        "name": "Ram",
        "address": "ktm", 
        "reg_number": "216712",
        "marks_obtained":[
            {"subject": "math", "score": 80},
            {"subject": "computer", "score": 0}
        ]
        
        },
    {
        "name": "sita",
        "address": "ktm",
        "reg_number": 27855,
        "marks_obtained":[
            {"subject": "math", "score": 25},
            {"sunjects": "computer", "score": 95}
        ]
        },
    {
       "name": "hari",
        "address": "bkt",
        "reg_number": 28555,
        "marks_obtained":[
            {"subject": "math", "score": 55},
            {"sunjects": "computer", "score": 67}
        ]
        },
]

# Name: Ram
# Address: Ktm
# Registration Number: 216712
# Marks obtained in Maths:
# Marks obtained in Computer:
# Total Marks:Percentage:

# print(f"Name: {results.get(name == 'Ram')}")

for i in results:
    if i.get("name") == "Ram":
        print(f"Name : {i.get('name')}")
        print(f"Address : {i.get('address')}")
        print(f"Regidtration Number : {i.get('reg_number')}")
        marks = i.get('marks_obtained')
        for i in marks:
            if i.get('subject') == "math":
                print(f"Marks of obtained in Math : {i.get('score')}")
            elif i.get('subject') == "computer":
                print(f"Marks obtained in Computer : {i.get('score')}")
                


# c =[]
# a = [
#     {"name": "Ram", "score": 85},
#     {"name": "Hari", "score": 90},
#     {"name": "Sita", "score": 96},
#     {"name": "Suraj", "score": 89},
#     {"name": "Gita", "score": 88}
# ]
#sort the above given list in decending order, on the basis of dict
# for i in range(len(a)):
#     if a[0].get("score") > a[0].get("score"):
#         b.append(a[0])
#     else:
#         b.append(a[1])
#         break
# print(b)
# for i in a:
#     b = i.get("score")
#     c.append(i)
#     d = c.sort()
# print(d)
# a = sorted(a, key=lambda x: x["score"])
# for i in a:
#     print(i)