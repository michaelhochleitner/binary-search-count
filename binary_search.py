def binary_search(a_list, item, comparisons_inner=0):
    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = a_list[mid]
        comparisons_inner += 1
        if guess == item:
            return mid, comparisons_inner
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None, comparisons_inner


my_list = [5, 8, 11, 15, 21, 23, 100, 223]
index, comparisons = binary_search(my_list, 223)
print(index, comparisons)
