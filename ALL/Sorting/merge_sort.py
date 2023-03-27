def merge(inp, l, m, r):
    left_size = m - l + 1
    right_size = r - m

    L = [0] * left_size
    R = [0] * right_size

    for x in range(left_size):
        L[x] = inp[l+x]

    for x in range(right_size):
        R[x] = inp[m+1+x]

    l_i = r_i = 0
    # this needs to be updated with the left_terminating end of the
    f_i = l

    while l_i < left_size and r_i < right_size:
        if L[l_i] < R[r_i]:
            inp[f_i] = L[l_i]
            l_i += 1
        else:
            inp[f_i] = R[r_i]
            r_i += 1
        f_i += 1

    while l_i < left_size:
        inp[f_i] = L[l_i]
        l_i += 1
        f_i += 1

    while r_i < right_size:
        inp[f_i] = R[r_i]
        r_i += 1
        f_i += 1


def merge_sort(inp, l, r):
    if l < r:

        m = (l+(r-1))//2

        merge_sort(inp, l, m)
        merge_sort(inp, m+1, r)
        merge(inp, l, m, r)


sample_input = [21, 38, 29, 17, 1, 3, 4, 25, 11, 32, 9]
print(*sample_input)
merge_sort(sample_input, 0, len(sample_input)-1)
print(sample_input)
