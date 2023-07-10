# a = [i for i in range(1, 10)]
# print(a)


# b = [i for i in range(1, 20) if i % 3 == 0 ]
# print(b)

# c = [i if i % 5 == 0 else 0 for i in range(1,25)]
# print(c)

d = sum([i  for i in range(1,101) if i%3==0 or i%5==0 or i%15==0])
print(d)

  # my way  
# for i in range(1, 51):
#     if i % 3 == 0:
#         print("go")
#     if i % 5 == 0:
#         print("done")
#     if i % 3 == 0 and i % 5 == 0:
#         print("both")
#     else :
#         print("none") 



# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("done and go")
#     elif i % 3 == 0:
#         print("go")
#     elif i % 5 == 0:
#         print("done")
#     else :
#         print("none")

#find the sum of multiples of 3, 5 and 15 between 1 to 100
# total = 0
# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
#         print(i)
#         total = total + int(i)
# print(total) 

        
# total= 0
# a = ["python", 78,  "hello",  10, 6, 8, "apple", 60]
# for i in a:
#     if isinstance(i, int):
#         total = total+i
# print(total)


# a = ["python", 78, "98", "hello",  10, 6, 8, "64", "apple", "9", 60]
# # total = 0
# # for i in a:
# #     if isinstance(i, str) and i.isnumeric():
# #         total += int(i)
# #     elif isinstance(i, int):
# #         total += i
# # print(total)

# print(sum(map(int, filter(lambda n : isinstance(n, int) or (isinstance(n, str) and n.isnumeric()), a))))