# for nombre in range(1, 101):
#     if nombre % 3 == 0 and nombre % 5 == 0:
#         print("fizz")
#     elif nombre % 5 == 0:
#         print("buzz")
#     elif nombre % 3 == 0:
#         print("fizzbuzz")
#     else:
#         print(nombre)

for nombre in range(1, 101):
    res = ""
    if nombre % 3 == 0:
        res += "fizz"
    if nombre % 5 == 0:
        res += "buzz"
    if res == "":
        ...
    print(res)
