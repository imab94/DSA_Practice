from collections import OrderedDict
ordinary_dictionary = OrderedDict()
n = int(input())

for _ in range(n):
    name, price = input().rsplit(" ",1)
    price = int(price)

    if name in ordinary_dictionary:
        ordinary_dictionary[name] += price
    else:
        ordinary_dictionary[name] = price

for name, total in ordinary_dictionary.items():
    print(name,total)