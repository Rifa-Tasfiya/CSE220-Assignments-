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

    def isEmpty(self):
        if self.head == None:
            return "true"
        else:
            return "false"

    def clear(self):
        if self.head != None:
            self.head = None

    def size(self):
        count = 0
        n = self.head
        while (n is not None):
            count = count + 1
            n = n.next
        return count

    def atNode(self, index):
        if index < 0 and index >= self.size():
            return None
        x = self.head
        i = 0
        while (x is not None):
            if i == index:
                return x
            x = x.next
            i = i + 1

    def insert(self, newElement, index=None):
        if index == None:
            temp = self.head
            unique_check = True
            while temp != None:
                if temp.elem == newElement:
                    print(f"Key {newElement} already exists.")
                    unique_check = False
                    break
                temp = temp.next

            if unique_check:
                temp_1 = self.head
                new_node = Node(newElement, None)
                while temp_1.next != None:
                    temp_1 = temp_1.next
                temp_1.next = new_node

        else:
            if self.head != None:
                temp = self.head
                unique_check = True
                count_ele = 0
                while temp != None:
                    if temp.elem == newElement:
                        print(f"Key {newElement} already exists.")
                        unique_check = False
                    temp = temp.next
                    count_ele += 1

                if unique_check:
                    if index < 0 or index > count_ele:
                        raise Exception("Invalid Index")
                    new_node = Node(newElement, None)
                    if index == 0:
                        new_node.next = self.head
                        self.head = new_node
                    else:
                        temp_1 = self.head
                        for i in range(0, index - 1):
                            temp_1 = temp_1.next
                        pred = temp_1
                        new_node.next = pred.next
                        pred.next = new_node

    def remove(self, deleteKey):
        if self.head != None:
            temp = self.head
            idx = 0
            is_remove = False
            while temp != None:
                if temp.elem == deleteKey and idx == 0:
                    removed_node = self.head
                    self.head = self.head.next
                    is_remove = True
                elif temp.elem == deleteKey and idx != 0:
                    pred = self.atNode(idx - 1)
                    removed_node = pred.next
                    pred.next = removed_node.next
                    is_remove = True
                idx += 1
                temp = temp.next
            if is_remove == False:
                print(f"Key {deleteKey} does not exist")

    def evenList(self):
        first_time_even = False
        pos_1 = self.head
        pos_2 = pos_1  # Even position
        while pos_1 != None:
            if pos_1.elem % 2 == 0 and first_time_even == False:
                first_time_even = True
                pos_2 = pos_1
                self.head = pos_2

            elif pos_1.elem % 2 == 0:
                pos_2.next = pos_1
                pos_2 = pos_1

            pos_1 = pos_1.next
        pos_2.next = None
        return self

    def find(self, element):
        temp = self.head
        occurrence = False
        while temp != None:
            if temp.elem == element:
                occurrence = True
            temp = temp.next
        return occurrence

    def reverseList(self):
        new_head = None
        temp = self.head
        while temp != None:
            next_node = temp.next
            temp.next = new_head
            new_head = temp
            temp = next_node
        self.head = new_head

    def sort(self):
        tail = None
        copy_head = self.head
        while tail != copy_head.next:
            pos_1 = self.head
            while pos_1.next != tail:
                pos_2 = pos_1.next
                if pos_1.elem > pos_2.elem:
                    temp_val = pos_1.elem
                    pos_1.elem = pos_2.elem
                    pos_2.elem = temp_val
                pos_1 = pos_1.next
            tail = pos_1

    def sum(self):
        temp = self.head
        total = 0
        while temp != None:
            total += temp.elem
            temp = temp.next
        return total

    def rotateKTimes(self, k, direction):
        # Doing left rotation
        if direction == "left":
            for i in range(0, k):
                temp_node = self.head
                self.head = self.head.next
                temp_node.next = None
                pos = self.head
                while pos.next != None:
                    pos = pos.next

                pos.next = temp_node

        # Doing right rotation
        if direction == "right":
            for i in range(0, k):
                pos_1 = self.head
                pos_2 = pos_1
                while pos_1.next != None:
                    pos_2 = pos_1
                    pos_1 = pos_1.next
                last_node = pos_1
                pos_2.next = None
                last_node.next = self.head
                self.head = last_node


