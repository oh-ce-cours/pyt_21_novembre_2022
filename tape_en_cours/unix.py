def cat():
    with open("./plus_moins.py", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            print(line.rstrip())


cat()
