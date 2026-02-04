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


