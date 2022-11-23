def cat():
    with open("./plus_moins.py") as f:
        for line in f:
            print(line.rstrip())


cat()
