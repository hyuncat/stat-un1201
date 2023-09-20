import math
import matplotlib.pyplot as plt
import numpy as np

def mean(arr=[]):
    total, n = 0, 0
    for i in range(0, len(arr)):
        total += float(arr[i])
        n += 1
    return total/n

def sample_variance(arr = []):
    sample_mean = mean(arr)
    sum, n = 0, 0
    for i in range(0, len(arr)):
        sum = sum + (float(arr[i]) - sample_mean)**2
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
                arr.append(current)
                arr_count += 1
        elif arr_str[char].isdigit() is False and arr_str[char-1].isdigit() is True:
            arr.append(current)
            arr_count += 1
            current = ""
    return arr

if __name__ == "__main__":
    arr_str = input("Enter array of numbers: ")
    arr = create_arr_from_str(arr_str)
    
    print(f"Mean of entered array is: {mean(arr)}")
    print(f"Sample variance of entered array is: {sample_variance(arr)}")
    print(f"Standard deviation of entered array is: {standard_deviation(sample_variance(arr))}")

    
