'''
Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. 
For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', 
which has a frequency of 2.

You are given an array of strings words and another array of query strings queries.
For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) 
for each W in words.

Return an integer array answer, where each answer[i] is the answer to the ith query.
'''

def numSmallerByFrequency(queries: list[str], words: list[str]) -> list[int]:
    def f(s:str):
        first_letter = sorted(s)[0]
        freq = s.count(first_letter)
        return freq 
    queries_counts = [f(query) for query in queries]
    words_counts = [f(word) for word in words]
    result = []
    for query_count in queries_counts:
        counter = 0 
        for word_count in words_counts:
            if query_count < word_count:
                counter += 1 
        result.append(counter)
    return result 

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
print(numSmallerByFrequency(queries,words))

queries = ["cbd"]
words = ["zaaaz"]
print(numSmallerByFrequency(queries,words))