from os import terminal_size
from typing import List, Set
from model_entity import Reference, Master_Reference, Secondary_Reference

# TODO Később majd ellenorizni kell az AB, PY, TI ..... utáni formátumokat, (Hány space kötöjel elott utan stb )


def read_data(file_name: str, is_master: bool):
    end_of_line = "ER  - "
    reference_list = []

    f = open(file_name, "r", encoding="utf8")
    
    # TODO az elozo erteket beleteszi hogy ha nincsen AB vagy PY vagy TI
    for x in f:
        if is_master is True:
            reference = Master_Reference()
        else:
            reference = Secondary_Reference()

        if x[0:6] == "AB  - ":
            abstract = x[6:]
        if x[0:6] == "PY  - ":
            publication_year = x[6:]
        if x[0:6] == "TI  - ":
            title = x[6:]
        if x[0:6] == end_of_line:
            reference.setter(abstract, publication_year, title)
            reference_list.append(reference)
            abstract = ""
            publication_year = ""
            title = ""
    
    f.close()
    return reference_list


def intersection_compare_reference_lists(master_reference_list: List[Master_Reference], secondary_reference_list: List[Secondary_Reference], is_A: bool, a_error_reference_list: List[Secondary_Reference] = [], b_error_reference_list: List[Secondary_Reference] = []):

    element_of_master_reference_list = Master_Reference()
    element_of_secondary_reference_list = Secondary_Reference()
    counter = 0
    included = False

    for element_of_secondary_reference_list in secondary_reference_list:
        for element_of_master_reference_list in master_reference_list:
            
            #print(
            #    f"ABSTRACT ELEMENTS : MASTER : {element_of_master_reference_list.abstract} | SECONDARY {element_of_secondary_reference_list.abstract}")
            #print(
            #    f"TITLE ELEMENTS : MASTER : {element_of_master_reference_list.title} | SECONDARY {element_of_secondary_reference_list.title}")
            #print(
            #    f"ABSTRACT ELEMENTS : MASTER : {element_of_master_reference_list.publication_year} | SECONDARY {element_of_secondary_reference_list.publication_year}")
            if element_of_master_reference_list.abstract == element_of_secondary_reference_list.abstract and element_of_master_reference_list.title == element_of_secondary_reference_list.title and element_of_master_reference_list.publication_year == element_of_secondary_reference_list.publication_year:
                if is_A is True:
                    element_of_master_reference_list.set_a_matches(True)
                    master_reference_list[counter].set_a_matches(True)
                    included = True
                    # print("A EGYEZIK")
                else:
                    element_of_master_reference_list.set_b_matches(True)
                    master_reference_list[counter].set_b_matches(True)
                    included = True
                    # print("B EGYEZIK")
        
            counter+=1
        counter = 0
        if not included and is_A:
            a_error_reference_list.append(element_of_secondary_reference_list)
        if not included and not is_A:
            b_error_reference_list.append(element_of_secondary_reference_list)

        included = False
    # print(f"{counter} times you can find matches")
    return master_reference_list

def duplicate_checking(master_reference_list: List[Master_Reference]):

    duplicated_index_set = set()
    for i in range(len(master_reference_list)):
        for j in range(i + 1, len(master_reference_list)):
            if master_reference_list[i].abstract == master_reference_list[j].abstract and master_reference_list[i].title == master_reference_list[j].title and master_reference_list[i].publication_year == master_reference_list[j].publication_year:
                duplicated_index_set.add(j)
                print(f"DUPLICATE ITEM")
                print(master_reference_list[j].title)
    
    duplicated_list = list(duplicated_index_set)
    duplicated_list.sort()
    print(f" DUPLIKALT LISTANAK HOSSZA{len(duplicated_list)}")
    return duplicated_list

def remove_duplicate_elements(master_reference_list: List[Master_Reference], duplicate_element_index_list: List[int]):

    for index in range(len(duplicate_element_index_list)-1, -1, -1):
        master_reference_list.pop(index)




# A és B ben létezik e olyan elem ami niincs benne a MATERBEN mert akkor fogyatkes a felhasznalo
