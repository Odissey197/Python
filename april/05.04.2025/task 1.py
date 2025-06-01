# lst = [0.2, 0.54, 0.76, 0.8, 0.69]
# lst = list(map(lambda number: int(number*100), lst))
# print(lst)

ls = ['30%', '76%', '122%', '5%', '150%']
ls = list(map(lambda x: int(x[:-1]) / 100,ls))
# ls = list(map(lambda x: int(x.rstrip('%')) / 100,ls))
print(ls)