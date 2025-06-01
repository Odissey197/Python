print("Введите любое число: ")
try:
    number = int(input())
    print(number * 2)
    print(number / 2)
    print(number + 2)
    print(number - 2)
except ValueError:
    print("Введены некорректные данные")

except ZeroDivisionError:
    print("Ошибка деления на ноль")

except:
    print("Какая-то ошибка")