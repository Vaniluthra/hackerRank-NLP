# reference -https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
count_vect = CountVectorizer(lowercase = False, ngram_range = (1,2), max_df=0.95)
tfidf_transformer = TfidfTransformer(use_idf=False) #Count the frequency of words and divide it by total no. of words. deletes most common words like a ,is.

train_data = []            
test_data = []            
train_y = []            # data store for target variables for training, list of A(a)pples

def predict():
    # training set text processing
    X_train_counts = count_vect.fit_transform(train_data)    
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    # training set text processing
    X_new_counts = count_vect.transform(test_data)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    # initializing model
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB()  #94

    # model fitting
    clf = clf.fit(X_train_tfidf, train_y)

    # predicting answers for test set
    predicted = clf.predict(X_new_tfidf)
    for results in predicted: 
        print(results)

# reading trainig data from text files
for line in open('apple-computers.txt'):
    if len(line.strip())>0:                #skip empty lines
        train_data.append(line.strip().strip('. '))
        train_y.append('computer-company')
for line in open('apple-fruit.txt'):
    if len(line.strip())>0:                #skip empty lines
        train_data.append(line.strip('. '))
        train_y.append('fruit')

N = int(input())
for n in range(N):
    inp = input()
    test_data.append(inp)

predict()