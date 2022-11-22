# for nombre in range(1, 101):
#     if nombre % 3 == 0 and nombre % 5 == 0:
#         print("fizz")
#     elif nombre % 5 == 0:
#         print("buzz")
#     elif nombre % 3 == 0:
#         print("fizzbuzz")
#     else:
#         print(nombre)

# for nombre in range(1, 101):
#     res = ""
#     if nombre % 3 == 0:
#         res += "fizz"
#     if nombre % 5 == 0:
#         res += "buzz"
#     if not res:
#         res = str(nombre)
#     print(res)

for nombre in range(1, 101):
    match nombre % 3, nombre %5:
        case pattern-1:
            action-1
        case pattern-2:
            action-2
        case pattern-3:
            action-3
        case _:
            action-default