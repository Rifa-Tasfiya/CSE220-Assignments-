#######################################################################################################################
#Task-1
"""Sort an array RECURSIVELY using selection sort algorithm."""


def find_minidx(arr, i):  # find the minimum value's index
    if i == len(arr) - 1:
        return i   # last elem indx
    minpos = find_minidx(arr, i=i + 1)
    if arr[minpos] > arr[i]:
        return i
    return minpos


def recursive_selection_sort(arr, step=0):
    if step == len(arr):
        return
    minidx = find_minidx(arr, step)
    if step != minidx:  # Swapping the elem
        temp = arr[minidx]
        arr[minidx] = arr[step]
        arr[step] = temp
    recursive_selection_sort(arr, step=step + 1)


arr = [3, 2, 1]
print("Before sorting the array: ")
print(arr)
recursive_selection_sort(arr)
print("After sorting the array: ")
print(arr)

########################################################################################################################

# Task-2
"""Sort an array RECURSIVELY using insertion sort algorithm."""


def sorted_part(arr, current_elem, j):  # Doing the shifting
    if j >= 0:
        if arr[j] > current_elem:
            arr[j + 1] = arr[j]
            sorted_part(arr, current_elem, j - 1)
            return
    arr[j + 1] = current_elem


def insertion_sort(arr, i=0):
    if i == len(arr):
        return
    current_elem = arr[i]
    sorted_part(arr, current_elem, i - 1)
    insertion_sort(arr, i + 1)


arr = [7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
print("Before sorting the array: ")
print(arr)
print("After sorting the array: ")
insertion_sort(arr)
print(arr)
########################################################################################################################

# Task - 3
"""Sort a singly linked sequential list using bubble sort algorithm."""


class Node:
    def __init__(self, e, n):
        self.elem = e
        self.next = n


class myList:

    def __init__(self, a):
        self.a = a
        self.head = None
        tail = None
        for i in self.a:
            n = Node(i, None)
            if self.head == None:
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n

    def showList(self):
        temp = self.head
        if self.head == None:
            print("Empty List")
        else:
            while temp != None:
                if temp.next != None:
                    print(temp.elem, end="->")
                else:
                    print(temp.elem)
                temp = temp.next

    def bubble_sort(self):
        tail = None
        copy_head = self.head
        while tail != copy_head.next:
            pos_1 = self.head
            while pos_1.next != tail:
                pos_2 = pos_1.next
                if pos_1.elem > pos_2.elem:  # 1st elem and 2nd elem comparing
                    temp_val = pos_1.elem
                    pos_1.elem = pos_2.elem
                    pos_2.elem = temp_val
                pos_1 = pos_1.next
            tail = pos_1


a = [3, 2, 1]
l = myList(a)
l.showList()
l.bubble_sort()
l.showList()

########################################################################################################################

# Task - 4
"""Sort a singly linked sequential list using selection sort algorithm."""


class Node:
    def __init__(self, e, n):
        self.elem = e
        self.next = n


class myList:

    def __init__(self, a):
        self.a = a
        self.head = None
        tail = None
        for i in self.a:
            n = Node(i, None)
            if self.head == None:
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n

    def showList(self):
        temp = self.head
        if self.head == None:
            print("Empty List")
        else:
            while temp != None:
                if temp.next != None:
                    print(temp.elem, end=", ")
                else:
                    print(temp.elem)
                temp = temp.next

    def selection_sort(self):
        pos_1 = self.head
        pos_2 = self.head.next
        while pos_1.next != None:
            minpos = pos_1
            while pos_2 != None:
                if minpos.elem > pos_2.elem:
                    minpos = pos_2
                pos_2 = pos_2.next
            temp_elem = pos_1.elem
            pos_1.elem = minpos.elem
            minpos.elem = temp_elem
            pos_1 = pos_1.next
            pos_2 = pos_1.next


a = [66, 99, -1, 0, -5]
l = myList(a)
print("Before sorting the singly linked sequential list: ")
l.showList()
l.selection_sort()
print("After sorting the singly linked sequential list: ")
l.showList()

########################################################################################################################

# Task - 5
"""Sort a DOUBLY linked sequential list using insertion sort algorithm."""


class Node:
    def __init__(self, elem, next, prev):
        self.elem = elem
        self.next = next
        self.prev = prev


class DoublyList:
    def __init__(self, a):
        self.head = None
        pos = self.head
        for i in a:
            new_node = Node(i, None, None)
            if self.head == None:
                self.head = new_node
            else:
                pos.next = new_node
                new_node.prev = pos
            pos = new_node

    def showList(self):
        pos = self.head
        if self.head == None:
            print("Empty List")
        else:
            while pos != None:
                if pos.next != None:
                    print(pos.elem, end="->")

                else:
                    print(pos.elem)
                pos = pos.next

    # cur_pos.prev helps to iterate backward
    # In case of j = -1 the loop will not run
    # cur_elem store the current element so that it can store the elem in its respective slot
    def insertion_sort(self):
        i = 0
        pos = self.head
        while pos != None:
            cur_elem = pos.elem
            cur_pos = pos
            j = i - 1
            while cur_pos.prev != None and cur_pos.prev.elem > cur_elem and j >= 0:
                cur_pos.elem = cur_pos.prev.elem
                cur_pos = cur_pos.prev
                j = j - 1
            i += 1
            cur_pos.elem = cur_elem
            pos = pos.next


a = [4, 3, 2, 1]
l = DoublyList(a)
print("Before sorting the list: ")
l.showList()
print("After sorting the list: ")
l.insertion_sort()
l.showList()

########################################################################################################################

# Task-6
"""Implement binary search algorithm RECURSIVELY."""
find_value = False


def binary_searching(arr, lower, upper, value):
    if lower > upper:
        return
    else:
        middle_val = (lower + upper) // 2
        if arr[middle_val] == value:
            globals()["find_value"] = True
            return middle_val
        elif arr[middle_val] > value:
            return binary_searching(arr, lower, middle_val-1, value)
        else:
            return binary_searching(arr, middle_val+1, upper, value)


arr = [4, 7, 8, 12, 45, 99]
pos = binary_searching(arr, 0, len(arr)-1, 1222)

if find_value:
    print(f"Found at position No. {pos+1} ")
else:
    print("The element is not found.")

########################################################################################################################

# Task-7
"""Implement a recursive algorithm to find the n-th Fibonacci number using memoization."""
cache = {}


def fibonacci(n):
    if n in cache:
        return cache[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n_th_term = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = n_th_term
        return n_th_term


print(fibonacci(100))

########################################################################################################################
