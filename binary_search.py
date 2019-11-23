def binary_search(a_list, item, steps_inner=0):
    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = a_list[mid]
        steps_inner += 1
        if guess == item:
            return mid, steps_inner
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [5, 8, 11, 15, 21, 23, 100, 223]
index, steps = binary_search(my_list, 223)
print(index, steps)
