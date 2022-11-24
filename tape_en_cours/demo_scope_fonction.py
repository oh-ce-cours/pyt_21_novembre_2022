variable = 1


def example():
    global res
    if res == None:
        res = 3
    print(f"{locals()=}")
    print(f"{globals()=}")
    print(res, variable)


# def modifie_variable_ok():
#     global variable
#     variable += 1


# def modifie_variable_ok2():
#     # global variable
#     variable += 1


# modifie_variable_ok()
# modifie_variable_ok2()
example()
print(variable)
