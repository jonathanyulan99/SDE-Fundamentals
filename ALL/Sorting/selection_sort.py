def swap(inp: list, start_index: int, minimum_index: int):
    inp[start_index], inp[minimum_index] = inp[minimum_index], inp[start_index]


def selection_sort(inp):
    assert inp, "Must have an input to be sorted"

    if len(inp) == 1:
        return inp

    for start_index in range(0, len(inp)):
        minimum_index = start_index

        for secondary_index in range(start_index+1, len(inp)):
            if inp[minimum_index] > inp[secondary_index]:
                minimum_index = secondary_index

        swap(inp, start_index, minimum_index)


sample_input = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
print(*sample_input)
selection_sort(sample_input)
print(*sample_input)
