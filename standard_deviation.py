import math
import matplotlib.pyplot as plt
import numpy as np

def mean(arr=[]):
    total, n = 0, 0
    for i in range(0, len(arr)):
        total += arr[i]
        n += 1
    return total/n

#def median(arr=[]):
    

def sample_variance(arr = []):
    sample_mean = mean(arr)
    sum, n = 0, 0
    for i in range(0, len(arr)):
        sum = sum + (arr[i] - sample_mean)**2
        n += 1
    return sum / (n-1)

def standard_deviation(sample_variance):
    return math.sqrt(sample_variance)

def create_arr_from_str(arr_str: str):
    arr = []
    arr_count = 0
    current = ""

    for char in range(0, len(arr_str)):
        if arr_str[char].isdigit() is True:
            current = current + arr_str[char]
            if char == len(arr_str)-1:
                arr.append(float(current))
                arr_count += 1
        elif arr_str[char].isdigit() is False and arr_str[char-1].isdigit() is True:
            arr.append(float(current))
            arr_count += 1
            current = ""
    return arr

if __name__ == "__main__":
    
    arr_list = []
    valid = True

    while valid == True:
        arr_str = input("Enter array of numbers: ")
        arr = create_arr_from_str(arr_str)

        print(f"Mean of entered array is: {mean(arr)}")
        print(f"Sample variance of entered array is: {sample_variance(arr)}")
        print(f"Standard deviation of entered array is: {standard_deviation(sample_variance(arr))}")
        
        arr_list.append(arr)

        tmp = input("Enter another array? (y/n) ")
        if tmp == "y" or tmp == "Y":
            valid = True
        else:
            valid = False

    plt.boxplot(arr_list)
    plt.show()
    
