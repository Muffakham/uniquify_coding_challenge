def getTensor(arr, shape):
    """
    this funciton takes in a list of data, converts it into a tensor of the corresponding shape given
    Inputs -  list of data, list of shape
    Outputs - "Error message" if there us an error with the shape list
               [] if a shape list is empty
               Tensor of the given shape, if the above two conditions are not met
    """
    if shape:
        #only work with the list of data, the shape list is non mepty.
        for i in range(len(shape)):
            #if the spae list has empty dimension or has a dimesion not as integer
            if (type(shape[i-1]) != type(shape[i])) or not (shape[i]) or type(shape[i]) != int:
                return "Erroneous shape array!"
        mval = 1
        for i in shape: mval *= i #calculating the toal number of data points needed according to the dimensions (product of dimensions)
        if len(arr) > mval: 
            #trimming the data list if it is too long
            arr = arr[:mval]
        else:
            #padding the data list with 0 if it is smaller than number of data points required
            while len(arr) < mval:
                arr.append(0)
            
        for i in shape[::-1]:
            #iterating over shape from lowest order dimension to higest order
            newArr = [] 
            for j in range(0,len(arr),i):
                #creating tensors of current dimension
                newArr.append(arr[j:j+i])
            arr = newArr #updating the list with newly created tensors
        
        newArr = newArr[0]
        return newArr
    else:
        return []
    
