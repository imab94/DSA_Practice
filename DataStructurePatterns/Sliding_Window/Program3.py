"""
Point to be remember - sliding window doesn't work on avg.
Average of each subarray(window) of windown size k.
Input:
arr= [1,2,3,4], k = 2
Output: [1.5,2.5,3.5]
Constrainst: 1<=n<=10^5
Hint: Use Sliding Window Fixed.
"""

# brute force solution
ls = list(map(int,input().split()))
k = 2
avg = []

for i in range(len(ls)-k+1):
    window_sum = 0
    for j in range(i,i+k):
        window_sum += ls[j]
    avg.append(window_sum/2)

print(avg)

# Optimal solution using sliding window
ls = list(map(int,input().split()))
k = 2
avg = []
window_sum = 0
for i in range(k):
    window_sum += ls[i]

avg.append(window_sum/k)

# slide
for right in range(k,len(ls)):
    window_sum += ls[right]
    window_sum -= ls[right-k]
    avg.append(window_sum / k)
print(avg)






