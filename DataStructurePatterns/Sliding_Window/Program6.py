"""
Sliding_Window.Program6
Task
Smallest subarray with sum >=k (positive numbers only)

Input:
arr  = [2,1,5,2,3], target = 7
Outout:
2
Constraints:
1<=n<=10^5

Hint: use sliding window variable
"""
ls = list(map(int,input().split()))
min_len = float('inf')
left = 0
current_sum = 0
target = 7
for right in range(len(ls)):
     # add elements
    current_sum += ls[right]
    while current_sum >= target:
        # find min_len
        min_len = min(min_len, right-left+1)
        # shrink window
        current_sum -= ls[left]
        left += 1
print(min_len)


