# Depression-Sentiment-Analysis-with-Twitter-Data
Sentiment Analysis using Python, Twitter API and Hive

# Steps 
Step1: Get twitter sentiments for keywords – depression, anxiety, mental health.

Step2: Store twitter sentiments in a text file, Collected for an hour. Got 3500 tweets.

Step3: Install and setup Hadoop and Hive. Once setup create a table to store the necessary tweet details. Use Jsonserde to convert the JSON format according to our tables.

Step4: Create a table called tweets_raw table containing the records as received from Twitter.

Step5: Load the time zone file and the dictionary file to the Hadoop file system (hdfs).

Step6: The time zone file contains the time zone and the associated country.

Step7: The dictionary contains words with their polarity. Each word taken from the tweet is compared with the dictionary and given a score.

Step8: the sum of polarity is added for each tweet and of it is above 0, then it is a positive tweet. If it is equal to 0 it is neutral and if lesser than 0 it is a negative tweet.

Step9: By this way tweets are classified as positive or negative.

Step10. Stores as an excel file and fed to python. Here using Naive Bayes classifier to classify tweets as positive or negative and also see the efficiency of the algorithm. The algorithm ran on the test set and were able to get a 95% accuracy in predicting positive and negative tweets.
