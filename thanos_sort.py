def unite(l, r):
    united = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            united.append(l[i])
            i += 1
        else:
            united.append(r[j])
            j += 1
    if i < len(l):
        united += l[i:]
    else:
        united += r[j:]
    return united

def thanos_sort(arr):
    if len(arr) <= 1:
        return arr
    sorted1 = []
    unsorted = []
    prev = 0
    for n in arr:
        if not sorted1:
            sorted1.append(n)
            prev = n
        elif n >= prev:
            sorted1.append(n)
            prev = n
        else:
            unsorted.append(n)
    if unsorted:
        sorted2 = thanos_sort(unsorted)
        return unite(sorted1, sorted2)
    return sorted1
        

arr = thanos_sort([3, 8, 9, 9, 5, 2, 7, 0, 0, 1])
print(arr)
