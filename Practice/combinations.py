from itertools import combinations

string, k = map(str, input().split())
c = list([item for item in string])
combs = list(combinations(string,int(k)))
combs = combs.extend(c)
print(combs)