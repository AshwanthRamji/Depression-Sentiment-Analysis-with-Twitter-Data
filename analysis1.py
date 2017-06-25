# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 19:43:52 2017

@author: ashwa
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'depression', 'anxiety', 'mental health'
    stream.filter(track=['Depression', 'Anxiety', 'mental health'])
    
import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'tweetdata.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
    
print (len(tweets_data))
'''
tweets = pd.DataFrame()

tweets['id'] = map(lambda tweet: tweet.get('id', None),tweets_data)
tweets['text'] = map(lambda tweet: tweet.get('text', None),tweets_data)

print(tweets.head())
print(tweets)
'''
sent = pd.read_excel('sentiment2.xlsx')
print(sent.head())
print(sent['id'])
print(len(sent))

x = []
y = []
for i in range(len(tweets_data)):
    if tweets_data[i]['id']==sent['id'][i]:
        x.append(tweets_data[i]['text'])
        y.append(sent['sentiment'][i])
print(x[0].split(" "))
print(y[0])
'''
for i in range(len(x)):
    x[i] = x[i].split(" ")
print(x[0])
print(x)
'''
            
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

vectorizer = CountVectorizer(stop_words='english')
train_features = vectorizer.fit_transform(x)

actual = y[:-500]



nb = MultinomialNB()
nb.fit(train_features, [int(r) for r in y])

test_features = vectorizer.transform(x[:-500])

test_try= vectorizer.transform(["Can we all stop treating anxiety like it's a choice and something cool to have thank you"])
test_try2= vectorizer.transform(["I want to die depression sucks"])
predict2 = nb.predict(test_try)
predict3 = nb.predict(test_try2)

#print(predict2)
predictions = nb.predict(test_features)

print()

fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
print("Multinomial naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))

print(predict2)
print(predict3)


