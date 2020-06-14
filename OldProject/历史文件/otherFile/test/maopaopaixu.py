def bubbleSort(arr):
    length = len(arr)

    for j in range(length - 1, 0, -1):
        for i in range(0, length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


arr = [23, 41, 25, 54, 18, 14]
print(bubbleSort(arr))

arr = [23, 25, 41, 18, 14, 54]


# 每轮循环找到最大的值放到列表最后面，有几个值就循环几次
