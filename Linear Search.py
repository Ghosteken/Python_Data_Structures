def Linear_Search(arr,x):
    for i in range(len(arr)):
        if [i] == x:
           return i
    return -1   


# it has a complexity of O(N) because each element in an array is compared only once.
