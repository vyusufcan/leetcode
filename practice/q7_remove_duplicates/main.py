def remove_duplicates(n: list) -> list:
    new_list=[]
    for x in n:
        if x not in new_list:
            new_list.append(x)
    return new_list

remove_duplicates([1, 2, 2, 3, 4, 4, 5])
