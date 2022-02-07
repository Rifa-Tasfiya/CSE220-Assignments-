# ======================================== Task-1 =====================================================================
# Key index Searching & Sorting
import sys


class KeyIndex:
    def __init__(self, a):
        self.min = self.find_minval(a)
        if self.min < 0:
            pos_minval = self.min * (-1)
            size_a = len(a)
            temp_a = [0] * size_a
            for i in range(size_a):
                temp_a[i] = a[i] + pos_minval
            # print(temp_a)
            self.k = [0] * (self.find_maxval(temp_a) + 1)
            for i in temp_a:
                self.k[i] = self.k[i] + 1
            # print(self.k)
            # print(f"min val: {self.min}")

        else:
            self.k = [0] * (self.find_maxval(a) + 1)
            for i in a:
                self.k[i] = self.k[i] + 1
            # print(self.k)

    def find_minval(self, a):
        min_value = sys.maxsize
        for i in a:
            if i < min_value:
                min_value = i
        return min_value

    def find_maxval(self, a):
        max_value = -sys.maxsize
        for i in a:
            if i > max_value:
                max_value = i
        return max_value

    def do_search(self, val):
        size_k = len(self.k)
        if self.min >= 0:
            if val < size_k and val >= 0 and self.k[val] > 0:
                return "true"

            else:
                return "false"
        else:
            temp = val + (self.min * (-1))
            if temp < size_k and temp >= 0 and self.k[temp] > 0:
                return "true"
            else:
                return "false"

    def do_sort(self):
        global a
        sorted_arr = [0] * len(a)
        if self.min >= 0:
            idx = 0
            for i in range(len(self.k)):
                if self.k[i] > 0:
                    counter = self.k[i]
                    while counter != 0:
                        sorted_arr[idx] = i
                        counter = counter - 1
                        idx += 1
            return sorted_arr
        else:
            idx = 0
            for i in range(len(self.k)):
                if self.k[i] > 0:
                    counter = self.k[i]
                    while counter != 0:
                        sorted_arr[idx] = i + self.min
                        counter = counter - 1
                        idx += 1
            return sorted_arr

        # print(a)


# ============================================ Tester Code ===========================================================
# ============================================= Input-1 ==============================================================
accuracy_flag = True
a = [0, -1, -2, -3, -4, -5]
obj_1 = KeyIndex(a)
print("For input-1 :")
print(obj_1.do_search(100))  # Output should be false
if obj_1.do_search(100) != "false":
    accuracy_flag = False
print(obj_1.do_search(-5))   # Output should be true
if obj_1.do_search(-5) != "true":
    accuracy_flag = False
print(obj_1.do_sort())  # Output should be [-5, -4, -3, -2, -1, 0]
if obj_1.do_sort() != [-5, -4, -3, -2, -1, 0]:
    accuracy_flag = False
print()
# =========================================== Input-2 ================================================================
a = [4, -2, 3, -4, 7, 4]
obj_2 = KeyIndex(a)
print("For input-2 :")
print(obj_2.do_search(70))  # Output should be false
if obj_2.do_search(70) != "false":
    accuracy_flag = False
print(obj_2.do_search(4))   # Output should be true
if obj_2.do_search(4) != "true":
    accuracy_flag = False
print(obj_2.do_sort())  # Output should be [-4, -2, 3, 4, 4, 7]
if obj_2.do_sort() != [-4, -2, 3, 4, 4, 7]:
    accuracy_flag = False
print()

# ========================================== Input-3 =================================================================
a = [4, 2, 3, 4, 7, 4]
obj_3 = KeyIndex(a)
print("For input-3 :")
print(obj_3.do_search(99))  # Output should be false
if obj_3.do_search(99) != "false":
    accuracy_flag = False
print(obj_3.do_search(3))   # Output should be true
if obj_3.do_search(3) != "true":
    accuracy_flag = False
print(obj_3.do_sort())  # Output should be [2, 3, 4, 4, 4, 7]
if obj_3.do_sort() != [2, 3, 4, 4, 4, 7]:
    accuracy_flag = False
print()

# ====================================== Accuracy =====================================================================
if accuracy_flag:
    print("TESTING: \n   All the methods in the KeyIndex class is working properly")
else:
    print("TESTING: \n   All the methods in the KeyIndex class is NOT working properly")
