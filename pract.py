def bubble_sort(arr):
    array_length = len(arr)
    for i in range(array_length):
        for j in range(array_length):
            if (arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]






my_array = [32, 56, 11, 45, 66, 1, 3, 77, 25]
bubble_sort(my_array)
print(my_array)