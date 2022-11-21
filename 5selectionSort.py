# Selection sort 

def selectionSort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[minimum] > array[j]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array


Array = [9, 5, 8, 4, 3, 1]
print("Sorted Array")
print(selectionSort(Array))