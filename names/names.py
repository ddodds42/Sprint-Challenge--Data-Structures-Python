import time
import sys
sys.path.insert(1, "../ring_buffer/")
from linked_list import Node, LinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

for name_1 in names_1:
    if name_1 in names_2:
        duplicates.append(name_1)

# ll1 = LinkedList()
# ll2 = LinkedList()
# for name_1 in names_1:
#     ll1.add_to_tail(name_1)
# # for name_2 in names_2:
# #     ll2.add_to_tail(name_2)
# # for node_1 in ll1:
# for name_2 in names_2:
#     if ll1.contains(name_2):
#         duplicates.append(name_2)


'''
Jam names from name1 into a linked list
recursive contains fxn
if names_2.contains(name1)
append it
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds \n")
print ('The former code is QUADRATIC TIME. The new code is LOG-LINEAR TIME.')

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
