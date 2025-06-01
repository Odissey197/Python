def is_simple_number(number):
    for defitel in range(1, number + 1):
        if number % defitel == 0:
            return False
        return True
    
print(is_simple_number(7))
print(is_simple_number(6))