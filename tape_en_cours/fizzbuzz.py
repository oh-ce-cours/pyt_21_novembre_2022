# for nombre in range(1, 101):
    est_divible_3 = nombre % 3 == 0
    if est_divible_3 and nombre % 5 == 0:
        print("fizz")
    elif nombre % 5 == 0:
        print("buzz")
    elif est_divible_3:
        print("fizzbuzz")
    else:
        print(nombre)

# for nombre in range(1, 101):
#     res = ""
#     if nombre % 3 == 0:
#         res += "fizz"
#     if nombre % 5 == 0:
#         res += "buzz"
#     if not res:
#         res = str(nombre)
#     print(res)

# for nombre in range(1, 101):
#     match (nombre % 3, nombre % 5):
#         case (0, 0):
#             print("fizzbuzz")
#         case (_, 0):
#             print("buzz")
#         case (0, _):
#             print("fizz")
#         case _, _:
#             print(nombre)

for nombre in range(1, 101):
    print("fizz" * (nombre % 3 == 0) + "buzz" * (nombre % 5 == 0) or str(nombre))
