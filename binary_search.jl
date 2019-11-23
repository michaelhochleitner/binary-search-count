function binary_search(list, item)
    low = 1
    high = length(list)

    while low <= high
        mid = Int(floor((low + high)/2))
        guess = list[mid]
        if guess == item
            return mid
        elseif guess > item
            high = mid - 1
        else
            low = mid + 1
        end
    end
    return 0
end

my_list = [1, 3, 5, 7, 9]
println(binary_search(my_list, 10))
