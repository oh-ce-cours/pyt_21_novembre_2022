variable = 1


def example():
    if not hasattr(example, "toto"):
        print("on configure un truc long à configurer")
        example.toto = 
    print(example.toto)
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
print(variable)
