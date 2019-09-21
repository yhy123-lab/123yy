
#快速排序
def quick_sort(data):
    store = data[0]
    i = 1
    j = len(data) - 1
    if len(data) > 1:
        while j > i:
            if data[i] > store:
                if data[j] <= store:
                    data[i],data[j] = data[j],data[i]
                else:
                    j -= 1
            else:
                i += 1
        if data[j] <= store:
            data[j],data[0] = data[0],data[j]
        return quick_sort(data[:j]) + quick_sort(data[j:])
    else:
        return data
