from textblob import _text
from textblob import TextBlob
import pandas as pd
import numpy as np
from sklearn import metrics


data = pd.read_csv('twitter-2016test-A-clean.tsv', sep='\t')
df = pd.DataFrame(data)

polar_tab = []

for sent in df['text']:
       blob_sent = TextBlob(sent)
       pol_value = blob_sent.sentiment.polarity
       polar_tab.append(pol_value)


# df['pred_sent'] = polar_tab
polar = np.array(polar_tab)
df['values'] = polar
three_polars = pd.cut(polar,3, labels=["negative", "neutral", "positive"])
print(three_polars)
df['pred_sent'] = three_polars
print(df)

print("////Before extensive search/////")
print("Accuracy of the prediction",metrics.accuracy_score(df['sentiment'],df['pred_sent']))
print("Precision of the prediction",metrics.precision_score(df['sentiment'],df['pred_sent'],average=None))
print("Recall of the prediction",metrics.recall_score(df['sentiment'],df['pred_sent'],average=None))
print("F-Score of the prediction",metrics.f1_score(df['sentiment'],df['pred_sent'],average=None))

print(metrics.confusion_matrix(df['sentiment'],df['pred_sent']))

best_neg = 0
best_pos = 0
best_acc = 0
new_polar = []
best_column = []


for max_neg in np.arange(-0.400,-0.300,0.005):

       for max_pos in np.arange(0.300, 0.400, 0.005):

              for value in df['values']:
                     if value > max_pos:
                            new_polar.append('positive')
                     elif value < max_neg:
                            new_polar.append('negative')
                     else:
                            new_polar.append('neutral')
              df['new_polar'] = np.array(new_polar)
              # print(df['new_polar'])
              new_polar.clear()
              if (metrics.accuracy_score(df['sentiment'],df['new_polar'])) > best_acc:
                     best_neg = max_neg
                     best_pos = max_pos
                     best_acc = metrics.accuracy_score(df['sentiment'],df['new_polar'])
                     best_precision = metrics.precision_score(df['sentiment'], df['new_polar'], average=None)
                     best_recall = metrics.recall_score(df['sentiment'], df['new_polar'], average=None)
                     best_fscore = metrics.f1_score(df['sentiment'], df['new_polar'], average=None)
                     best_column = df['new_polar'].tolist()
              del df['new_polar']

df['new_polar'] = np.array(best_column)
print("///// After the search //////")
print("The best accuracy after the extensive search",best_acc)
print("Best negative thresholf",best_neg)
print("Best positive thresholf",best_pos)
print("Best Precision of the prediction",metrics.precision_score(df['sentiment'],df['new_polar'],average=None))
print("Best Recall of the prediction",metrics.recall_score(df['sentiment'],df['new_polar'],average=None))
print("Best F-Score of the prediction",metrics.f1_score(df['sentiment'],df['new_polar'],average=None))


print(metrics.confusion_matrix(df['sentiment'],df['new_polar']))