def cat():
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            print(line.rstrip())


def tac():
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in reversed(lines):
            print(line.rstrip())


def head():
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            print(line.rstrip())


tac()
