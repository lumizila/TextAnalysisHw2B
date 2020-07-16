from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy 
import pandas 
import nltk
import collections
import json
import string
import re
import sys
from nltk.corpus import twitter_samples as tw
from nltk import cluster
from nltk.cluster import cosine_distance
from collections import Counter
import matplotlib.pyplot as plt
import gensim
from gensim import corpora
import pyLDAvis.gensim

numpy.set_printoptions(threshold=sys.maxsize)

def preprocesTweets(bigTweets):
	# Creating stopStrings
	# English stopwords defined by the NLTK package.
	stopStrings = nltk.corpus.stopwords.words('english')
	# adding empty string to list of stopStrings
	stopStrings = stopStrings + list("")
	# adding other useless words in the list
	stopStrings = stopStrings + list("ah")

	#reading list of internet jargons
	jargonsJSON = open('interSlangs.json', 'r').read()
	jargons = json.loads(jargonsJSON)
	#adding jargons in lowercase to stopstrings
	for jargon in jargons:
		stopStrings.append(jargon.lower())

	proceTweets = []
	for tweet in range(0,len(bigtweets)):
		#removing digits
		bigtweets[tweet] = re.sub(r'\d+', '', bigtweets[tweet])
		#removing newlines
		bigtweets[tweet] = re.sub(r'\n+', ' ', bigtweets[tweet])
		#removing @
		bigtweets[tweet] = re.sub(r'@', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'£', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'❌😱', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'…', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'👍', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'😂', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'😁', '', bigtweets[tweet])

		#removing punctuations
		for char in string.punctuation:
			bigtweets[tweet] = bigtweets[tweet].replace(char, '');
		#making everything lowercase
		bigtweets[tweet] = bigtweets[tweet].lower()
		#splitting tweets by space		
		proceTweets.append(bigtweets[tweet].split(" "))

	#for each tweet
	for tweet in range(0, len(proceTweets)):
		proceTweets[tweet] = list(filter(None, proceTweets[tweet]))
		for item in stopStrings:
			proceTweets[tweet] = list(filter(lambda a: a != item, proceTweets[tweet]))
				#removing http links
		for word in range(0, len(proceTweets[tweet])):
			if ("http" in proceTweets[tweet][word]):
				proceTweets[tweet].pop(word)
				break;

	return proceTweets

## LOADING DATA
alltweets = tw.strings('tweets.20150430-223406.json')

#removing small tweets (less than 140 chars) because they might be too meaningless to classify 
bigtweets = []
for tweet in alltweets:
	if len(tweet) > 140:
		bigtweets.append(tweet)	

### PREPROSSESSING
tweets = []
#saving without the preprocessing
unchangedTweets = []
unchangedTweets = bigtweets.copy()
tweets = preprocesTweets(bigtweets)

## Now each tweet is a list of strings, I have to create a dictionary
# build the dictionary
dictionary = corpora.Dictionary(tweets)
# construct the corpus
corpus_ = [dictionary.doc2bow(tweet) for tweet in tweets]

nClustersStr = input("---> How many clusters do you want to use? ")
nClusters = int(nClustersStr)

alphaStr = input("---> Which alpha do you want to use? ")
alphaFl = float(alphaStr)

betaStr = input("---> Which beta do you want to use? ")
betaFl = float(betaStr)

minProStr = input("---> Which minimum_probability do you want to use? ")
minProFl = float(minProStr)

ldamodel = gensim.models.ldamodel.LdaModel(corpus=corpus_,
                                           num_topics=nClusters,
                                           id2word=dictionary,
                                           alpha=alphaFl,                 # optional LDA hyperparameter alpha
                                           eta=betaFl,                   # optional LDA hyperparameter beta
                                           minimum_probability=minProFl    # optional the lower bound of the topic/word generative probability
                                          )

#showing all the learned topics
print("the topics were:")
topics = ldamodel.print_topics(num_words=15)

for topic in topics:
    print(topic)

# for each tweet, show the probabilities of topics which beyond the minimum_probability [(topic ID, probability)]
for n,item in enumerate(corpus_[:len(corpus_)]):
    print("tweet ID "+str(n)+":" ,end="")
    print(ldamodel.get_document_topics(item))

for n in range(0,20):
	# nth tweet's topic distribution
	print(ldamodel.get_document_topics(corpus_[n]))

	# show the original tweet
	print(unchangedTweets[n])


#plotting clusters number of elements for analysis
labels = list(list(zip(*topics))[0])
print(labels)
tweetTopics = dict.fromkeys(labels, 0)
corpusSize = len(corpus_)

for cps in corpus_:
	for tp in ldamodel.get_document_topics(cps):
		topic = tp[0]
		tweetTopics[topic] =  tweetTopics[topic] + 1
print(tweetTopics)

values = list(tweetTopics.values())
print(values)
y_pos = numpy.arange(len(labels))
plt.bar(y_pos,values, color = (0.5,0.1,0.5,0.6))
plt.title('Number of topics in total = '+str(nClusters))
plt.xlabel('Topics')
plt.ylabel('Number of tweets with each topic')
plt.ylim(0,400)
plt.xticks(y_pos, labels)
plt.show()