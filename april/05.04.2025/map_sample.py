def is_simple_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        return True
    
lst = [2, 234, 89, 21 ,8, 34, 98, 21, 67, 945]
lst_2 = list(map(is_simple_number, lst))