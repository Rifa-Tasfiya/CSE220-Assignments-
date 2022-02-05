#######################################################################################################################
# (1) Shift Left k Cells
"""A method that shifts all the elements of the source array to the left by 'k' positions.

Test case-1: [10,20,30,40,50,60], k=3
Output: [ 40, 50, 60, 0, 0, 0 ]"""

def shiftLeft(source, k):
    i = 0
    while i + k < len(source):
        source[i] = source[i + k]
        i = i + 1

    for j in range(i, len(source)):
        source[j] = 0
    return source

source = [10, 20, 30, 40, 50, 60, 70, 80]
shift_array = shiftLeft(source, 5)
print(shift_array)

#######################################################################################################################
# (2) Rotate Left k cells
"""A method that rotates all the elements of the source array to the left by 'k' positions.

Test Case-1: [10,20,30,40,50,60], k=3
Output: [ 40, 50, 60, 10, 20, 30]"""

def rotateLeft(source, k):
    size = len(source)
    for i in range(0, k):
        temp = source[0]
        for j in range(1, size):
            source[j - 1] = source[j]
        source[size - 1] = temp
    print(source)

source = [10, 20, 30, 40, 50, 60]
rotateLeft(source, 3)

#######################################################################################################################
# (3)Remove an element from an array
"""A method/function named remove(source, size, idx) that removes the element in index idx of the source array.

Test Case-1: [10,20,30,40,50,0,0], size = 5, idx=2
Output: [ 10,20,40,50,0,0,0]"""

def remove(source, size, idx):
    if idx < 0 or idx > size:
        print("Wrong index. Please input the correct index!")
        return
    else:
        i = idx + 1
        while i < size:
            source[i - 1] = source[i]
            i = i + 1
        source[size - 1] = 0
        return source

source = [10, 20, 30, 40, 50, 0, 0]
print(remove(source, 5, 2))

# (4) Remove all occurrences of a particular element from an array
"""A method/function named removeAll( source, size, element) that removes all the occurrences of the given element in 
the source array. 
Test Case-1: [10,2,30,2,50,2,2,0,0], size = 7, element=2
Output: [10,30,50,0,0,0,0,0,0]"""

def removeAll(source, size, element):
    idx = 0
    while idx < size:
        if source[idx] == element:
            source[idx] = 0
        idx = idx + 1

    idx = 0
    i = 0
    result_array = [0] * len(source)
    while i < size:
        if source[i] != 0:
            result_array[idx] = source[i]
            idx = idx + 1
        i = i + 1
    return result_array

source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
print(removeAll(source, 7, 2))

#######################################################################################################################
# (5) Splitting an Array

"""The elements of an array A containing positive integers, denote the weights in kilograms. And we have a beam balance.
We want to put the weights on both pans of the balance in such a way that for some index 0 < i < A.length - 1, all 
values starting from A[0], A[1], upto A[ i - 1], should be on the left pan. And all values starting from A[ i ] upto 
A[ A.length - 1] should be on the right pan and the left and right pan should be balanced. 

If such an i exists, return true. Else, return false.

Test Case-1: [1, 1, 1, 2, 1]
Output: true

Test Case-2: [2, 1, 1, 2, 1]
Ouput: false

Test Case-3: [10, 3, 1, 2, 10]
Output: true"""

def do_split(source):
    total_1 = 0
    total_2 = 0
    size = len(source)
    split_checker = False
    for i in range(0, size-1):
        total_1 += source[i]
        for j in range(i+1, size):
            total_2 += source[j]
        if total_1 == total_2:
            split_checker = True
        total_2 = 0
    return split_checker

source = [1, 1, 1, 2, 1]
print(do_split(source))

#######################################################################################################################
# (6) Array series
"""A method that takes an integer value n as a parameter. Inside the method, you should create an array of length n 
squared (n*n) and fill the array with the certain pattern. Return the array at the end and print it.

Test Case-1: n=1
Output: [0,1, 2,1]

Test Case-2: n=3
Output: [0, 0, 1, 0, 2, 1, 3, 2, 1]

Test Case-3: n=4
Output: {0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1}"""

def do_create_array(n):
    a_array = [0] * n ** 2
    counter = 1
    idx = n - 1
    for i in range(0, n):
        temp = idx
        value = 1
        for j in range(0, counter):
            a_array[temp] = value
            value = value + 1
            temp = temp - 1
        idx = idx + n
        counter = counter + 1

    return a_array

n = int(input("Enter an integer: "))
print(do_create_array(n))

#######################################################################################################################
# (7) Max Bunch Count
"""A method that returns the number of elements in the largest bunch found in the given array.

Test Case-1: [1, 2, 2, 3, 4, 4, 4]
Output: 4

Test Case-2: [1,1,2, 2, 1, 1,1,1]
Output: 4

Test Case-3: [1,2,3,4]
Output: There is no max bunch."""

def count_max_bunch(source):
    temp_val = source[0]
    max_bunch = 0
    count_bunch = 1
    idx = 1
    size = len(source)
    while idx < size:
        if source[idx] == temp_val:
            count_bunch += 1
        else:
            if max_bunch < count_bunch:
                max_bunch = count_bunch
            temp_val = source[idx]
            count_bunch = 1
        idx += 1

    if max_bunch < count_bunch:
        max_bunch = count_bunch

    if max_bunch == 1:
        return "There is no max bunch."
    else:
        return max_bunch

source = [1, 1, 2, 2, 1, 1, 1, 1]
print(count_max_bunch(source))

#######################################################################################################################
# (8) Repetition
"""A method that takes in an array as a parameter and counts the repetition of each element. That is, if an element has 
appeared in the array more than once, then its ‘repetition’ is its number of occurrences. The method returns true if 
there are at least two elements with the same number of ‘repetition’. Otherwise, return false.

Test Case-1: [4,5,6,6,4,3,6,4]
Output: True

Test Case-2: [3,4,6,3,4,7,4,6,8,6,6]
Output: False"""

def do_sort(arr):
    for idx in range(len(arr) - 1):
        min_idx = idx
        for j in range(idx + 1, len(arr)):
            if arr[min_idx] < arr[j]:
                min_idx = j

        swap(min_idx, idx, arr)
    return arr

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def count_repetition(source):
    size = len(source)
    do_count_array = [0] * size
    for i in range(0, size - 1):
        count = 1
        if source[i] != 0:
            for j in range(i + 1, size):
                if source[i] == source[j]:
                    count += 1
                    source[j] = 0
            if count > 1:
                do_count_array[i] = count
    sort_array = do_sort(do_count_array)

    is_sem_repetition = False
    for i in range(1, len(sort_array)):
        if sort_array[i - 1] == sort_array[i] and sort_array[i] != 0:
            is_sem_repetition = True
            break
    return is_sem_repetition

source = [4, 5, 6, 6, 4, 3, 6, 4]
print(count_repetition(source))

