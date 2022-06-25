

# b = input("Zii ceva: ")

# for i in b:
#     a = []
#     a.append(i)
#     if i == " ":
#         a.remove(i)
# c = "/".join(a)
# print(c)

from unicodedata import numeric


a = 1
try:
    a = int(a)
    print("intiger")
except:
    print("str")
    pass