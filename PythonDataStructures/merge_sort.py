import math
import os

def main():
    sorted_list = des_merge_sort([1,3,2,5])
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

        for i in range(0, half_length+1, 2):
            # initial list is uneven size
            if (i > len(sorted_half2)):
                numbers[i] = sorted_half1[i]                

            if sorted_half1[i] < sorted_half2[i]:
                numbers[i] = sorted_half2[i]
                numbers[i+1] = sorted_half1[i]

            else:
                numbers[i] = sorted_half1[i]
                numbers[i+1] = sorted_half2[i]

        return numbers

if __name__ == "__main__":
    main()



