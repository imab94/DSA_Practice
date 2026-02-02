"""
Minimum Sum of subarray of size k
Input:
arr = [3,2,1,5,6] for window size k = 2
Output: 3
Constraints: 1<=n<=10^5
"""
ls = list(map(int,input().split()))
k = 2
window_min = 0
for i in range(k):
    window_min += ls[i]
min_sum = window_min
for right in range(k,len(ls)):
    window_min += ls[right]
    window_min -= ls[right-k]
    min_sum = min(min_sum,window_min)
print(min_sum)
