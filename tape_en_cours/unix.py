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
        for line in lines[:5]:
            print(line.rstrip())


def tail(n: int):
    """Show tail of a file

    Args:
        n (int): the number of lines to display
    """
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines[:-n]:
            print(line.rstrip())


def nimporte_quoi():



tail(5)
