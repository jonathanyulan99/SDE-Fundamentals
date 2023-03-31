def solution(words: list[str]):
    word_occurrences = dict()

    for idx in range(len(words)):
        word = ''.join(sorted(words[idx]))
        count = word_occurrences.get(word, 0)
        if count == 0:
            word_occurrences[word] = [words[idx]]
        else:
            word_occurrences[word].append(words[idx])

    return list(word_occurrences.values())


anagrams = ['aba', 'bad', 'dad', 'ac', 'ca', 'baa', 'dab', 'add']
print(solution(anagrams))
