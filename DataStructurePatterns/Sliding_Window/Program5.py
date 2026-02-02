"""
Sliding_Window.Program5
Task
Longest Substring with atmost K distinct characters

Input:
s = "eceba", k = 2

Output:
3

Constraints:
1<=n<=10^5
"""
string = input()
max_len = 0
k = 2
left = 0
freq =  {}
for right in range(len(string)):
    freq[string[right]] = freq.get(string[right],0) + 1

    # shrink if distinct > k
    while len(freq) > k:
        freq[string[left]] -= 1

        if freq[string[left]] == 0:
            del freq[string[left]]
        left += 1

    # update answer
    max_len = max(max_len,right-left+1)
print(max_len)