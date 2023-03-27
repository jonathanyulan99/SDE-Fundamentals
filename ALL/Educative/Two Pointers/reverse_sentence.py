'''
Prompt:
Given a sentence, reverse the order of its words without affecting the order of letters within a given word.

Sentence contains English uppercase and lowercase letters, digits, and spaces.

The order of the letters within a word is not to be reversed.

The input string may contain leading or trailing spaces or multiple spaces between words. 
The returned string, however, should only have a single space separating each word. 
Do not include any extra spaces.

E:
- What should the input take in if not a string? 
- What are acceptable characters?
- We are to reverse ordering but not the ordering of said words?
- Our output is a string.

B:
- reverse_sentence(Reversed String.)-> .String Reversed
- reverse_sentence("    Reversed String     ")-> String Reversed

P:
Solution1: Two Pointers at the end of the string and beginning
- trim the white space of the string 
- We need to build a new string because strings are immutable 
- Start a pointer at the beginning of the word and end of the word 
- Populate the new string from the beginning back 

I:

V:

'''


def reverse_words(sentence: str) -> str:
    # split the word .split() gets rid of all the empty white space
    # sentence comes back in a list[str] with no white space
    # then we can change it back to a string by " ".join(sentence) on the list[str]
    # this concatenates them together with one single " " between the elements
    # sentencex = sentence.split()
    # sentencey = " ".join(sentence.split())
    sentence = list(" ".join(sentence.split()))
    # sentence2 = " ".join(sentence.split())
    # print(sentence)
    str_reverse(sentence, 0, len(sentence)-1)
    # print(sentence)
    start_index = 0
    end_index = 0

    while start_index < len(sentence):
        while end_index < len(sentence) and sentence[end_index] != ' ':
            end_index += 1
        else:
            str_reverse(sentence, start_index, end_index-1)
            end_index += 1
            start_index = end_index

    # make our list back into a string
    return ''.join(sentence)


def str_reverse(_str, start, end):
    while start < end:
        temp = _str[start]
        _str[start] = _str[end]
        _str[end] = temp

        start += 1
        end -= 1


sentence1 = "    Welcome     to     Educative   "
sentence2 = "Hello Friend"
sentence3 = "Hurray 3 2 1"

print(reverse_words(sentence1))
# join takes a list and joins that list based on the literal value you pass in front of it
'''
evitacudE ot emocleW

'''
