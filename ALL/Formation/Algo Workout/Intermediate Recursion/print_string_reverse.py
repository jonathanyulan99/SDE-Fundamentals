def print_reverse_recursively(s:str)->None:
    if s:
        def helper(string,start):
            if start >= len(string) or string is None:
                return 
            
            helper(string,start+1)
            print(string[start],start)
        helper(s,0)

print_reverse_recursively("OLLEH")
print()
print_reverse_recursively("HELLO")