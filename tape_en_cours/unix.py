def cat():
    with open("./plus_moins.py", encoding="utf8") as f:
        for line in f:
            print(line.rstrip())


cat()
