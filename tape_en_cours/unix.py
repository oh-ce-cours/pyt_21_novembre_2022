def cat():
    with open("./plus_moins.py", encoding="cp1252") as f:
        for line in f:
            print(line.rstrip())


cat()
