import itertools
from collections import deque
import sys
import click


def cat():
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            print(line.rstrip())


def cat_iter():
    with open("./plus_moins.py", encoding="utf8") as f:
        for line in itertools.islice(f, 3, 10, 2):
            print(line.rstrip())


def tac():
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in reversed(f):
            print(line.rstrip())


def head():
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines[:5]:
            print(line.rstrip())


def head_lazy_1():
    with open("./plus_moins.py", encoding="utf8") as f:
        line_number = 0
        for line in f:
            line_number += 1
            if line_number > 5:
                break
            print(line.rstrip())


def head_lazy_1():
    with open("./plus_moins.py", encoding="utf8") as f:
        for line_number, line in enumerate(f):
            if line_number > 5:
                break
            print(line.rstrip())


def head_lazy_2():
    with open("./plus_moins.py", encoding="utf8") as f:
        for line, _ in zip(f, range(5)):
            print(line.rstrip())


def head():
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines[:5]:
            print(line.rstrip())


@click.command()
@click.option("--filename", "-f", help="File to tail.")
@click.option("--number", "-n", default=10, help="NUmber of lines to display.")
def tail(filename: str, number: int):
    """Show tail of a file

    Args:
        number (int): the number of lines to display
    """
    with open(filename, encoding="utf8") as f:
        lines = f.readlines()
        for line in lines[-number:]:
            print(line.rstrip())


def tail_lazy():
    with open("./plus_moins.py", encoding="utf8") as f:
        for index, _ in enumerate(f):
            pass
        nb_total = index
        print(nb_total)

    with open("./plus_moins.py", encoding="utf8") as f:
        for index, line in enumerate(f):
            if nb_total - index < 5:
                print(line.rstrip())


def tail_lazy_2():
    with open("./plus_moins.py", encoding="utf8") as f:
        q = deque(f, maxlen=10)
    print(q)


def nimporte_quoi():
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines[5:-10:3]:
            print(line.rstrip())


# filename = "./plus_moins.py"
# n = 10
tail()
# python unix.py -f fizzbuzz.py -n 3
