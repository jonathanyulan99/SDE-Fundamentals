'''
Q: Remove a certain character from the element 
    str = 'bacccad' ans = 'bccd'
    1) pass the 'ans' string in arguement : pass that answer to future recrusive calls, return at the end 
    2) create the answer variable in function body : create a new answer for each function call 
    
                            str = 'baccad'          char = 'a'
                                            baccad 
                                        b/accad                 local_answer/current_string_left 
                                    SKIP the 'a'
                                b/ccad 
                            bc/cad 
                        bcc/ad 
                    bcc/d 
                bccd/{empty} returns the 'bccd' all the way back to the original main function 
'''
# 1st Method 
def remove_character_from_str_1(string: str,char: str)->str: 
    if string: 
        def helper(string,char,answer,start_index):
            if len(string) == start_index:
                return answer 
            
            if string[start_index] != char: 
                answer += string[start_index]
            return helper(string,char,answer,start_index+1)
        if answer:=helper(string,char,'',0):
            return answer 
        else:
            return None 
    else:
        return None 

print(remove_character_from_str_1('baccdah','a'))

# 2nd Method 
def remove_character_from_str_2(string: str,char: str)->str: 
    if string: 
        def helper(string,char,start_index=0):
            if len(string) == start_index: 
                return ''
            
            returning_answers = helper(string,char,start_index+1) 
            
            if string[start_index] == char:
                return returning_answers
            return string[start_index] + returning_answers 
        
        if answer:= helper(string,char): 
            return answer 
    else:
        return string 
    
print(remove_character_from_str_2('baccdah','a'))

def remove_character_from_str_3(string: str,char: str)->str: 
    if string: 
        current_character = string[0]
        
        if current_character != char:
            return current_character + remove_character_from_str_3(string[1:],char) 
        return remove_character_from_str_3(string[1:],char)
    return '' 

print(remove_character_from_str_3('baccdah','b'))


def skip_embedded_string(string:str,skip:str)->None:
    if not string:
        return ''
    if string.startswith(skip): 
        return skip_embedded_string(string[len(skip):],skip)
    return string[0] + skip_embedded_string(string[1:],skip)
    
print(skip_embedded_string('baceceafeapplezds','apple'))

# remember when slicing you are creating a new string object
# you can easily convert this into a more optimal solution by using indices 
def skip_embedded_string_2(string, skip, start_index=0):
    if start_index >= len(string):
        return ''

    skip_length = len(skip)
    substring_length = len(string) - start_index

    if substring_length == 0:
        return ''

    if substring_length < skip_length:
        subsequence = ''
        for i in range(start_index, len(string)):
            subsequence += string[i]
        return subsequence

    for i in range(skip_length):
        if string[start_index + i] != skip[i]:
            if i == 0:
                return string[start_index] + skip_embedded_string_2(string, skip, start_index + 1)
            else:
                return string[start_index] + skip_embedded_string_2(string, skip, start_index + i)

    return skip_embedded_string_2(string, skip, start_index + skip_length)

print(skip_embedded_string_2('baceceafeapplezds', 'apple'))


'''
SubSets & SubSequences: 
    - Combinations & Permutations
    -  SubSets -> Non-Adjacent Collection 
ex: [3,5,9] -> [3],[3,5],[3,9],[3,5,9],[5,3,9],[5,9],[5],[9], []/{empty_set} 
            [3,5] == [5,3] ** These are not two different values 
            
                                    str= 'abc'       return all the SubSets: How do you approach this problem? 
                            ouput: ['a','b','c','ab','ac','bc','abc',''] ** CANNOT CHANGE THE ORDERING, THAT IS PERMTUATIONS!
        Note: That in every output example, it takes certain elements in the input and ignore other elements in the input, this is known as the SUBSET problem 
                                * This pattern of taking some elements and removing them as the Subset Pattern    
                                
                                answer/input        ===     processed_string/unprocessed_string

                                                                   ""/"abc" 
                                            "a"/"bc"                                           ""/"bc"
                                "ab"/"c"                "a"/"c"                  "b"/"c"                    ""/"c"
                        "abc"/{}        "ab"/{}    "ac"/{}     "a"/{}    "bc"/{}         "b"/{}      "c"/{}         ""/{}            
                                                ** Recurrence Relationship {}:empty set **                                                    
'''

def print_subsets(inp:str)->None:
    if input:
        def helper(original,answer):
            if not original and not answer:
                return 
            elif not original and answer:
                print(answer,end=' ')
                return 
            
            helper(original[1:],answer+original[0])
            helper(original[1:],answer)
            
            
        helper(inp,'')
    else:
        return inp 
    
print_subsets('abc')