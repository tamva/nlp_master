import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown
import collections
import re
from nltk.probability import FreqDist
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# ======> 1 <=======
file = open("./viruses1200135v2.txt", "r", encoding='utf-8')
raw = file.read()
type(raw)
tokens = word_tokenize(raw)
print(len(tokens))  # word count

punctuation = re.compile(r'[.?!,:;()[]|0-9]')
post_punc = []


def vocab(raw):
    vocab = set([words.lower() for words in raw])
    print
    return len(vocab)


print('The vocabulary is', vocab(raw))

# text = nltk.Text(tokens)
# print(len(text))


# =======> 2 <=======
# sents = nltk.corpus.brown.sents()
sentences = nltk.sent_tokenize(raw)
print("Sentences Number",len(sentences))


# ======> 3 <========
print('Lexical Diversity', len(raw)/ vocab(raw))

# ======> 5 <========
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import re

freq = FreqDist()
for word in tokens:
    freq[word.lower()] += 1

top10 = freq.most_common(10)  # before stop words
print(top10)

stop_words = set(stopwords.words('english'))
filtered = [wo for wo in tokens if not wo in stop_words]
len(filtered)

punctuation = re.compile(r'[.?!,:;()/[]|0-9]')
post_punc = []
for words in filtered:
    word = punctuation.sub("", words)
    if len(word) > 0:
        post_punc.append(word)

freq_filt = FreqDist()
for word in post_punc:
    freq_filt[word.lower()] += 1

top10_filter = freq_filt.most_common(10)
print('==========after================\n===============================')
print(top10_filter)




# =======> 6 <===========
allparts = []
for word in post_punc:
    part = nltk.pos_tag([word])
    allparts.append(part)

# print(allparts.most_common(5)[0][0])
# pos_tags = {word: allparts[word].most_common(5)[0][0] for word in allparts}

# print(allparts)


pos_list = nltk.pos_tag(post_punc)
# print(pos_list)
pos_counts = collections.Counter((subl[1] for subl in pos_list))
print ("the five most common tags are", pos_counts.most_common(5))

for nn in pos_list:
    if nn == '':
        x =1



nouns = 0
for k in allparts:
    if k[0][1] == 'NN':
        nouns = nouns + 1
print("Question 6 Number of nouns:",nouns)