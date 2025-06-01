fl = open("_writelines.txt", "r", encoding="utf-8")

lst = fl.readlines()[-2]
fl.close()

fl = open("task2.txt", "w", encoding="utf-8")

fl.writelines(lst)
fl.close()