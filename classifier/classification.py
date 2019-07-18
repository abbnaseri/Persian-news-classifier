import numpy as np
import pandas as pd
import os
import re
from sklearn.datasets import load_files
import nltk
import pickle
from hazm import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import codecs


class PersianClassifier():
    # intializing an object
    def __init__(self):
        self.name = "text-classifier"
        self.report = ''
        self.accuracy = ''
    # method for checking if a value is float or not
    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    # the classifier method
    def run(self):
        # loading data from the directory
        per_data = load_files(r"classifier/isna-dataset", encoding='UTF-8')
        # assigning the data and label to x and y 
        x, y = per_data.data, per_data.target
        documents = []
        # reading stop word list from the file
        newstop = [w for w in codecs.open('classifier/persian', encoding='utf-8').read().split('\n') if w]
        # normalizing texts
        for sen in range(0, len(x)):
            sample = str(x[sen])
            asen = sent_tokenize(sample)
            # deleting the last sentence
            del asen[-1]
            sample = '\n'.join(asen)
            a = list(word_tokenize(sample))
            tokens = []
            # deleting stopwords
            for word in a:
                if not (word.isdigit() or self.isfloat(word) or len(word)<2 or (word in newstop)):
                    tokens.append(word)
            tokens = ' '.join(tokens)
            documents.append(tokens)
        # getting the current directory for exporting normalized text to csv
        path1 = os.getcwd()
        # merging normalized texts with labels
        df = pd.DataFrame(documents, index=y)
        # exporting to csv
        df.to_csv(r'' + path1 + '/' + 'data.csv')
        # creating an object from CountVectorizer class that extact 1500 features from text. for this to be done only words which occured in at least 5 documnets and 70 percent of doucments are going to be selected
        vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7)
        # using the fit method for extracting features
        x = vectorizer.fit_transform(documents).toarray()
        # creating an object from TfidfTransformer()  
        tfidfconverter = TfidfTransformer()
        # evaluating Tfidf value of texts
        x = tfidfconverter.fit_transform(x).toarray()
        # seprating train data and test data in which 80 percent is for training and the rest of it is for test
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
        # creating an object from RandomForestClassifier class which is the implementation of this algorithm.
        classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
        # training the object with fit method
        classifier.fit(X_train, y_train)
        # testing the classifier model
        y_pred = classifier.predict(X_test)
        # saving report of model's accuracy
        self.report = classification_report(y_test,y_pred)
        self.accuracy = accuracy_score(y_test, y_pred)
        # saving model into a pickle file
        with open('bbcnews_classifier', 'wb') as picklefile:
            pickle.dump(classifier, picklefile)
        # printing the report
        print(self.report)
        print(self.accuracy)
        




