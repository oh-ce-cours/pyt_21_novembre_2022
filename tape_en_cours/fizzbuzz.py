import time

# tic = time.time()
# for nombre in range(1, 101):
#     if nombre % 3 == 0 and nombre % 5 == 0:
#         print("fizz")
#     elif nombre % 5 == 0:
#         print("buzz")
#     elif nombre % 3 == 0:
#         print("fizzbuzz")
#     else:
#         print(nombre)
# print(time.time() - tic)


def divisible_par_3(nombre):
    return nombre % 3 == 0


def divisible_par_5(nombre):
    return nombre % 5 == 0


for nombre in range(1, 101):
    res = ""
    if divisible_par_3(nombre):
        res += "fizz"
    if divisible_par_5(nombre):
        res += "buzz"
    if not res:
        res = str(nombre)
    print(res)

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

# for nombre in range(1, 101):
#     print("fizz" * (nombre % 3 == 0) + "buzz" * (nombre % 5 == 0) or str(nombre))
