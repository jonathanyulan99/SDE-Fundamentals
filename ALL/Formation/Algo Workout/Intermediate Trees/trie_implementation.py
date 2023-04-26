class Node(object):
    def __init__(self,letter,isEndOfWord=False):
        # the actual letter of a word
        self.letter = letter
        # the children or the letters attached to our beginning or before-letter 
        self.children = set() 
        # our boolean flag to note that the letter we are looking at is a specific end of a word 
        self.isEndOfWord = isEndOfWord 
    

beginning = Node('')
a = Node('a')
p = Node('p')
p2 = Node('p')
l = Node('l')
e = Node('e')


# inserting 'apple'
beginning.children.add(a)
a.children.add(p)
p.children.add(p2)
p2.children.add(l)
l.children.add(e)
e.isEndOfWord = True


# inserting 'apples'
s = Node('s')
e.children.add(s)
s.isEndOfWord = True


w,i,t,h,o,u,t2 = Node('w'),Node('i'),Node('t'),Node('h'),Node('o'),Node('u'),Node('t')
i2,n = Node('i'),Node('n')


# inserting 'with'
beginning.children.add(w)
w.children.add(i)
i.children.add(t)
t.children.add(h)
h.isEndOfWord = True


# inserting 'without'
h.children.add(o)
o.children.add(u)
u.children.add(t2)
t2.isEndOfWord = True


# inserting 'within'
h.children.add(i2)
i2.children.add(n)
n.isEndOfWord = True

class TrieNode(object):
    def __init__(self,letter,isEndOfWord=False):
        self.letter = letter 
        self.children = set() 
        self.isEndOfWord = isEndOfWord 

def find_words(root:Node)->list[str]:
    result = [] 
    def helper(root,_string):
        if not root:
            return 

        if root.isEndOfWord: 
            result.append(_string+root.letter)
        
        for _child in root.children:
            helper(_child,_string+root.letter) 
    
    helper(root,'')
    return result 

print(find_words(beginning))

# method to insert a whole word into the trie 
def insert_word(root,desired_word):
    if len(desired_word) == 0:
        return 
    
    idx = 0 
    curr = root
    
    while idx < len(desired_word):
        chr_desired_word = desired_word[idx]
        letter_node = get_node_letter(root,chr_desired_word)
        # if we dont have a letter_node 
        if not letter_node: 
            new_letter_node = Node(chr_desired_word) 
            curr.children.add(new_letter_node) 
            curr = new_letter_node
        else:
            curr = letter_node 
        idx += 1 

    # end of the while loop means the end of the desired_word being inserted 
    # set the flag 
    curr.isEndOfWord = True 
    print(f'{desired_word} has been inserted into Trie')
    
def get_node_letter(root,chr_desired_word):
    for child in root.children:
        if child.letter == chr_desired_word:
            return child 
        
beginning = Node('')
print("Inserting words into the trie.")
insert_word(beginning, "apple")
insert_word(beginning, "martini")
insert_word(beginning, "butter")
insert_word(beginning, "buttermilk")
insert_word(beginning, "button")
insert_word(beginning, "buttocks")
insert_word(beginning, "apples")
print('\n')



def find_words_2(root:Node)->list[str]: 
    result = [] 
    def helper(root,_string):
        if not root:
            return 
        
        if root.isEndOfWord:
            result.append(_string + root.letter)
        
        for child in root.children: 
            helper(child,_string + root.letter)
    helper(root,'')
    return result 

print("Searching for programmatically inserted words in the trie.")
print(find_words_2(beginning))

def contains_word(root,checked_word):
    if not root or not checked_word:
        return False 
    if len(checked_word)==0:
        return True 
    
    def helper(root,checked_word,idx):
        if idx == len(checked_word):
            return root.isEndOfWord 
        
        for child in root.children:
            if checked_word[idx] == child.letter:
                return helper(child,checked_word,idx+1)
        
        return False 
    
    return helper(root,checked_word,0)


print("The following results should all print 'True'")
print(contains_word(beginning, "apple") == True)
print(contains_word(beginning, "apples") == True)
print(contains_word(beginning, "appl") == False)
print(contains_word(beginning, "appless") == False)
print(contains_word(beginning, "appletini") == False)
