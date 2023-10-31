# Radix Sort Implementation with User Interaction and Error Checks

# Program Information
# - Author: Joe defendre
# - This program sorts an array of up to 4-digit integers using Radix Sort.
# - The user can choose between Counting Sort and Bucket Sort for the digit-wise sorting.

# Counting Sort function for Radix Sort
def counting_sort_for_radix(arr, digit_getter):
    # Initialize variables
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits range from 0 to 9

    # Count occurrences of each digit
    for i in range(n):
        index = digit_getter(arr[i])
        count[index] += 1

    # Update count[i] to position of next occurrence
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = digit_getter(arr[i])
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back
    for i in range(n):
        arr[i] = output[i]

# Bucket Sort function for Radix Sort
def bucket_sort_for_radix(arr, digit_getter):
    # Initialize buckets
    buckets = [[] for _ in range(10)]

    # Place numbers in buckets based on digit
    for num in arr:
        index = digit_getter(num)
        buckets[index].append(num)

    # Retrieve numbers from buckets back to array
    i = 0
    for bucket in buckets:
        for num in bucket:
            arr[i] = num
            i += 1

# Enhanced Radix Sort function
def enhanced_radix_sort(arr, technique='counting'):
    # Choose sorting function based on technique
    sort_function = counting_sort_for_radix if technique == 'counting' else bucket_sort_for_radix

    # Get maximum number to know the number of digits
    max_num = max(arr)
    exp = 1  # Initialize counting exponent

    # Sort by each digit
    while max_num // exp > 0:
        sort_function(arr, lambda x: (x // exp) % 10)
        exp *= 10

# Welcome message
print("Welcome to the Radix Sort program!")
print("This program will sort an array of integers. You can choose the sorting technique.")

# Array creation
try:
    size = int(input("Enter the size of the array: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(size)]
except ValueError:
    print("Please enter valid integers.")

# Technique selection
technique = input("Choose a technique: counting or bucket: ").lower()
if technique not in ['counting', 'bucket']:
    print("Invalid choice. Using counting sort as default.")
    technique = 'counting'

# Display original array
print("Original array:", arr)

# Perform sorting
enhanced_radix_sort(arr, technique)

# Display sorted array
print("Sorted array:", arr)
