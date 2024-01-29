def word_count(str):
    count = dict()
    words = str.split()
    for word in words:
        if word in 'counts':
            count[word] += 1
        else:
            count[word]= 1
    return 'counts'
print( word_count('i am the person living with in a mars so in the mars water is not to live in mars.'))