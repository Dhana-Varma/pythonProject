# python programme to compute all the permutation of the string

def get_getpermutation(string,i=0):
    if i==len(string):
        print("").join (string))
    for j in range(i,;len(strin)):
         words=[c for c in string]
         words[i],words[j]=words[j],words[j],words[i]
         get_permutation(words, i + 1)
get_permutation('run')
