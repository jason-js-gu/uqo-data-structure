def quick_sort(arr): 
    less,equal,greater=[],[],[]
    if len(arr)>1:
        pivot=arr[0]        
        for i in arr:
            if i<pivot:
                less.append(i)
            elif i==pivot:
                equal.append(i)
            else:
                greater.append(i)
        return quick_sort(less)+equal+quick_sort(greater)
    return arr

ar=[12,4,5,6,7,3,1,15]

print(quick_sort(ar))
