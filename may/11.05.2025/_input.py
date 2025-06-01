import sys

fl = open("_writelines.txt", "w", encoding="utf-8")
sys.stdin = fl

try:
    name = input()
    while name != '':
        print(f"Привет, {name}!")
        name = input()
except:
    pass

fl.close()