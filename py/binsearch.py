# binsearch.py
# Kaufman Rachel
# CSCI 77800 Fall 2022
# collaborators: none
# consulted: students of mine

def binary_search(target_word, word_list):
    #low
    a = 0
    #high
    b = len(word_list)
    count = 0

    while a < b: 
        middle = (a + b)//2
        if word_list[middle] < target_word:
            a = middle + 1
        else:
            #middle becomes max
            b = middle
        count += 1
    if a < len(word_list) and word_list[a] == target_word:
        #return a
        return count 
    else: 
        return -1
