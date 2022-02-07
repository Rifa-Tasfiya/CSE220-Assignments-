""" A program that will determine whether the open brackets (the square brackets, curly braces and the parentheses) are
closed in the correct order.

Input-1: 1+2*(3/4)
Output-1: 1+2*(3/4)

Input-2: 1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14
Output-2: This expression is NOT correct.
          Error at character # 10. ‘{‘- not closed.

Input-3: 1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14
Output-3: This expression is correct.

Input-4: 1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14
Output-4: This expression is NOT correct.
          Error at character # 4. ‘]‘- not opened."""

########################################################################################################################
# Using an array based stack


class arrStack:
    stack_arr = []
    pointer = -1

    def push(self, elem, idx):
        temp_lst = [elem, idx]
        self.stack_arr.append(temp_lst)
        self.pointer += 1

    def peek(self):
        return self.stack_arr[self.pointer]

    def pop(self):
        val = self.stack_arr[self.pointer]
        temp_stack = []
        for i in range(0, self.pointer):
            temp_stack.append(self.stack_arr[i])
        self.stack_arr = temp_stack
        self.pointer -= 1
        return val

    def is_empty(self):
        if len(self.stack_arr) == 0:
            return True
        else:
            return False


def valid_bracket_pairs(open, close):
    if open == "(" and close == ")":
        return True
    elif open == "{" and close == "}":
        return True
    elif open == "[" and close == "]":
        return True
    else:
        return False


def check_valid_expression(expression):
    opening_bracket = ["(", "{", "["]
    closing_bracket = [")", "}", "]"]
    index = 0
    for i in expression:
        if i in opening_bracket:
            obj.push(i, index)
        elif i in closing_bracket:
            if obj.is_empty():
                return f"This expression is NOT correct.\nError at character #{index + 1}.‘{expression[index]}‘- not opened."
            else:
                temp_lst = obj.peek()
                if valid_bracket_pairs(temp_lst[0], i):
                    obj.pop()
                else:
                    return f"This expression is NOT correct.\nError at character #{temp_lst[1] + 1}.‘{temp_lst[0]}‘- not closed."


        index += 1

    if obj.is_empty():
        return "This expression is correct."

    else:
        temp_lst = obj.peek()
        return f"This expression is NOT correct.\nError at character # {temp_lst[1] + 1}. ‘{temp_lst[0]}‘- not closed."


exp_lst = ["1+2*(3/4)", "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14", "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14",
           "1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"]
counter = 1
for k in range(len(exp_lst)):
    obj = arrStack()
    obj.stack_arr = []
    print(f"Output: {counter}")
    print(exp_lst[k])
    print(check_valid_expression(exp_lst[k]))
    counter += 1
    print("==========================================================")


#######################################################################################################################

#  =====================================================================================================================
# Stack implementation through linked list

class Node:
    def __init__(self, elem, idx):
        self.lst = [elem, idx]
        self.next = None


class Stack:
    head = None

    def push(self, elem, idx):
        if self.head == None:
            self.head = Node(elem, idx)
        else:
            n = Node(elem, idx)
            n.next = self.head
            self.head = n

    def peek(self):
        return self.head.lst

    def pop(self):
        if self.head != None:
            self.head = self.head.next

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False


def valid_bracket_pairs(open, close):
    if open == "(" and close == ")":
        return True
    elif open == "{" and close == "}":
        return True
    elif open == "[" and close == "]":
        return True
    else:
        return False


def check_valid_expression(expression):
    opening_bracket = ["(", "{", "["]
    closing_bracket = [")", "}", "]"]
    index = 0
    for i in expression:
        if i in opening_bracket:
            obj.push(i, index)
        elif i in closing_bracket:
            if obj.is_empty():
                return f"This expression is NOT correct.\nError at character #{index + 1}.‘{expression[index]}‘- not opened."

            else:
                temp_lst = obj.peek()
                if valid_bracket_pairs(temp_lst[0], i):
                    obj.pop()
                else:
                    temp_lst = obj.peek()
                    return f"This expression is NOT correct.\nError at character #{temp_lst[1] + 1}.‘{temp_lst[0]}‘- not closed."
        index += 1

    if obj.is_empty():
        return "This expression is correct"

    else:
        temp_lst = obj.peek()
        return f"This expression is NOT correct.\nError at character # {temp_lst[1] + 1}. ‘{temp_lst[0]}‘- not closed."


exp_lst = ["1+2*(3/4)", "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14", "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14",
           "1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"]
counter = 1
for k in range(len(exp_lst)):
    obj = Stack()
    obj.stack_arr = []
    print(f"Output: {counter}")
    print(exp_lst[k])
    print(check_valid_expression(exp_lst[k]))
    counter += 1
    print("==========================================================")

#######################################################################################################################
