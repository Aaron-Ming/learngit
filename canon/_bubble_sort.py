
arr = [7, 6, 5, 4, 3]

length = len(arr) - 1

for x in range(length):
    for y in range(length - x):
        if arr[y] > arr[y+1]:
            arr[y], arr[y+1] = arr[y+1], arr[y]
        print arr
