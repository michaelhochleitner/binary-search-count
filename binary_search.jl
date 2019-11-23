function binary_search(list, item, comparisons_inner=0)
    low = 1
    high = length(list)

    while low <= high
        mid = Int(floor((low + high)/2))
        guess = list[mid]
        comparisons_inner+=1
        if guess == item
            return mid,comparisons_inner
        elseif guess > item
            high = mid - 1
        else
            low = mid + 1
        end
    end
    return 0,comparisons_inner
end

my_list = [5, 8, 11, 15, 21, 23, 100, 223]
println(binary_search(my_list, 223))
