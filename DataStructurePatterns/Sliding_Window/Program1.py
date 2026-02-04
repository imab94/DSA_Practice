# Problem 1
"""
Maximum sum of subarray of size k
Input:
arr = [1,2,3,4,5,6] for k = 3
Output: 15 (4+5+6)
Constraints: 1<=n<=10^5
Hint: Use Sliding Window Fixed.
"""

ls = list(map(int,input().split()))
k = 3
window_sum = sum(ls[:k])
max_sum = window_sum
for right in range(k,len(ls)):
    window_sum += ls[right]
    window_sum -= ls[right-k]
    max_sum = max(max_sum, window_sum)

print(max_sum)

