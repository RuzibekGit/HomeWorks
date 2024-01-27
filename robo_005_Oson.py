def find_pairs(Z):
    pairs = 0
    for X in range(1, 11):
        for Y in range(X, 11):  
            if X * Y == Z:
                pairs += 1
    return pairs


Z = -2
pairs = find_pairs(Z)
print(pairs)
