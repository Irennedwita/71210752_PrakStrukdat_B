#UG PRAKSTRUKDAT 10

def quicksort(data, start, end):
    if start < end:
        pivot_index = partition(data, start, end)
        quicksort(data, start, pivot_index-1)
        quicksort(data, pivot_index+1, end)
        data.sort(reverse=True)
    return data

def partition(data, start, end):
    pivot = data[end]
    left = start
    right = end - 1
    while left <= right:
        while data[left] < pivot:
            left = left + 1
        while data[right] > pivot:
            right = right - 1
        if left <= right:
            data[left], data[right] = data[right], data[left]
            left = left + 1
            right = right - 1
    data[left], data[end] = data[end], data[left]
    return left
    
    

lst0 = [4,5,3,2,1]
lst1 = [1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56]
lst2 = [20,21,22,23,24,25,26,27]
lst3 = [30,29,31,33,19,20,31,21,59]
print(quicksort(lst0,0,len(lst0)-1))
print(quicksort(lst1,0,len(lst1)-1))
print(quicksort(lst2,0,len(lst2)-1))
print(quicksort(lst3,0,len(lst3)-1))