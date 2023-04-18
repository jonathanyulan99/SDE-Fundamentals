'''
❓ PROMPT
You have a string s that represents a chemical reaction.

The chemical reaction is a string in the following format: molecule (+ molecule)* = molecule (+ molecule)*, \
    where " * " means any non-negative number of repeats. For example, "A = B", "A = B + C", "A + B + C = D + E + F" \
        are chemical reactions but "X + Y = ", "X = + Z" are not.

A molecule is concatenation of an optional coefficient, a string that represents the concatenation of elements, and \
    their optional coefficents. A coefficent is a positive integer that doesn't exceed 1000, and it represents the number\
        of repeats. For example, "Cu12" means 12 repeats of "Cu" element. "3H2O" means 6 repeats of "H" element and 3\
            repeats of "O" elements: 3 is a coefficient of the "H2O" molecule, and 2 is a coefficient of the "H" element.\
                The coefficient of the "O" element is absent, which means this element repeats once in each instance of this\
                    molecule.

An element is a string that starts with an uppercase English letter, while every other symbol is a lowercase English letter.\
    For example, "A" and "Abc" are elements but "FF" and "hello" is not. "FF" actually indicates that there are 2 repeats of \
        the "F" element. A chemical reaction is considered to be balanced if every element has the same number of repeats on\
            both sides of the chemical reaction. Check whether the given chemical reaction is balanced.

Example(s)
For s = "2H2 + O2 = 2H2O", the output should be solution(s) = true. Left side: 4 * "H" and "2 * O".\
    Right side: 4 * "H" and "2 * O".

For s = "1000H2O = Au + Ag", the output should be solution(s) = false. Left side: 2000 * "H" and "1000 * O".\
    Right side: 1 * "Ag" and "1 * Au".
 

🔎 EXPLORE
List your assumptions & discoveries:
    Single Element => 'A' 'B' 'Ab' 
    Seperator between molecules => '+'
    Elements == Elements and num of molecules of that element == num of molecules of the other element
    Output is a boolean 
    Seperator between the molecules is => '='  

📆 PLAN
Outline of algorithm #: 
    s = "2H2 + O2 = 2H20" 
    s1 = "2H2 + O2"
    s2 = "2H2O"
    Use HashMap to Grab Elements and thier counts 
    Front CoEfficient is the multiplier = 2 for s1 
    s1 = "2H2 + O2" 
    list(s1) ==> [2 H 2 + O 2]

🛠️ IMPLEMENT
is_balanced(s: str) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# FIRST ATTEMPT WORKED AT NUMBERS Less than < 10 Trivial Solution 
# Needed to Modulate Code More 
# test = "2H2 + O2 = 2H20"
# # s1 = "2H2 + O2"
# # s2 = ''.join(s1.split('+')).split()
# # print(s2)
# test_string = test.split('=')
# first split the string into its proper parts left_molecule and right_molecule 
# by sting.split('=')
# iterate on the two parts of the s : one being left_molecule and the other being right_molecule 
# use a hashmap to record the frequencies of those counts 
# then we can iterate on the second half and check at the end to see if the key,values are idential 
# no elements in the perodic table are three letters long just 1 or 2 
# def is_balanced(s: str) -> bool:
#     left_right_molecules = s.split('=') 
#     left_side = left_right_molecules[0].strip()
#     right_side = left_right_molecules[1].strip()
#     left_elements = {} 
#     right_elements = {} 
    
#     element_key = ''
#     multiplier = 1
#     for element in left_side: 
#         if element.isdigit() and element_key == '': 
#             multiplier *= int(element) 
#         elif element.isdigit() and element_key != '':
#             value = left_elements.get(element_key,-1) 
#             if value == -1: 
#                 left_elements[element_key] = int(element) * multiplier 
#             else:
#                 left_elements[element_key] += int(element) * multiplier 
#             element_key = ''
#         # if its a letter
#         elif element.isalpha():
#             # if its lowercase then its part of an element 
#             if element.islower(): 
#                 element_key += element 
#                 # once its lower we know we have a key element 
#                 left_elements[element_key] = multiplier 
#             # if its uppercase then its the beginning of an element 
#             elif element.isupper():
#                 element_key = element
#         elif element == '+':
#             multiplier = 1 
#         elif element == ' ' and element_key != '':
#             left_elements[element_key] = multiplier 
#             element_key = ''   
#         elif element.isupper() and element_key != '':
#             left_elements[element_key] = multiplier
#             element_key = element
    
#     if element_key != '':
#         if element_key in left_elements:
#             left_elements[element_key] += multiplier 
#         else:
#             left_elements[element_key] = multiplier
    
#     element_key = ''
#     multiplier = 1
#     for element in right_side: 
#         if element.isdigit() and element_key == '': 
#             multiplier *= int(element) 
#         elif element.isdigit() and element_key != '':
#             value = right_elements.get(element_key,-1) 
#             if value == -1: 
#                 right_elements[element_key] = int(element) * multiplier 
#             else:
#                 right_elements[element_key] += int(element) * multiplier 
#             element_key = ''
#         # if its a letter
#         elif element.isalpha():
#             # if its lowercase then its part of an element 
#             if element.islower(): 
#                 element_key += element 
#                 # once its lower we know we have a key element 
#                 right_elements[element_key] = multiplier 
#             # if its uppercase then its the beginning of an element 
#             elif element.isupper() and element_key == '':
#                 element_key = element
#             elif element.isupper() and element_key != '':
#                 right_elements[element_key] = multiplier 
#                 element_key = element
#         elif element == '+':
#             multiplier = 1 
#         elif element == ' ' and element_key != '':
#             right_elements[element_key] = multiplier 
#             element_key = ''   
            
#     if element_key != '':
#         if element_key in right_elements:
#             right_elements[element_key] += multiplier 
#         else:
#             right_elements[element_key] = multiplier 
            
#     print(left_elements,right_elements)
#     return right_elements == left_elements 

s = "2H2 + O2 = 2H2O"
s1 = "1000H2O = Au + Ag"


# from typing import Dict
# from typing import List 
# this is where they get the upperCase versions of the data types on LeetCode 

def parse_molecule(molecule: str, counts: dict[str, int]) -> dict[str, int]:
    """
    Parse a single molecule string and update a dictionary of element counts.

    Args:
        molecule: A string representing a single molecule.
        counts: A dictionary representing the current element counts.

    Returns:
        A dictionary with updated element counts.
    """
    coefficient = 1
    i = 0
    while i < len(molecule):
        if molecule[i].isdigit():
            digit = ""
            while molecule[i].isdigit():
                digit += molecule[i]
                i += 1
            coefficient = int(digit)
        else:
            element = molecule[i]
            i += 1
            while i < len(molecule) and molecule[i].islower():
                element += molecule[i]
                i += 1
            count = ''
            while i < len(molecule) and molecule[i].isdigit():
                count += molecule[i]
                i += 1
            count = int(count) if count else 1
            count *= coefficient
            counts[element] = counts.get(element, 0) + count
    return counts

def parse_side(side: str) -> dict[str, int]:
    """
    Parse a side of a chemical equation and return a dictionary of element counts.

    Args:
        side: A string representing a side of a chemical equation.

    Returns:
        A dictionary with element counts for the given side.
    """
    molecules = side.replace(" ", "").split('+')
    counts = {}
    for molecule in molecules:
        counts = parse_molecule(molecule, counts)
    return counts

def is_balanced(s: str) -> bool:
    """
    Check if a chemical equation is balanced.

    Args:
        s: A string representing a chemical equation.

    Returns:
        True if the equation is balanced, False otherwise.
    """
    lhs, rhs = s.split('=')
    left_counts = parse_side(lhs)
    right_counts = parse_side(rhs)
    return left_counts == right_counts

print(is_balanced("2H2 + O2 = 2H2O"))
print(is_balanced("1000H2O = Au + Ag")==False)
print(is_balanced("H2O = H2O"))
print(is_balanced("2H2O2 = 2H2O + O2"))
print(is_balanced("NaCl = Na + Cl2")==False)
print(is_balanced("C6H12O6 + 6O2 = 6CO2 + 6H2O"))
print(is_balanced("12H2O = 12H2 + 6O2"))