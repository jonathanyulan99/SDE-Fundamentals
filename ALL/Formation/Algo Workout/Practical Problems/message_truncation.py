'''
❓ PROMPT
You're working on the UI for the text messaging app for a phone.
In a message notification, there is limited space, so the entire message cannot be shown, so the app designer wants 
to show a truncated form of the message in the space allotted.

The message will be words separated by spaces. Don't worry about punctuation or other special characters.
Consider any series of characters other than spaces as a word.

Example(s)                                       12345678
truncateMessage("This is a test message", 8) == 'This ...'
                                                'This is ' # not allowed because we don't have the truncation 
truncateMessage("This is a test message", 11) == 'This is ...'
truncateMessage("This is a test message", 15) == 'This is a ...'
truncateMessage("This is a test message", 20) == 'This is a test ...'
truncateMessage("This is a test message", 25) == 'This is a test message'

🛠️ IMPLEMENT
function truncateMessage(message, threshold) {
def truncateMessage(message: str, threshold: int) -> str:

Given an input text message (string) and a maximum number of characters (integer), return the truncated string.

The rules for truncation are as follows:
- If the string must be truncated, it must be indicated as such with a trailing '...', a space then three periods.
- If there is a word before the '...' then there must also be a space.
- Including the truncation indicator, the resulting string must be less than the provided maximum number of characters.
- Truncation can only happen on word boundaries (mustn't include partial words)
- If the whole string fits in the allotted space, no truncation is necessary.

Get the length of the inp_string 
Check to see if the length of the string <= threshold:
    if it is then just output the string 
sentence_length = 0
res = ''
truncation_string = ' ...'
temp = message.split() ==> changes string into a list/array => "This" "is" "a" "test" "message" 
for word in temp: # iterate through our list of words
    if len(word) + 4 + current_sentence_length <= threshold: # change our result to include that word because its under the threshold, len(word) includes our space 
        
    else:
        res += truncation_string
    
    sentence_length gets updated with the new string len()
return res # at end 

truncation = '_...' = len(4) 
if truncation: 
    beg_string + '_...'
else:
    beg_string + rest_of_message 
'''
def truncateMessage(message: str, threshold: int) -> str:
    # no truncation needed
    if len(message) <= threshold:
        return message 

    # sentence_length variable to update 
    sentence_length = 0 
    # res string to output
    res = ''
    # truncation string to add
    truncation_string = ' ...'
    
    # get a temp list from our message
    words = message.split()
    
    # iterate through our words 
    for word in words:
        if sentence_length == 0 and (len(word) >= threshold) or (len(word)+4 > threshold) : 
            res += '...'
            return res
        if len(word) + 4 + sentence_length <= threshold and sentence_length == 0:
            res += ''.join(word) 
        elif len(word) + 4 + sentence_length <= threshold:
            res = res + ' ' + ''.join(word)    
        else:
            res += truncation_string
            return res
        sentence_length += len(word) + 1
    return res 

print(truncateMessage("", 3) == '')
print(truncateMessage("ab", 3) == 'ab')
print(truncateMessage("abc", 3) == 'abc')
print(truncateMessage("abc", 4) == 'abc')
print(truncateMessage("abcd", 4) == 'abcd')
print(truncateMessage("abcd", 3) == '...')
print(truncateMessage("Hello", 4) == '...')
print(truncateMessage("Hello", 5) == 'Hello')
print(truncateMessage("Hello Cat", 8) == '...')
print(truncateMessage("Hello Cat", 9) == 'Hello Cat')
print(truncateMessage("Hello Cat", 5) == '...')
print(truncateMessage("Hello Rufus", 9) == 'Hello ...')
print(truncateMessage("Hello Rufus", 11) == 'Hello Rufus')
print(truncateMessage("Hello Rufus", 12) == 'Hello Rufus')
print(truncateMessage("This is a test message", 3) == '...')
print(truncateMessage("This is a test message", 7) == '...')
print(truncateMessage("This is a test message", 8) == 'This ...')
print(truncateMessage("This is a test message", 10) == 'This ...')
print(truncateMessage("This is a test message", 11) == 'This is ...')
print(truncateMessage("This is a test message", 15) == 'This is a ...')
print(truncateMessage("This is a test message", 20) == 'This is a test ...')
print(truncateMessage("This is a test message", 25) == 'This is a test message')