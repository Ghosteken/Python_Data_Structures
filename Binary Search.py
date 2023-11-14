# def binary_search(arr, x):
#    low = 0
#    high = len(arr) - 1
#    while [low] <= [high]: # it has to be sorted
#        mid = low + high //2
#        if (arr[mid] < x ):
#            low = mid + 1
#        elif (arr[mid]> x):
#            high = mid - 1
#        else:
#            return mid 
        
#    return -1         
          
def Binary_search(arr,x):
    low = 0 
    high = len(arr)-1
   
    while [low] <= [high]: 
       mid = low + high // 2
       if (arr[mid] < x):
           low = mid +1
       elif (arr[mid] > x):
           high = mid - 1
       else:
           return mid
    return -1        
                 

    #this results in a worst case time complexity of O(log2N).

    
    
    
    
    
    
    
    
    
    
    
    
    
#    while low <= high:
#        mid = (low + high) // 2
#        if arr[mid] < x:
#            low = mid + 1
#        elif arr[mid] > x:
#            high = mid - 1
#        else:
#            return mid
#    return -1
