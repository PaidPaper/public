def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have the same length for addition")

    result = []

    # Iterate through the arrays and add corresponding elements
    for i in range(len(arr1)):
        result.append(arr1[i] - arr2[i])

    return result
