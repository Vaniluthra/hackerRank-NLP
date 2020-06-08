import sys
from collections import Counter
from functools import reduce
from operator import iconcat

def Trigrams(sentence):
    words = sentence.split()
    return [" ".join(words[i:i+3]) for i in range(len(words)-2)]

if __name__ == '__main__':
    text = sys.stdin.read().lower().split('.') #finish the input by enter and Ctrl+D
    trigrams = Counter(reduce(iconcat, map(Trigrams, text), []))
    print(trigrams)
    print(max(trigrams, key = trigrams.get))