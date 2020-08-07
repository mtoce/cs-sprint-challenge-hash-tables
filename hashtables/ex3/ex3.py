def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    for i, arr in enumerate(arrays):
        arrays[i] = dict.fromkeys(arr, 1)
    
    matches = []
    for i in range(1, len(arrays)):
        first_array = arrays[0].keys()
        ith_array = arrays[i].keys()
        # when i = 1:
            # compares arrays[0] with arrays[1]
            # appends to matches if there is the same value (&)
        # when i = 2:
            # compares arrays[0] with arrays[2]
            # appends to matches if there is a crossover
        # ...
        matches.append(list(first_array & ith_array))

    # only take one match inside matches list
    result = matches[0]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))