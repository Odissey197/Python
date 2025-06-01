# print(10/2 % 3)
# print(10/2**3 % 3)
# print(9 % 6 % 2)
# print(2**2**3**2)

number = 4832

val1 = number % 10
val2 = (number - val1) / 10 % 10
val3 = ((number - val1) / 10 - val2) / 10 % 10
val4 = number // 1000

print(val1)
print(val2)
print(val3)
print(val4)