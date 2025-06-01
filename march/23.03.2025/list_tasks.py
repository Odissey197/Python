# ls1 = [1, 22, -12, -4, -27, 5, 108, 45, 34, 98]

# # Сумма отрицательных чисел
# s = 0
# for i in ls1:
#     if i < 0:
#         s += i
#         # s = s + 1
# print(s)

# # Сумма четных чисел
# s = 0
# for i in ls1:
#     if i % 2 == 0:
#         s += i
# print(s)

# # Сумма нечетных чисел
# s = 0
# for i in ls1:
#     if i % 2 != 0:
#         s += i
# print(s)

# # Произведение чисел с индексами кратными 3
# s = 1
# for i in range(len(ls1)):
#     if i % 3 == 0:
#         s *= ls1[i]
# print(s)

# Произведение эелементов между минимальным и максимальным значениями
ls1 = [1, 22, -12, -4, -27, 5, 108, 45, 34, 98]
ls1_max = max(ls1)
ls1_min = min(ls1)
print(ls1_max * ls1_min)

a = ls1.index(ls1_max)
b = ls1.index(ls1_min)

ls1 = ls1[a+b]

# Произведение 
s = 0
v = 0

for i in range(len(ls1)):
    if ls1[i] > 0:
        s = i
        break

for i in range(len(ls1)):
    if ls1[i] > 0:
        v = i
        break