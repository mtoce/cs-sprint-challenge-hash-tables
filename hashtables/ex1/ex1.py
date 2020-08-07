def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    idx = []
    lookup = {}
    # length has to be greater than 1
    if length > 1:
        for i in range(length):
            lookup[weights[i]] = limit - weights[i]
            if lookup[weights[i]] in weights:
                print(f"weights[i]: {weights[i]}")
                print(f"limit: {limit}")
                print(f"lookup[weights[i]]: {lookup[weights[i]]}")
                idx.append(i)
    print(f"indexes of weights that form a pair: {idx}")
    print(f"Two paired weights, not ordered: {[weights[idx[0]], weights[idx[1]]]}")
    if len(idx) > 1:
        # place higher valued index first
        if idx[0] > idx[1]:
            print(f"Two paired weights in order: {[weights[idx[0]], weights[idx[1]]]}")
            return (idx[0], idx[1])
        else:
            print(f"Two paired weights in order: {[weights[idx[1]], weights[idx[0]]]}")
            return (idx[1], idx[0])
    
    # return None if no pairs found
    return None

# checking with test 3
weights_3 = [4, 6, 10, 15, 16]
answer3 = get_indices_of_item_weights(weights_3, 5, 21)
print(f"Indexes - should be (3, 1): {answer3}")