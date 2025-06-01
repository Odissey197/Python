# def is_simple_number(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#         return True
    
# lst = [3, 65, 7, 10]
# for i in lst:
#     print(is_simple_number(i))

# def divide_by_2(number):
#     return number/2

# lst = [354, 54, 7, 998, 67]
# lst = list(map(divide_by_2, lst))
# print(lst)

# lambda number: number/2

lst = [354, 54, 7, 998, 67]
lst = list(map(lambda number: number/2, lst))
print(lst)

my_func = lambda x: x/2

print(my_func(1200))