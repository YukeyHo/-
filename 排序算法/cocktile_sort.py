def cocktail_sort(arr):
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        swapped = False
        for i in range(left, right):  # 从左到右冒泡
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        right -= 1  # 右边界缩小
        for i in range(right, left, -1):  # 从右到左冒泡
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        left += 1  # 左边界缩小
        if not swapped:
            break  # 如果没有交换，提前结束
    return arr

#鸡尾酒排序（Cocktile Sort）算法，因为其执行过程像是有一个调酒师在左右摇晃调酒壶（Shaker）而得名。
#你可以想象一个鸡尾酒调酒师将调酒壶左右摇晃，大的气泡往右边冒泡，小的气泡往左边冒泡，由此完成了气泡从小到大的升序排列。
#鸡尾酒排序算法的时间复杂度仍然是O(n^2)，只是相比于单向冒泡排序略微减少了一些无效比较。
