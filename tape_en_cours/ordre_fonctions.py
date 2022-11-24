"""bla
"""
f_1()
f_2()

def f_2():
    """bla"""
    print("dans f2")
    f_1()


def f_1():
    """bla"""
    print("dans f1")


f_2()
