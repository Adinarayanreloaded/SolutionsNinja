def search(nums, target):
    left, right = 0, len(nums) - 1  # Initialize the pointers
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        
        if nums[mid] == target:
            return mid  # Target found, return the index
        elif nums[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
    
    return -1  # Target not found in the array

if __name__ == "__main__":
    # Reading input
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    
    # Performing the search
    result = search(nums, target)
    
    # Printing the result
    print(result)
