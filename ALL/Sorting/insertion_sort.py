def insertion_sort(inp):
    assert inp, "No Input, An Input is Required to Sort"

    if len(inp) == 1:
        return

    for start_index in range(1, len(inp)):
        anchor = inp[start_index]

        shifting_indices = start_index - 1

        while shifting_indices >= 0 and anchor < inp[shifting_indices]:
            inp[shifting_indices+1] = inp[shifting_indices]
            shifting_indices -= 1
        inp[shifting_indices+1] = anchor


def insertion_sort_2(inp):
    for a in range(1, len(inp)):
        b = a
        while b > 0 and inp[b] < inp[b-1]:
            inp[b], inp[b-1] = inp[b-1], inp[b]
            b -= 1


sample_input = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
sample_input = [8, 5, 3, -13, 2, 1, -10, 32, 45, 0, 6]
print(*sample_input)
insertion_sort_2(sample_input)
print(*sample_input)
