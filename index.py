def find_index(lst, target):
    try:
        return lst.index(target)
    except ValueError:
        return -1
my_list = [10, 20, 30, 40, 50]
target_value = 50
index = find_index(my_list, target_value)
print(f"The index of {target_value} is {index}.")
