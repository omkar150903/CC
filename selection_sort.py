def selectionSort(array, size):
    for indexex in range(size):
        min_indexex = indexex
        for j in range(indexex + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_indexex]:
                min_indexex = j
        # swapping the elements to sort the array
        (array[index], array[min_indexex]) = (array[min_indexex], array[index])

arr = [-5,-10,80,-50,100,-40,90,60,70,0,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
