from textblob import _text
from textblob import TextBlob
import pandas as pd


data = pd.read_csv('C:/Users/athanasis/Desktop/Semester_B/NLP/twitter-2016test-A-clean.tsv', sep='\t', header=0)
sentences = data.iloc[:,2]

for sent in sentences:
       blob_sent = TextBlob(sent)
       print(blob_sent.sentiment.polarity)
       # if blob_sent.sentiment.polarity > 0:

#
# print(blob.tags)
# print(blob.noun_phrases)
#
# for sentence in blob.sentences:
#     print(sentence.sentiment.polarity)