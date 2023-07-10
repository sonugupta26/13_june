# for i in range(1,10):
#     if i % 6 == 0:
#         break
#     print(i)
# print(i)
# print(end = "\n")

# for i in range(1,10):
#     if i % 6 == 0:
#         continue
#     print(i)

# for i in range(1,6):
#     if i % 3 == 0:
#         break
#     print(i)
# else:
#     print("loop is completed")

emails = []
for i in range(5):
    email = input("enter your email :")
    if email.endswith("@gmail.com"):
        emails.append(email)
print(emails)