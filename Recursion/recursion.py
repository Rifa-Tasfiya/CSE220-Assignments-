########################################################################################################################

# Task- 1(a)
"""Implement a recursive algorithm to find factorial of n.

Sample Input 1: 9
Sample Output: 362880"""


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(9))

########################################################################################################################

# Task - 1(b)
"""Implement a recursive algorithm to find the n-th Fibonacci number.

Sample Input: 10
Sample Output: 55"""


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))

########################################################################################################################

# Task - 1(c)
# Traversing through recursively
def do_print(arr, i=0):
    if i == len(arr):
        return
    print(arr[i])
    return do_print(arr, i=i + 1)


arr = [1, 2, 3, 4, 5]
do_print(arr)

########################################################################################################################

# Task - 1(d)
"""Compute recursively the value of base to the n power. (Base and n are both 1 or more than)
Sample input & output
powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27"""
def powerN(base, n):
    if n == 0:
        return 1
    x = powerN(base, n//2)
    if n % 2 == 0:
        return x * x
    else:
        return x * x * base


print(powerN(3, 1))
print(powerN(3, 2))
print(powerN(3, 3))

########################################################################################################################

# Task - 2(a)
# Covert a decimal number (n) into binary.
def decimal_to_binary(n):
    if n > 1:
        return str(decimal_to_binary(n // 2)) + str(n % 2)
    return n % 2


print(decimal_to_binary(0))

########################################################################################################################

# Task 2(b)
"""A function that implement a recursive algorithm to add all the elements of a singly linked linear list.
Sample input: [1, 2, 3, 4, 5]
Sample output: 15"""
class singlyNode:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class myLinkedList:

    def __init__(self, lst):
        self.lst = lst
        self.head = None
        tail = None
        for i in self.lst:
            n = singlyNode(i)
            if self.head == None:
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n


def find_sum(head):
    if head.next is None:
        return head.elem
    return head.elem + find_sum(head.next)


lst = [1, 2, 3, 4, 5]
ll = myLinkedList(lst)
print(find_sum(ll.head))

#######################################################################################################################

# Task 2(c)
# A function that will print all the elements of a singly linked linear list in reversed order.
# A recursive algorithm
# Sample input: [1,2,3,4]
# Sample output: 4 3 2 1
class singlyNode:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class myLinkedList:
    def __init__(self, a):
        self.a = a
        self.head = None
        tail = None
        for i in self.a:
            n = singlyNode(i)
            if self.head == None:
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n


def do_reverse(head):
    if head is None or head.next is None:
        print(head.elem)
        return head

    new_head = do_reverse(head.next)
    print(head.elem)
    head.next.next = head
    head.next = None
    return new_head


lst = [1, 2, 3, 4]
l1 = myLinkedList(lst)
do_reverse(l1.head)

########################################################################################################################

# Task 3
"""A function that find the number of cards required to build a ‘house of cards’ of specific height
Height will be always non negative integer number
The top level of the building requires 8 cards. The rest of the level requires 5 cards.
Sample input & output
hocBuilder(0) → Can not build a house
hocBuilder(1) → 8
hocBuilder(2) → 13
hocBuilder(3) → 18"""


def hocBuilder(height):
    if height == 0:
        return "Can not build a house"
    elif height == 1:
        return 8
    else:
        return 5 + hocBuilder(height - 1)


print(hocBuilder(0))
print(hocBuilder(1))
print(hocBuilder(2))
print(hocBuilder(3))

########################################################################################################################

# Task 4(a)
# Print pattern
def print_pattern(n, i=1, j=1):
    if n == 0:
        return
    if i > j:  # just printing the row until the 1st elem of the row occur
        print(j, end=" ")
        print_pattern(n, i=i, j=j + 1)
    if i == j:    # Print the last elem of the row & change the row (i.e: 1st row theke 2nd row te jay)
        print(j)
        print_pattern(n=n - 1, i=i + 1, j=1)


print_pattern(4)

########################################################################################################################

# Task 4(b)
# Print pattern
def space(s):  # Detect the space
    if s == 0:
        return
    print(" ", end=" ")
    space(s - 1)


def row_printer(n, i=1):  # Print the row
    if n == 0:          # "n" initialize the iteration
        return          # i print the row elem
    else:
        print(i, end=" ")
        row_printer(n - 1, i=i + 1)


def pattern_print(n):
    wrap(n, 1, 1, n)


def wrap(num, j, i, n):
    if num == 0:
        return
    space(n - i)
    row_printer(j)
    print()  # space new row start
    wrap(num=num - 1, i=i + 1, j=j + 1, n=n)


pattern_print(3)

########################################################################################################################

# Task 5
"""A function that will print the profit of a company "X"

=============================================== Conditions ==============================================================
If investment <= 25000, print 0.
If 25000 < investment <= 100000, then the (investment-setupPrice) will increment by 4.5%.
If investment > 100000, then the (investment-100000) will increment by 8%. The rest (100000-setupPrice) will increment by 4.5%.

Sample Input 1: 25000
Sample Output 1: 0

Sample Input 2: 100000
Sample Output 2: 3375.0

SampleInput 3: 250000
Sample Output 3: 15375.0

Sample Input 4: 350000
Sample Output 4: 23375.0"""


class FinalQ:
    def print(self, array, idx):
        if (idx < len(array)):
            profit = self.calcProfit(array[idx])
            # TO DO
            print(f"Investment: {array[idx]}; Profit: {profit}")
            self.print(array, idx=idx + 1)

    def calcProfit(self, investment):
        # TO DO
        if investment <= 25000:
            return 0
        elif investment > 100000:
            if investment < 101000:
                return 8 + self.calcProfit(investment - 100)
            else:
                return 80 + self.calcProfit(investment - 1000)
        else:
            if investment < 26000:
                return 4.5 + self.calcProfit(investment - 100)
            else:
                return 45 + self.calcProfit(investment - 1000)


# Tester
array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.print(array, 0)

########################################################################################################################
