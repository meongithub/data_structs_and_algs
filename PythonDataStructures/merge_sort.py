import math
import os

def main():
    sorted_list = des_merge_sort([0,9])
    assert(sorted_list == [9,0])
    print(sorted_list)

    sorted_list = des_merge_sort([1,3,5])
    assert(sorted_list == [5,3,1])
    print(sorted_list)

    sorted_list = des_merge_sort([-3,4,6,1,19])
    assert(sorted_list == [19,6,4,1,-3])
    print(sorted_list) 
    

def des_merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    if len(numbers) == 2:
        if (numbers[1] < numbers[0]):
            return numbers

        else:
            numbers[1], numbers[0] = numbers[0], numbers[1]
            return numbers

    else:
        half_length = math.ceil(len(numbers)//2)
        sorted_half1 = des_merge_sort(numbers[:half_length])
        sorted_half2 = des_merge_sort(numbers[half_length:])

        return merge_lists(sorted_half1, sorted_half2)

        

def merge_lists(left, right):
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    while left:
        result.append(left[0])
        left.pop(0)
    
    while right:
        result.append(right[0])
        right.pop(0)

    return result

if __name__ == "__main__":
    main()



