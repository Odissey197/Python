def check_age(age):
    if age < 18:
        raise ValueError("Возраст должен быть больше 18 лет")
    elif age > 100:
        raise ValueError("Не советую, пенсия")

age = int(input("Ввдите свой возраст: "))
try:
    check_age(age)
except Exception as e:
    print(e)