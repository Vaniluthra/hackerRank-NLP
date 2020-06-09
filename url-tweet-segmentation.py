#https://scotch.io/tutorials/an-introduction-to-regex-in-python
#import re
#from wordsegment import load, segment
#def seg(text):
#    a=re.split('\s|(?<!\d)[,.](?!\d)', text)   #remove special symbols, numbers and split it
#    splitwords = ["www","com","in","#"]      # remove the words which is in the list
#    a ="".join([each for each in a if each not in splitwords])
#    load()
#    print(str(segment(a)))
#seg('#isittime')
#https://github.com/narendraprasath/Word-Segmentation-in-NLP-Python/blob/master/Segmentation.py
from __future__ import with_statement #with statement for reading file
import re   # Regular expression

words = []  #  corpus file words
testword = []   # test words   
ans = []    # words matches with corpus

# Reading the corpus
with open('words.txt', 'r') as f:
    lines = f.readlines()
    words =[(e.strip()) for e in lines]

a=re.split('\s|(?<!\d)[,.](?!\d)', text)
splitwords = ["www","com","in","#"]      # remove the words which is containg in the list
a ="".join([each for each in a if each not in splitwords])

for each in a:
    testword.append(each)   #test word 
test_lenth = len(testword)       # lenth of the test data

def Seg(a,lenth):
    ans =[]
    for k in range(0,lenth+1):  # this loop checks char by char in the corpus
        
        if a[0:k] in words:
            print(a[0:k],"-appears in the corpus")
            ans.append(a[0:k])   
            break
    if ans != []:
        g = max(ans,key=len)
        return g

def out(a):
    test_tot_itr = 0    #each iteration value
    answer = []     # Store the each word contains the corpus
    Score = 0   # initial value for score
    N = 37    # total no of corpus
    M = 0
    C = 0
    while test_tot_itr < test_lenth:    
        ans_words = Seg(a,test_lenth)
        if ans_words != 0:
            test_itr = len(ans_words)
            answer.append(ans_words)
            a = a[test_itr:test_lenth]
            test_tot_itr += test_itr

    Aft_Seg = " ".join([each for each in answer]
    print(Aft_Seg)  # print After segmentation the input 