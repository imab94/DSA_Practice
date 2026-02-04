"""
Sliding_Window.Program8

Task
Find first negative number in each window.

Input:
arr = [12,-1,-7,8,-15,30], window size k = 3
Outout:
[-1,-1,-7,-15]
Constraints:
1<=n<=10^5
 12 -1 -7 8 -15 30

Hint: use sliding window Fixed
"""

array = list(map(int,input().split()))
negatives = []
result = []
k = 3
for i in range(k):
    if array[i] < 0:
        negatives.append(i)

# add only one first negaitve
if negatives:
    result.append(array[negatives[0]])
else:
    result.append(0)

# slide window
for right in range(k,len(array)):

    if negatives and negatives[0] <= right-k:
        negatives.pop(0)

    if array[right]<0:
        negatives.append(right)

    # append result
    if negatives:
        result.append(array[negatives[0]])
    else:
        result.append(0)

print(result)





