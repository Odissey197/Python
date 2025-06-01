num = int(input("Введите любое целое число: "))
new_num = 0
while num != 0:
    # print("num % 10 =", num % 10)
    new_num = new_num * 10 + num % 10
    num = num // 10
    # print("new_num =", new_num)
    # print("num =", num)
print(new_num)