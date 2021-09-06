

forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
arr = []
# we are sorting by the first index here and then for each index combo we check if the value is more than 1
arr = sorted((v, r, c)for r, row in enumerate(forest)
             for c, v in enumerate(row) if v > 1)

print(arr)
