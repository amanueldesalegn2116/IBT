"""
Day 08 - Recursion, Searching, Sorting & LeetCode Challenges
"""

def factorial(n: int) -> int:
    """Recursive Factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """Recursive Fibonacci."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def binary_search(arr: list, target) -> int:
    """Iterative Binary Search on sorted list. Returns index or -1."""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def quicksort(arr: list) -> list:
    """QuickSort Implementation."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def search_rotated_array(nums: list, target: int) -> int:
    """Challenge 20: Search in Rotated Sorted Array in O(log n)."""
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        # Left side is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right side is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == "__main__":
    print("Factorial 5:", factorial(5))
    print("Fibonacci 7:", fibonacci(7))

    data = [12, 3, 5, 7, 1, 9, 2]
    sorted_data = quicksort(data)
    print("QuickSorted:", sorted_data)
    print("Binary Search 7 in sorted:", binary_search(sorted_data, 7))

    rotated = [4, 5, 6, 7, 0, 1, 2]
    print("Search 0 in rotated array:", search_rotated_array(rotated, 0))