# ==========================Tester Code==========================#

# Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
a = [10, 20, 30, 40, 50, 60]
l1 = myList(a)
l1.showList()  # Should print: 10->20->30->40->50->60

# Task-2.3 -- isEmpty
print("\n//========Task 2.3 -- isEmpty========//")
isListEmpty = l1.isEmpty()
print(isListEmpty)  # Should print: false
b = []
l2 = myList(b)
isListEmpty = l2.isEmpty()
print(isListEmpty)  # Should print: true

# Task-2.4 -- Clear
print("\n//=======Task 2.4 -- Clear =======//")
print("Before clearing Linked List")
l1.showList()  # Should print: 10->20->30->40->50->60
l1.clear()
print("After clearing Linked List")
l1.showList()  # Should print: Empty List

# Task-2.5, 2.6 -- Insert
print("\n//=======Task 2.5, 2.6 -- Insert=======//")
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = myList(c)
l3.showList()  # Should print: 10->20->30->40->50->60->70->80->90
l3.insert(100)
l3.showList()  # Should print: 10->20->30->40->50->60->70->80->90->100
l3.insert(0, 0)
l3.showList()  # Should print: 0->10->20->30->40->50->60->70->80->90->100
l3.insert(110, 5)
l3.showList()  # Should print: 0->10->20->30->40->110->50->60->70->80->90->100
l3.insert(120, 12)
l3.showList()  # Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.insert(50)  # Should print: Key 50 already exists

# Task-2.7 -- Remove
print("\n//=======Task 2.7 -- Remove=======//")
l3.showList()  # Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(0)
l3.showList()  # Should print: 10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(110)
l3.showList()  # Should print: 10->20->30->40->50->60->70->80->90->100->120
l3.remove(120)
l3.showList()  # Should print: 10->20->30->40->50->60->70->80->90->100
l3.remove(120)  # Should print: Key 120 does not exist

# Task-3.1 -- EvenList
print("\n//=======Task 3.1 -- EvenList =======//")
d = [1, 2, 5, 3, 8]
l4 = myList(d)
l5 = l4.evenList()
l5.showList()  # Should print: 2->8

# Task-3.2 -- Find
print("\n//=======Task 3.2 -- Find =======//")
d = [1, 2, 5, 3, 8]
l4 = myList(d)
found = l4.find(5)
print(found)  # Should print: true
found = l4.find(4)
print(found)  # Should print: false

# Task-3.3 -- Reverse List
print("\n//=======Task 3.3 -- Reverse =======//")
print("Before Reverse: ", end='')
l4.showList()  # Should print: 1->2->5->3->8
l4.reverseList()
print("After Reverse: ", end='')
l4.showList()  # Should print: 8->3->5->2->1

# Task-3.4 -- Sort
print("\n//=======Task 3.4 -- Sort =======//")
print("Before Sort: ", end='')
l4.showList()  # Should print: 8->3->5->2->1
l4.sort()
print("After Sort: ", end='')
l4.showList()  # Should print: 1->2->3->5->8

# Task-3.5 -- Sum of Elements
print("\n//=======Task 3.5 -- Sum of Elements =======//")
l4.showList()  # Should print: 1->2->3->5->8
total = l4.sum()
print("Sum of Elements:", total)

# Task-3.6-- Rotate
print("\n//=======Task 3.6 -- Rotate =======//")
l4.showList()  # Should print: 1->2->3->5->8
l4.rotateKTimes(2, "left")
l4.showList()  # Should print: 3->5->8->1->2
l4.rotateKTimes(2, "right")
l4.showList()  # Should print: 1->2->3->5->8
