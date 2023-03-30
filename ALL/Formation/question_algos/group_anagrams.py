def group_anagrams(words: list[str]) -> list[list[str]]:
    word_dict = {}

    for idx in range(len(words)):
        word = ''.join(sorted(words[idx]))
        if word not in word_dict:
            word_dict[word] = words[idx]
        else:
            word_dict[word].append(words[idx])

    return list(word_dict.values())


print(group_anagrams(['aab', 'bba', 'c', 'abb', 'baa', 'aba', 'bab']))
