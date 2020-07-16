# TextAnalysisHw2B

# This is the report of the Text Analysis class' "Assignment 2B"

This assignment was to develop a program satisfying the following requirements:
- Using 100 or more documents used in Assignment 2A (for reference: https://github.com/lumizila/TextAnalysisHw2A )
- Using LDA

  ### 1. Summary of the dataset
  
  For this assignment I decided to use the twitter_samples dataset from the NLTK.corpus. (More about it can be seen at http://www.nltk.org/howto/twitter.html )
  The twitter_samples data is actually divided into 3 files, so I chose "tweets.20150430-223406.json" because it is the one with the biggest number of tweets.
  I considered one tweet to be one "document" to be analyzed. 
  
  #### 1.1 Preprocessing 
    
   The original "tweets.20150430-223406.json" file comes with 20,000 tweets. However, many of them are very short which would make them hard to cluster. 
   Therefore I decided to exclude the tweets smaller than 140 characthers, which left me with 857 tweets. 
    
   Next I removed newlines (in exchange for spaces), numbers, punctuations, urls and some emojis from the texts.  
    
   I created a list of "stopWords" using NLTK stopwords for english as well as common internet jargons that you can find in the file "interSlangs.json", which were scraped from https://www.netlingo.com/acronyms.php  
    
   Next I split the tweets in words, and moved all the words that match one of the words in the "stopWords" list. Everything left was transformed to lowercase. 
  
  ### 2. Comparing the clustering results with different parameter k 
  
  The code I wrote gives the user the opportunity to choose different values for: alpha, beta, minimum probability and number of topics (k clusters). Firstly I decided to keep everything the same except for the number of topics (k clusters). Therefore for this section 2, the values remaining the same are: alpha = 0.1; beta = 0.1; minimum probability = 0.5. 
  And I ran the code with 3 different values for k: 5, 10, 15
  My results of the clustering as well as discussion of differences for each k are discussed on the topics below. 
  
  #### 2.1 Describing the results for each k.
  
  As mentioned before, I considered each tweet to be one document, so each cluster will contain multiple tweets. 
  
  #### For K = 5
  
  
  #### For K = 10
  
  
  #### For K = 15
  
  
  #### 2.2 Discuss the differences for each k. 
  
  ### 3. Changing values for alpha, beta and minimum probability.
  
  ### 4. Consideration
  
  The same consideration made on the Assignment 2A, this dataset has a problem in that many tweets are retweets with most of the text being the same between the original tweet and the retweets. In the future I should also filter the retweets and test the clustering methods again.  
  
  ### 5. Source code on GitHub: https://github.com/lumizila/TextAnalysisHw2B
  
