a = ["1","2","3","Ram","60"]
for i in a:
    if i.isdigit():
        a.remove(i)
print(a)