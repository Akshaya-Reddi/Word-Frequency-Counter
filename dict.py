def count_text(text):
    words = text.lower().split()
    dict = {}

    for word in words:
        dict[word] = dict.get(word,0) + 1
    
    return dict

sentence = input("Enter sentence: ")

count_words = count_text(sentence)
print(count_words)

"""
from collections import Counter
sentence = input("Enter sentence: ")
count_words = Counter(sentence.lower().split())
print(count_words)

"""