
with open("task4.txt", "r", encoding="utf-8") as fl, open("task4_1.txt", "r", encoding="utf-8"):
    text = fl.read().strip().split()
    text = [i.strip(".,!?;:\"'_") for i in text]
    new_text = [f"{i}\n" for i in text if len(i)>=7]
    print(text)
    fl.writelines(new_text)