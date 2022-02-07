class Node:
    def __init__(self, elem, next, prev):
        self.elem = elem
        self.next = next
        self.prev = prev


class DoublyList:
    def __init__(self, a):  # a is an array
        self.head = Node(None, None, None)  # Dummy Node
        self.head.prev = self.head
        self.head.next = self.head
        pos = self.head
        for i in a:
            new_node = Node(i, None, None)
            if self.head == self.head.next:
                self.head.next = new_node
                new_node.prev = self.head

            else:
                pos.next = new_node
                new_node.prev = pos
            pos = new_node
        pos.next = self.head
        self.head.prev = pos

    def showList(self):
        pos = self.head.next  # Dummy node = head
        if self.head is self.head.next:
            print("Empty List")
        else:
            while pos != self.head:
                if pos.next != self.head:
                    print(pos.elem, end="->")

                else:
                    print(pos.elem)
                pos = pos.next

    def count(self):
        count = 0
        point = self.head.next
        while point != self.head:
            count += 1
            point = point.next
        return count

    def insert(self, newElement, index=None):
        is_unique = True
        pos = self.head.next
        while pos != self.head:
            if pos.elem == newElement:
                is_unique = False
                print("The key already exists")
            pos = pos.next
        if is_unique:
            new_node = Node(newElement, None, None)
            if index == None:
                pos = self.head.next
                while pos.next != self.head:
                    pos = pos.next
                new_node.prev = pos
                new_node.next = self.head
                self.head.prev = new_node
                pos.next = new_node

            else:
                is_valid_idx = True
                length = self.count()
                if index < 0 and index > length:
                    print("Invalid Index")
                    is_valid_idx = False

                if is_valid_idx:
                    if index == length:
                        last_node = self.head.prev
                        new_node.prev = last_node
                        new_node.next = self.head
                        self.head.prev = new_node
                        last_node.next = new_node
                    else:
                        i = 0
                        pos = self.head.next
                        while pos != self.head:
                            if i == index:
                                new_node = Node(newElement, None, None)
                                pre_node = pos.prev
                                new_node.prev = pre_node
                                new_node.next = pos
                                pre_node.next = new_node
                                pos.prev = new_node
                            pos = pos.next
                            i += 1

    def remove(self, index):
        length = self.count()
        if index < 0 or index > length - 1:
            raise Exception("Invalid Index")

        pos = self.head.next
        i = 0
        while pos != self.head:
            if i == index:
                prev_node = pos.prev
                next_node = pos.next
                prev_node.next = next_node
                next_node.prev = prev_node
            i += 1
            pos = pos.next

    def removeKey(self, deleteKey):
        is_exist = False
        pos = self.head.next
        while pos != self.head:
            if pos.elem == deleteKey:
                prev_node = pos.prev
                next_node = pos.next
                prev_node.next = next_node
                next_node.prev = prev_node
                is_exist = True
            pos = pos.next
        if is_exist:
            return f"The deleted element is {deleteKey}"
        else:
            return f"Key {deleteKey} does not exist"


# ==========================Tester Code==========================#
# Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
a = [10, 20, 30, 40, 50, 60]
l1 = DoublyList(a)
l1.showList()  # Should print: 10->20->30->40->50->60
# Task-2.5, 2.6 -- Insert
print("\n//=======Task 2.3, 2.4 -- Insert=======//")
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = DoublyList(c)
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
print("\n//=======Task 2.5 -- Remove=======//")
l3.remove(0)
l3.showList()  # Should print: 10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(11)
l3.showList()  # Should print: 10->20->30->40->110->50->60->70->80->90->100
l3.remove(5)
l3.showList()  # Should print: 10->20->30->40->110->60->70->80->90->100
print("\n//=======Task 2.6 -- removeKey=======//")
print(l3.removeKey(20))
l3.showList()  # Should print: 10->30->40->110->60->70->80->90->100
print(l3.removeKey(100))
l3.showList()  # Should print: 10->30->40->110->60->70->80->90
print(l3.removeKey(10))
l3.showList()  # Should print: 30->40->110->60->70->80->90
print(l3.removeKey(11))
