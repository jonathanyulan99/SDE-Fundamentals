def print_all_subsequences(word,subseq,i):
    if len(word) == i:
        print('\"'+subseq+'\"')
        return 
    print_all_subsequences(word,subseq+word[i],i+1)
    print_all_subsequences(word,subseq,i+1)

print_all_subsequences("ABCD","",0)

'''










'''