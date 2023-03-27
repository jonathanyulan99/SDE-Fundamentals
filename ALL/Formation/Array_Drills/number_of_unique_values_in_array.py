'''
Q. Given an unsorted array, return the number of unique elements that appear only once in the array.

Examples:
• Given an array: [3, 1, 1, 2, 3, 1, 1, 1, 4] // returns 2 (unique elements: 2 and 4)
• Given an array: [1] // returns 1 (unique element: 1)

B: 
- Will we always be given an array input 
- [] -> return -1 or [] 
- Do we need to sort this array?
- We need to iterate through the entire array to check whether the value is unique or not 

E:
- O(N) to iterate through the array 
- O(N) to store the seen values? Set? Map?

P: 
- Set a unique_count to zero 
- initialize a dict()
- Iterate through the array
- If num is in our dictionary then decrement unique_count
- If the num is not in our dictionary then increment unique_count and store it 
- return the unique_count 

'''
# Implement


def numUniques(array: list[int]) -> int:
    # Write your code here.
    unique_count = 0
    map = dict()

    for num in array:
        if num not in map:
            map[num] = 1
        elif num in map:
            map[num] += 1

    for k, v in map.items():
        if map[k] == 1:
            unique_count += 1

    return unique_count


# Test Cases - Verify
print(numUniques([]))  # 0
print(numUniques([3, 1, 1, 2, 3, 1, 1, 1, 4]))  # 2
print(numUniques([1]))  # 1


def numUniques2(array: list[int]) -> int:
    d = dict()
    unique_counts = 0

    for index, value in enumerate(array):
        counts = d.get(array[index], 0)

        if counts == 0:
            unique_counts += 1
        elif counts == 1:
            unique_counts -= 1

        d[value] = counts + 1

    return unique_counts


print(numUniques2([]))  # 0
print(numUniques2([3, 1, 1, 2, 3, 1, 1, 1, 4, 5, 2, 4, 5]))  # 2
print(numUniques2([1]))  # 1
