word = "ABCD"


def subsequences(word: str, subseq: str = ''):
    if len(word) == 0:
        print('\"'+subseq+'\"')
        return

    subsequences(word[1:], subseq+word[0])
    subsequences(word[1:], subseq)


subsequences(word)
