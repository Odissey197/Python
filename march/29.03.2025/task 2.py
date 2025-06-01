peoples = 20

def print_Pposad():
    global peoples
    peoples = 80
    print(f"Численность населения в Павловском Посаде {peoples} тыс. человек")

def print_Noginsk():
    peoples = 102
    print(f"Численность населения в Ногинске {peoples} тыс. человек")

print(peoples)
print_Pposad()
print_Noginsk()
print(peoples)