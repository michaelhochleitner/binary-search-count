def binary_search(a_list, item):
    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = a_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [5, 8, 11, 15, 21, 23, 100, 223]
index= binary_search(my_list, 224)
print(index)
