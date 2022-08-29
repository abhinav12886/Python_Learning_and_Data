# maximum sum of subarray of contiguous element of size k

def maxSumSubArray(arr, k):
    left = 0
    right = k-1
    window_sum = 0
    for i in range(k):
        window_sum = window_sum + arr[i]

    for right in range(k,len(arr)):
        window_sum = max(window_sum, window_sum + arr[right] - arr[left])
        left += 1

    return window_sum


array = [2, 7, 3, 5, 8, 1]
k = 3
print(maxSumSubArray(array, k))

#-------------------using one loop--------------

# def maxSubArraySum(arr, k):
#     start = 0
#     maxSum = 0
#     window_sum = 0
#     for end in range(len(arr)):
#         window_sum = window_sum + arr[end]
#         if(end>=k-1):
#             maxSum = max(window_sum, maxSum)
#             window_sum = window_sum - arr[start]
#             start+=1
#
#     return maxSum
#
# array = [2, 7, 3, 5, 8, 1]
# k = 3
# print(maxSubArraySum(array, k))