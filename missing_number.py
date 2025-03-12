"""
Problem Explanation:

You are given an array that contains n-1 distinct numbers. These numbers are chosen from the range 1 to n, where 
n is the total number of elements you expect. Since there is one missing number, the array contains every number 
from the range except one.

For example, if n = 6, the complete set of numbers would be: [1, 2, 3, 4, 5, 6]
If the array contains the numbers: [1, 2, 3, 5, 6]
Then the missing number is 4.

"""
def find_missing_number_sum(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

example:
arr = [1, 2, 3, 4, 5, 6, 8]
n = 8
print(find_missing_number_sum(arr, n))  
 Output: 7
