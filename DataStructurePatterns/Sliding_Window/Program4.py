"""
Sliding_Window.Program4
Task
Longest substring without repeating characters

Input:
s = "abcabcbb"

Output: 3
Constraints:
1<=n<=10^5
Hint: Use Sliding Window variable.

"""
# brute force solution
string = input()
max_len = 0
for i in range(len(string)):
    seen = set()
    current = 0
    for j in range(i,len(string)):
        if string[j] in seen:
            break
        else:
            seen.add(string[j])
            current += 1
    max_len = max(max_len, current)
print(max_len)


# Optimal solution using sliding window
string = input()
seen = set()
left = 0
max_len = 0

for right in range(len(string)):
    while string[right] in seen:
        seen.remove(string[left])
        left += 1
    seen.add(string[right])
    max_len = max(max_len, right-left+1)

print(max_len)


