
array = [3, 25, 6, 2, 0]

hashm = {}
# build a hashmap from the values
# key will be value and hashm[value] will be index
for i, value in enumerate(array):
    hashm[value] = i

array.sort()

# we use the values in the array to get the original indexes
for value in array:
    print(value, hashm[value])
