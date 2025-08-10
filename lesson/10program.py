def revstring(string):
    """Reverse the string Text...
    
    Args:
        string (str): The string to reverse."""
    return string[::-1]


def vcount(string):
    """Count the number of vowels in a string.
    
    Args:
        string (str): The string to count vowels."""
    vowels = 'aeiou'
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count


def p_numbers(n):
    """check prime numbers.
    Args:
        n (int): The number to check."""
    
    if n % 1 == 0 and n % n == 0:
        return True
    return False


def remove_duplicates(lst):
    """Remove duplicates from a list.
    
    Args:
        lst (list): The list to remove duplicates from that."""
    
    # temp = lst
    # for i in lst:
    #     for j in lst:
    #         if i == j:
    #             temp.remove(i)

    temp = lst
    
    for i in range(0, len(lst)-1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                temp.remove(lst[j])
    return temp


def matrices():
    pass


def most_frequent(lst):
    frequency = {}
    max_count = 0
    most_common = None

    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

        if frequency[item] > max_count:
            max_count = frequency[item]
            most_common = item
    return most_common


def bubble_sort(arr):
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return arr


def kadan_algo():
    pass


def pascal_triangle(n):
    """Generate Pascal's Triangle up to n rows.
    
    Args:
        n (int): The number of rows in Pascal's Triangle."""
    for i in range(n):
        for j in range(n - i + 1):
            pass


my_list = [3, 7, 3, 2, 9, 3, 7, 7, 7, 2]
print(pascal_triangle(5))


