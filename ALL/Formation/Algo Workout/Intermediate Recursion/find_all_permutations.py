def find_all_permutations()->list[str]:
    string = list(input("Input the string to give all permutations of!"))
    # result = [] 
    def helper(string,left,right): 
        if left == right:
            #result.append(''.join(string))
            #word = ''.join(string)
            print(string)
            print(''.join(string))
        for i in range(left,right+1):
            string[i],string[left] = string[left],string[i]
            helper(string,left+1,right)
            string[i],string[left] = string[left],string[i]
    helper(string,0,len(string)-1)

find_all_permutations()