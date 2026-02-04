"""
Sliding_Window.Program7

Task
maximum number of vowels in substring of size k

Input:
s  = "abciiidef", k = 3
Outout:
3
Constraints:
1<=n<=10^5

Hint: use sliding window Fixed
"""

s = input()
left = 0
k = 3
window_vowel_count = 0
vowels = set("aeiou")

# step 1 -- first window
for i in range(k):
    if s[i] in vowels:
        window_vowel_count += 1

max_count = window_vowel_count

# step 2 -- slide window
for right in range(k,len(s)):
    if s[right] in vowels:
        window_vowel_count += 1

    if s[right-k] in vowels:
        window_vowel_count -= 1

    # update answer
    max_count = max(max_count, window_vowel_count)

print(max_count)









