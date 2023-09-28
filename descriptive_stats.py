import math
import matplotlib.pyplot as plt
import numpy as np
from quicksort import *

def mean(arr):
    total, n = 0, 0
    for i in range(0, len(arr)):
        total += arr[i]
        n += 1
    return total/n

def median(arr):
    quickSort(arr, 0, len(arr)-1)
    if len(arr)%2 == 1:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2] + arr[(len(arr)//2)+1])/2
    
def fiveNumberSummary(arr):
    quickSort(arr, 0, len(arr)-1)

    min, max = arr[0], arr[len(arr)-1]
    q1, med, q3 = 0, 0, 0
    
    if len(arr)%2 == 1:
        q1 = arr[len(arr)//4]
        med = arr[len(arr)//2]
        q3 = arr[(3*len(arr)//4)]
    else:
        q1 = (arr[len(arr)//4] + arr[(len(arr)//4)+1])/2
        med = (arr[len(arr)//2] + arr[(len(arr)//2)+1])/2
        q3 = (arr[(3*len(arr))//4] + arr[(3*(len(arr))//4)+1])/2
    
    return [("Min", min), ("Q1", q1), ("Med", med), ("Q3", q3), ("Max", max)]

def printFiveNSumm(data):
    for label, value in data:
        print(f"{label}: {value}")
    
def sample_variance(arr):
    sample_mean = mean(arr)
    sum, n = 0, 0
    for i in range(0, len(arr)):
        sum = sum + (arr[i] - sample_mean)**2
        n += 1
    return sum / (n-1)

def alt_sample_variance(arr):
    sum1, sum2, n = 0, 0, 0
    # first part S(x.i)^2
    for i in range(0, len(arr)):
        sum1 = sum1 + arr[i]**2
        n += 1
    # second part (S(x.i))^2
    for i in range(0, len(arr)):
        sum2 = sum2 + arr[i]
    sum2 = (sum2**2)/n
    return (sum1 - sum2)/(n-1)

def standard_deviation(sample_variance):
    return math.sqrt(sample_variance)

def create_arr_from_str(arr_str: str):
    arr = []
    arr_count = 0
    current = ""

    for char in range(0, len(arr_str)):
        if arr_str[char].isdigit() or (arr_str[char] == "."):
            current = current + arr_str[char]
            # at end of input string just 
            if char != "." and char == len(arr_str)-1:
                arr.append(float(current))
                arr_count += 1
        elif arr_str[char].isdigit() is False and arr_str[char-1].isdigit() is True:
            arr.append(float(current))
            arr_count += 1
            current = ""
    return arr


if __name__ == "__main__":

    arr_list = [] # store list of arrays

    # keep prompting user for arrays until valid == False
    valid = True
    while valid == True:
        arr_str = input("Enter array of numbers: ")
        arr = create_arr_from_str(arr_str)

        print(f".\n.\nMean: {mean(arr)}")
        print(f"Median: {median(arr)}")
        print("Five number summary:")
        for label, value in fiveNumberSummary(arr):
            print(f" - {label}: {value}")
        print(f"Sample variance: {sample_variance(arr)}")
        print(f"Sample variance (alt. formula): {alt_sample_variance(arr)}")
        print(f"Standard deviation: {standard_deviation(sample_variance(arr))}")

        arr_list.append(arr)

        tmp = input(f".\n.\nEnter another array? (y/n) ")

        if tmp == "y" or tmp == "Y":
            valid = True
        else:
            valid = False

    plt.boxplot(arr_list)
    plt.show()
    
