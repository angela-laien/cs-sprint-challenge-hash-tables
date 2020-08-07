def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    result = []
    for array in arrays:
        for num in array:
            if num in storage:
                storage[num] += 1
            else:
                storage[num] = 1
    
    for num in storage:
        if storage[num] > 1:
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
