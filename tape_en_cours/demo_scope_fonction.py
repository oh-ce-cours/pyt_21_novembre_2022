variable = 1


def example():
    if not hasattr(example, "comptage"):
        print("on configure un truc long à configurer")
        example.comptage = 0
    example.comptage += 1
    print(example.comptage)
    # print(f"{locals()=}")
    # print(f"{globals()=}")
    # print(res, variable)


# def modifie_variable_ok():
#     global variable
#     variable += 1


# def modifie_variable_ok2():
#     # global variable
#     variable += 1


# modifie_variable_ok()
# modifie_variable_ok2()
example()
example()
print(example.comptage)
print(variable)
