# ========================================= Task - 2 =================================================================
# Hashing
class myHashTable:
    def __init__(self, arr):
        self.arr = arr
        self.hash_table = [0] * 9
        for i in arr:
            self.insert_string(i)

    def hash_function(self, elem):
        vowel_lst = ["A", "E", "I", "O", "U"]
        count_consonant = 0
        sum_of_digits = 0
        for i in elem:
            if 65 <= ord(i) <= 90:
                if i not in vowel_lst:
                    count_consonant += 1
            else:
                sum_of_digits += int(i)
        hash_number = ((count_consonant * 24) + sum_of_digits) % 9
        return hash_number

    def insert_string(self, elem):
        hash_idx = self.hash_function(elem)
        if self.hash_table[hash_idx] != 0:
            while self.hash_table[hash_idx] != 0:
                hash_idx = (hash_idx + 1) % 9
            self.hash_table[hash_idx] = elem
        else:
            self.hash_table[hash_idx] = elem

    def show_hashtable(self):
        return self.hash_table


arr = ["ST1E89B8A32", "RIFA321TASFIYA", "MO56YA44NA", "ST1E89B8A32", "MINO555NS", "RIFA321TASFIYA", "ST1E89B8A32",
       "864PIIPUU", "ST1E89B8A32"]

h1 = myHashTable(arr)
print(h1.show_hashtable())  # Should print ['864PIIPUU', 'MO56YA44NA', 'ST1E89B8A32', 'MINO555NS', 'ST1E89B8A32',
# 'ST1E89B8A32', 'RIFA321TASFIYA', 'RIFA321TASFIYA', 'ST1E89B8A32']
