#######################################################################################################################
# Circular Array
# (1) Palindrome
"""A method/function that takes in a circular array, 
its size and start index and finds whether the elements in the array form a palindrome or not.

Test Case-1: [20,10,0,0,0,10,20,30] (start =5, size=5)
Output: True

Test Case-2: [10,20,0,0,0,10,20,30] (start =5, size=5)
Output: False"""

def check_palindrome(circular_array, size, start):
    is_palindrome = True
    idx = start
    rev_idx = (start + size - 1) % len(circular_array)
    div = size // 2
    while idx < (div + start) % len(circular_array):
        if circular_array[idx] != circular_array[rev_idx]:
            is_palindrome = False
            break
        else:
            rev_idx = rev_idx - 1
            if rev_idx < 0:
                rev_idx = len(circular_array) - 1
            idx = (idx + 1) % len(circular_array)
    return is_palindrome

circular_array = [20, 10, 0, 0, 0, 10, 20, 30]
print(check_palindrome(circular_array, 5, 5))
circular_array = [10,20,0,0,0,10,20,30]
print(check_palindrome(circular_array, 5, 5))


#######################################################################################################################
# (2) Intersection
"""A method/function that takes two circular arrays, their sizes and start indexes and returns a linear array containing
 the common elements between the two circular arrays
 
Test Case-1: Cir_1: [40,50,0,0,0,10,20,30] (start_1 =5, size_1 =5)
             Cir_2: [10,20,5,0,0,0,0,0,5,40,15,25] (start_2=8, size_2 =7)
Output: [10,20,40]"""

def do_sort(arr):
    for idx in range(len(arr) - 1):
        min_indx = idx
        for j in range(idx + 1, len(arr)):
            if arr[j] < arr[min_indx]:
                min_indx = j
        swap(min_indx, idx, arr)
    return arr

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def intersection(cir_array_1, cir_array_2, size_1, size_2, start_1, start_2):
    common_ele = [0] * len(cir_array_1)
    common_idx = 0
    idx_1 = start_1
    common_count = 0
    for i in range(0, size_1):
        idx_2 = start_2
        for j in range(0, size_2):
            if cir_array_1[idx_1] == cir_array_2[idx_2]:
                common_ele[common_idx] = cir_array_1[idx_1]
                common_idx += 1
                common_count += 1
            idx_2 = (idx_2 + 1) % len(cir_array_2)
        idx_1 = (idx_1 + 1) % len(cir_array_1)

    final_lst = [0] * common_count
    for i in range(0, common_count):
        if common_ele[i] != 0:
            final_lst[i] = common_ele[i]
        else:
            break
    return do_sort(final_lst)

print(intersection([40, 50, 0, 0, 0, 10, 20, 30], [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25], 5, 7, 5, 8))
print(intersection([40,50,0,0,0,10,20,30], [40,50,0,0,0,10,20,30], 5, 5,5,5))


#######################################################################################################################
"""In the musical chair game, there will be 7 participants and all of them will be moving clockwise around a set of 7 
chairs organized in a circular manner. You will control the music using random numbers between 0-3.

If the generated random number is 1, you will stop the music and if the number of participants who are still in the game 
is n, the participants at position (n/2) will be eliminated. Each time a participant is eliminated, a chair will be 
removed and you have to print the player names who are still in the game.

At the end of the game,display the name of the winner."""

def random_num_generator():
    import random
    return random.randint(0, 3)

def musical_chair(participates):
    size = len(participates)
    while size != 1:
        num_generator = random_num_generator()
        if num_generator != 1:
            temp = participates[size - 1]
            i = size - 1
            while i >= 1:
                participates[i] = participates[i - 1]
                i = i - 1
            participates[0] = temp

        else:
            eliminate = size // 2
            participates[eliminate - 1] = 0
            i = eliminate
            while i < size:
                participates[i - 1] = participates[i]
                i = i + 1
            participates[size - 1] = 0
            size = size - 1
            print(participates)

    print(participates[0])

musical_chair(['A', 'B', 'C', 'D', 'E', "F"])
musical_chair(["rifa", "tasfiya", "Mango", "Nimo"])
#######################################################################################################################
