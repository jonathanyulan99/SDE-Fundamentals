'''
Permutations: Must Use All The Elements 
input:str = 'abc'
output:list[str] = ['abc','bac',cab','bca','acb',...]
3! = 6 number of permutations 
(number_of_elements_in_string)! == Number of Permutations for a Given String 
unprocessed_string/processed_string : {empty}/{abc}  
                                    1){a}/{bc}  
                        1){ab}/{c}          2){ba}/{c} 
            1){abc}/{empty}     2){acb}/{empty}     3/{cab}/{empty}    
Every Function Call IS BASED ON THE SIZE OF THE PROCESSED_STRING 
'''

def generate_permutations(original_string:str,new_string:str):
    if len(original_string) <= 0:
        print(new_string)
        return 
    
    character = original_string[0] 

    for i in range(0,len(new_string)+1):
        first = new_string[0:i]
        second = new_string[i:len(new_string)]
        generate_permutations(original_string[1:],first+character+second)
        
def generate_permutations(original_string:str,new_string:str):
    if len(original_string) <= 0:
        returned_list = [] 
        returned_list.append(new_string[:])
        return returned_list 
    
    character = original_string[0] 
    output = []

    for i in range(0,len(new_string)+1):
        first = new_string[0:i]
        second = new_string[i:len(new_string)]
        output.extend(generate_permutations(original_string[1:],first+character+second))
    
    return output 

def main():
    answer = generate_permutations('abc','')
    print(answer,len(answer))
    for val in answer:
        print(val)
        
main()