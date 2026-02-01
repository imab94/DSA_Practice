from itertools import permutations

string, k = map(str, input().split())

permutations = sorted(list(permutations(string,int(k))))

for i in permutations:
    print("".join(i))