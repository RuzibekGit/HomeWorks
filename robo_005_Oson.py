def count_pairs(Z):
    count = 0
    for X in range(Z+1):
        if Z % X == 0:
            Y = Z // X
            if X <= Y:
                count += 1
    return count




Z = -2
print(count_pairs(Z))
