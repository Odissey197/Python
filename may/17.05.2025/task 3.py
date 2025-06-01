print("Введите любое число: ")
count_mistake = 0
try:
    number = int(input())
    print(number * 2)
except:
    count_mistake += 1
    print("Введены некорректные данные")