from os import dup
from model_entity import Reference
from features import *

MASTER_FILE = "test_files\master.txt"
A_FILE = "test_files\A.txt"
B_FILE = "test_files\B.txt"

master_reference_list = read_data(MASTER_FILE, True)
a_reference_list = read_data(A_FILE, False)
b_reference_list = read_data(B_FILE, False)

a_error_reference_list = []
b_error_reference_list = []

duplicated_index_list = []
duplicated_index_list = duplicate_checking(master_reference_list)
print("****************************************************************************************")
print(f"Length of the master list before : {len(master_reference_list)}")
remove_duplicate_elements(master_reference_list, duplicated_index_list)
print(f"Length of the master list after : {len(master_reference_list)}")


master_reference_list = intersection_compare_reference_lists(master_reference_list, a_reference_list, True, a_error_reference_list)
master_reference_list = intersection_compare_reference_lists(master_reference_list, b_reference_list, False, b_error_reference_list)

print(len(a_error_reference_list))
print(len(b_error_reference_list))

print(f"Master section list list size : {len(master_reference_list)}")

counterA = 0
counterB = 0
for master_reference_list_element in master_reference_list:
    if master_reference_list_element.a_matches:
        counterA += 1
    if master_reference_list_element.b_matches:
        counterB += 1

print(f"counter A : {counterA}")
print(f"counter B : {counterB}")


# print(f"Master reference list size: {len(master_reference_list)}")
# print(f"A reference list size: {len(a_reference_list)}")
# print(f"B reference list size: {len(b_reference_list)}")
# Checked 3009 Master, 303 A, 675 B
# for x in master_reference_list:
#      x.print()