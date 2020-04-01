#generate list of random integers according to specifications
#list size specified by user at run-time
#range of integer values specified by user at run-time
#run functions with generated list of integers
#calculate and display the time it took to run the function
#allow for multiple runs

import time
from random import randint

#generate_list

list_size = int(input("What is the size of the list you want to create? "))
max_range_value = int(input("What is the max value of the range? "))
run_times = int(input("How many times do you want to run? "))

integers_list = [randint(0,max_range_value) for num in range(list_size)]
print("UNSORTED LIST: ", integers_list)

#quicksort

def quicksort(arr):
    
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)       
    return quicksort(smaller) + equal + quicksort(larger)

#mergesort

def merge_sorted(arr1,arr2):
    sorted_arr = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
         
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    return sorted_arr

def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return merge_sorted(l1, l2)

#bubblesort

def bubblesort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

#selection_sort

def selectionsort(arr):
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1
    return arr


#time_to_run

def time_func(func_name, arr):
    time1 = time.time()
    func_name(arr)
    time2 = time.time()
    run_time = time2 - time1
    print(f"{func_name.__name__.upper()} - elapsed time: {run_time} sec")

#results

for num in range(run_times):
    print(f"Run: {num+1:}")
    time_func(quicksort, integers_list)
    time_func(mergesort, integers_list)
    time_func(bubblesort, integers_list.copy())
    time_func(selectionsort, integers_list)
    print("-"*70)