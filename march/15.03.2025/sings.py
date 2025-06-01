s = "Тео́рия относи́тельности — физическая теория пространства-времени, то есть теория, описывающая универсальные пространственно-временные свойства физических процессов." "Термин был введён в 1906 году Максом Планком с целью подчеркнуть роль принципа относительности в специальной теории относительности."

# print(s)
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.swapcase())

# Поиск подстроки в строке
# print(s)
# print(s.count("."))
# print(s.count(".",20))
# print(s.count(".",20, 30))

# print(s)
# print(s.find("."))
# print(s.find(".",20))
# print(s.find(".",20, 30))
# print(s.rfind("."))

# print(s.index("."))
# print(s.rindex("."))
# print(s.index(".",20, 30))

# Методы проверки начала и конца
print(s)
print(s.startswith("тео"))
print(s.startswith("Тео"))
print(s.endswith("."))
print(s.endswith(" "))

# Методы проверки строк
s = " \n\t"
print(s)
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.isspace())