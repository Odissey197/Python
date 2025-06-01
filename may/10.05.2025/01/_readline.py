fl = open("_readline.txt", "w", encoding="utf-8")

# print(fl.readline())

line = fl.readline()
while line != "":
    if line[0] == "7":
        print(line, end='')
    line = fl.readline()

fl.close()