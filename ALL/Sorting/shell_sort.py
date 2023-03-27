'''

Shellsort is a another version of insertion sort that gains speed by allowing 
exchanges of entries that are far apart, to produce partially sorted arrays that 
can be efficiently sorted, eventually by insertion sort. The idea is to rearrange 
the array to give it the property that taking every `h` elements (starting anywhere)
 yields a sorted sequence. Such an array is said to be `h`-sorted.

'''
# shell_sort == insertion sort w/GAP == 1


def shell_sort(inp: list):
    if inp is None or len(inp) < 1:
        print("Nothing to Sort")
        return

    divisor = 2
    length = len(inp)
    gap = length // divisor

    while gap > 0:
        for start in range(gap, length):
            anchor = inp[start]
            runner = start

            while runner >= gap and inp[runner-gap] > anchor:
                inp[runner] = inp[runner-gap]
                runner -= gap
            inp[runner] = anchor
        gap = gap // divisor


sample_input_2 = [21, 38, 29, 17, 4, 25, 11, 32, 9]
sample_input = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
print(*sample_input_2)
shell_sort(sample_input_2)
print(*sample_input_2)

tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
]

for elements in tests:
    if len(elements) == 0:
        pass
    else:
        shell_sort(elements)
        print(*elements)
