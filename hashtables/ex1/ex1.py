def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    for i, item in enumerate(weights):
        storage[item] = i

    for i, item in enumerate(weights):
        target = limit - item
        if target in storage:
            j = storage[target]
            if i > j:
                return (i, j)
            else:
                return (j, i)