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
  
  Below you can see the bar graph showing how many tweets were found to have each topic (tweets might have more than one topic) for K=5. 
  
  ![GitHub Logo](/K5.png)
  
  For this number of topics, the topics found were: 
 
  ```
  (0, '0.017*"miliband" + 0.015*"ukip" + 0.015*"labour" + 0.013*"farage" + 0.011*"bbcpolitics" + 0.010*"says" + 0.010*"nigel" + 0.010*"candidate" + 0.009*"bbcqt" + 0.009*"much" + 0.009*"tories" + 0.008*"racist" + 0.008*"stupid" + 0.008*"know" + 0.008*"doesnt"')
  (1, '0.020*"snp" + 0.014*"ukip" + 0.014*"cameron" + 0.014*"miliband" + 0.013*"tory" + 0.013*"tories" + 0.011*"mr" + 0.010*"labour" + 0.009*"bbcqt" + 0.008*"deal" + 0.008*"audience" + 0.008*"clegg" + 0.007*"vote" + 0.007*"geezajay" + 0.006*"sturgeon"')
  (2, '0.038*"snp" + 0.025*"labour" + 0.017*"miliband" + 0.016*"vote" + 0.015*"tories" + 0.013*"bbcqt" + 0.010*"tory" + 0.009*"must" + 0.009*"clear" + 0.008*"government" + 0.008*"jimforscotland" + 0.007*"called" + 0.007*"bluff" + 0.007*"scotland" + 0.007*"fm"')
  (3, '0.029*"tories" + 0.021*"miliband" + 0.020*"snp" + 0.018*"labour" + 0.014*"vote" + 0.011*"rule" + 0.010*"let" + 0.008*"bbcqt" + 0.008*"looks" + 0.008*"could" + 0.008*"lab" + 0.007*"close" + 0.007*"saying" + 0.007*"eng" + 0.007*"aside"')
  (4, '0.020*"snp" + 0.018*"labour" + 0.012*"farage" + 0.009*"miliband" + 0.008*"doesnt" + 0.007*"people" + 0.007*"tories" + 0.007*"tory" + 0.007*"uk" + 0.006*"debt" + 0.006*"cant" + 0.005*"bbcqt" + 0.005*"power" + 0.005*"would" + 0.005*"cchqpress"')
  ```
  
  Some examples of tweets and their respective topics:
  
  ```
  [(1, 0.9703656)]
  RT @KatieKhaleesi: I'm #SNPbecause in my entire adult life I've only seen Labour &amp; Tories cause misery, war, and further victimisation of t…
  [(1, 0.97036767)]
  RT @joncraig: Scottish audience all address Sturgeon as "Nicola". Earlier on QT it was "Mr Cameron", "Mr Miliband" &amp; "Mr Clegg". http://t.c…
  [(4, 0.9741846)]
  Couldn't watch the leaders Q&amp;As tonight as I was at a scholarship dinner, but at said dinner I argued Labour doesn't need nor want the SNP
  [(2, 0.9703678)]
  RT @JimForScotland: Labour has called SNP bluff. The SNP must now be clear: are they willing to prevent or bring down a Labour government &amp;…
  [(2, 0.97036684)]
  RT @MichaelH14: Ed Miliband : it wasn't the spending on teachers &amp; nurses in Britain that crashed the global economy. 'Bout time someone sa…
  [(3, 0.9771292)]
  RT @WelshConserv: We've come a long way in 5yrs. Don't let EdM &amp; SNP drag us back to square one. Let's keep going #SecureTheRecovery https:…
  [(3, 0.9652099)]
  ```
  
  #### For K = 10
  
  Below you can see the bar graph showing how many tweets were found to have each topic (tweets might have more than one topic) for K=10. 
  
  ![GitHub Logo](/K10.png)
  
   For this number of topics, the topics found were: 
   
   ```
  (0, '0.030*"labour" + 0.028*"snp" + 0.012*"bbcpolitics" + 0.011*"tories" + 0.010*"nigel" + 0.010*"bring" + 0.010*"government" + 0.010*"jimforscotland" + 0.010*"says" + 0.009*"must" + 0.009*"called" + 0.009*"willing" + 0.009*"bluff" + 0.009*"clear" + 0.009*"prevent"')
  (1, '0.023*"tories" + 0.017*"snp" + 0.017*"labour" + 0.010*"tory" + 0.010*"pressure" + 0.009*"thesnp" + 0.009*"doesnt" + 0.009*"know" + 0.009*"edmilibands" + 0.009*"given" + 0.009*"distancing" + 0.009*"wholly" + 0.009*"went" + 0.009*"kevinjpringle" + 0.009*"far"')
  (2, '0.027*"miliband" + 0.021*"snp" + 0.020*"bbcqt" + 0.017*"tories" + 0.015*"labour" + 0.011*"cameron" + 0.009*"uk" + 0.008*"nhs" + 0.007*"benefit" + 0.007*"vote" + 0.006*"politics" + 0.006*"say" + 0.006*"across" + 0.006*"strongly" + 0.006*"farage"')
  (3, '0.025*"tories" + 0.016*"ukip" + 0.011*"labour" + 0.011*"bbcqt" + 0.010*"tory" + 0.008*"vote" + 0.008*"bbc" + 0.007*"common" + 0.007*"nigel" + 0.007*"sense" + 0.006*"farage" + 0.006*"people" + 0.006*"snp" + 0.006*"geezajay" + 0.005*"miliband"')
  (4, '0.031*"snp" + 0.024*"labour" + 0.018*"miliband" + 0.016*"mr" + 0.013*"cameron" + 0.012*"deal" + 0.011*"fm" + 0.010*"would" + 0.010*"clegg" + 0.009*"nicola" + 0.009*"much" + 0.009*"tories" + 0.008*"sturgeon" + 0.008*"audience" + 0.007*"scottish"')
  (5, '0.021*"ukip" + 0.016*"tory" + 0.015*"snp" + 0.012*"bbcqt" + 0.012*"people" + 0.011*"miliband" + 0.009*"labour" + 0.008*"nobody" + 0.008*"willblackwriter" + 0.008*"tripped" + 0.008*"trips" + 0.008*"t̶r̶i̶p̶s̶" + 0.008*"mocks" + 0.008*"hes" + 0.008*"̶o̶u̶t̶"')
  (6, '0.033*"vote" + 0.031*"snp" + 0.020*"labour" + 0.016*"tories" + 0.015*"sorry" + 0.013*"back" + 0.013*"tory" + 0.012*"youll" + 0.012*"huff" + 0.012*"indyfortheguy" + 0.012*"sulk" + 0.012*"go" + 0.012*"get" + 0.011*"miliband" + 0.008*"much"')
  (7, '0.032*"miliband" + 0.020*"let" + 0.019*"tories" + 0.019*"looks" + 0.019*"could" + 0.017*"eng" + 0.017*"rathe" + 0.017*"saying" + 0.017*"aside" + 0.017*"well" + 0.017*"stand" + 0.017*"lab" + 0.017*"irvinewelsh" + 0.017*"rule" + 0.017*"close"')
  (8, '0.024*"snp" + 0.017*"bbcqt" + 0.016*"vote" + 0.014*"strongly" + 0.013*"say" + 0.013*"whats" + 0.011*"matter" + 0.011*"scotnight" + 0.011*"scotlandtonight" + 0.011*"exclude" + 0.011*"reaction" + 0.011*"traquir" + 0.011*"told" + 0.011*"scots" + 0.011*"toryamplab"')
  (9, '0.028*"snp" + 0.018*"miliband" + 0.016*"tories" + 0.015*"vote" + 0.014*"labour" + 0.011*"must" + 0.009*"tory" + 0.007*"deal" + 0.007*"nicola" + 0.006*"liar" + 0.006*"cowardampa" + 0.006*"gain" + 0.006*"admits" + 0.006*"blunkett" + 0.006*"sturgeons"')
   ```
  
  Some examples of tweets and their respective topics:
  
  ```
  [(0, 0.93570626)]
  RT @KatieKhaleesi: I'm #SNPbecause in my entire adult life I've only seen Labour &amp; Tories cause misery, war, and further victimisation of t…
  [(4, 0.9357106)]
  RT @joncraig: Scottish audience all address Sturgeon as "Nicola". Earlier on QT it was "Mr Cameron", "Mr Miliband" &amp; "Mr Clegg". http://t.c…
  [(2, 0.94373)]
  Couldn't watch the leaders Q&amp;As tonight as I was at a scholarship dinner, but at said dinner I argued Labour doesn't need nor want the SNP
  [(0, 0.9357074)]
  RT @JimForScotland: Labour has called SNP bluff. The SNP must now be clear: are they willing to prevent or bring down a Labour government &amp;…
  [(7, 0.9357119)]
  RT @MichaelH14: Ed Miliband : it wasn't the spending on teachers &amp; nurses in Britain that crashed the global economy. 'Bout time someone sa…
  [(4, 0.9499749)]
  RT @WelshConserv: We've come a long way in 5yrs. Don't let EdM &amp; SNP drag us back to square one. Let's keep going #SecureTheRecovery https:…
  ```
  
  #### For K = 15
  
  Below you can see the bar graph showing how many tweets were found to have each topic (tweets might have more than one topic) for K=15. 

  ![GitHub Logo](/K15.png)
  
  For this number of topics, the topics found were: 
  
  ```
  the topics were:
  (0, '0.030*"tories" + 0.025*"saying" + 0.025*"miliband" + 0.024*"let" + 0.023*"lab" + 0.022*"rule" + 0.021*"well" + 0.021*"rathe" + 0.021*"activists" + 0.021*"aside" + 0.021*"eng" + 0.021*"looks" + 0.021*"irvinewelsh" + 0.021*"close" + 0.021*"stand"')
  (1, '0.019*"labour" + 0.018*"tories" + 0.015*"miliband" + 0.013*"tory" + 0.011*"cameron" + 0.011*"britain" + 0.010*"thesnp" + 0.010*"went" + 0.009*"pressure" + 0.008*"far" + 0.008*"given" + 0.008*"wholly" + 0.008*"edmilibands" + 0.008*"kevinjpringle" + 0.008*"distancing"')
  (2, '0.030*"snp" + 0.022*"tory" + 0.020*"labour" + 0.011*"tories" + 0.009*"bbcqt" + 0.007*"nicola" + 0.007*"need" + 0.007*"westviews" + 0.006*"cant" + 0.006*"disguise" + 0.006*"campbell" + 0.006*"dislike" + 0.006*"national" + 0.006*"mps" + 0.006*"bbcs"')
  (3, '0.035*"snp" + 0.021*"labour" + 0.012*"bbcqt" + 0.012*"tories" + 0.011*"government" + 0.009*"clear" + 0.009*"miliband" + 0.008*"bring" + 0.007*"uk" + 0.007*"agree" + 0.007*"politics" + 0.007*"luck" + 0.007*"must" + 0.007*"willing" + 0.007*"prevent"')
  (4, '0.032*"snp" + 0.021*"deal" + 0.016*"labour" + 0.010*"cameron" + 0.010*"miliband" + 0.009*"wales" + 0.009*"good" + 0.009*"getting" + 0.009*"best" + 0.009*"tories" + 0.008*"deliver" + 0.008*"thats" + 0.008*"leannewood" + 0.008*"greens" + 0.008*"well"')
  (5, '0.020*"miliband" + 0.013*"vote" + 0.013*"ukip" + 0.013*"tories" + 0.011*"bbcqt" + 0.011*"tory" + 0.009*"cameron" + 0.009*"scotland" + 0.007*"get" + 0.007*"nhs" + 0.007*"either" + 0.007*"racist" + 0.007*"doesnt" + 0.007*"heywood" + 0.007*"condone"')
  (6, '0.012*"nigelfarage" + 0.012*"labour" + 0.011*"miliband" + 0.009*"much" + 0.009*"tories" + 0.009*"tory" + 0.007*"thank" + 0.007*"take" + 0.007*"media" + 0.007*"ukip" + 0.007*"farage" + 0.006*"see" + 0.005*"houseoftraitors" + 0.005*"somebody" + 0.005*"one"')
  (7, '0.016*"fm" + 0.014*"tories" + 0.011*"questions" + 0.009*"answered" + 0.009*"benefit" + 0.009*"milliband" + 0.009*"strongly" + 0.009*"ground" + 0.009*"stood" + 0.009*"nite" + 0.009*"cameron" + 0.009*"diffcult" + 0.009*"martinmcarthur" + 0.009*"dodged" + 0.009*"working"')
  (8, '0.031*"miliband" + 0.020*"labour" + 0.019*"much" + 0.018*"snp" + 0.017*"tories" + 0.012*"spent" + 0.010*"deal" + 0.010*"power" + 0.010*"bbcqt" + 0.010*"would" + 0.009*"sorry" + 0.009*"borrowed" + 0.007*"clear" + 0.007*"nicola" + 0.006*"makes"')
  (9, '0.031*"mr" + 0.022*"snp" + 0.017*"labour" + 0.017*"cameron" + 0.015*"miliband" + 0.012*"name" + 0.011*"vote" + 0.010*"audience" + 0.010*"clegg" + 0.010*"tory" + 0.009*"nicola" + 0.009*"joncraig" + 0.009*"sturgeon" + 0.009*"scottish" + 0.009*"address"')
  (10, '0.025*"vote" + 0.025*"miliband" + 0.019*"snp" + 0.013*"labour" + 0.012*"scotland" + 0.010*"bbcqt" + 0.008*"tory" + 0.007*"say" + 0.006*"england" + 0.006*"austerity" + 0.006*"uk" + 0.006*"salmond" + 0.006*"rule" + 0.006*"hed" + 0.006*"blairmcdougall"')
  (11, '0.021*"snp" + 0.014*"miliband" + 0.013*"labour" + 0.010*"tory" + 0.009*"edmiliband" + 0.009*"tories" + 0.008*"bbcqt" + 0.007*"govt" + 0.007*"spending" + 0.006*"work" + 0.006*"vote" + 0.005*"someone" + 0.005*"global" + 0.005*"nurses" + 0.005*"wasnt"')
  (12, '0.018*"tories" + 0.013*"bbcqt" + 0.012*"miliband" + 0.012*"snp" + 0.011*"vote" + 0.008*"labour" + 0.008*"uk" + 0.006*"politics" + 0.006*"back" + 0.005*"across" + 0.005*"fm" + 0.005*"votesnp" + 0.005*"downing" + 0.005*"cameron" + 0.005*"get"')
  (13, '0.020*"snp" + 0.015*"labour" + 0.014*"tories" + 0.011*"edmiliband" + 0.010*"would" + 0.008*"debt" + 0.008*"cchqpress" + 0.008*"sturgeon" + 0.007*"ukip" + 0.007*"you’d" + 0.007*"propped" + 0.007*"borrowing" + 0.007*"ive" + 0.007*"mean" + 0.007*"taxes"')
  (14, '0.034*"snp" + 0.023*"labour" + 0.017*"ukip" + 0.014*"tories" + 0.014*"vote" + 0.011*"bbcqt" + 0.011*"farage" + 0.010*"nigel" + 0.009*"clear" + 0.009*"must" + 0.008*"bluff" + 0.008*"bring" + 0.008*"willing" + 0.008*"government" + 0.008*"prevent"')
  ```
  
  Some examples of tweets and their respective topics:
  
  ```
  [(1, 0.9034419)]
  RT @MichaelH14: Ed Miliband : it wasn't the spending on teachers &amp; nurses in Britain that crashed the global economy. 'Bout time someone sa…
  [(8, 0.9242945)]
  RT @WelshConserv: We've come a long way in 5yrs. Don't let EdM &amp; SNP drag us back to square one. Let's keep going #SecureTheRecovery https:…
  [(1, 0.88799304)]
  RT @KevinJPringle: .@Ed_Miliband's distancing from @theSNP wholly under pressure from Tories - he went way too far &amp; has given Labour in Sc…
  [(13, 0.5805273)]
  RT @A_Liberty_Rebel: Only regret at #BBCQT is that, in Yorkshire, no-one asked Miliband about connection between #Rotherham &amp; criminalising…
  [(1, 0.8962687)]
  RT @shonad7674: Tory &amp; Labour you insult me every time you open your mouth.I am a pensioner voting politically for 1st time &amp; will be votin…
  [(13, 0.9034386)]
  RT @AngusMacNeilSNP: Again Nicola Sturgeon a truly amazing political &amp; honest personal connection with audience ..#Impressed  Join SNP at h…
  [(14, 0.8879382)]
  ```
  
  #### 2.2 Discuss the differences for each k. 
  
  ### 3. Changing values for alpha, beta and minimum probability.
  
  ### 4. Consideration
  
  The same consideration made on the Assignment 2A, this dataset has a problem in that many tweets are retweets with most of the text being the same between the original tweet and the retweets. In the future I should also filter the retweets and test the clustering methods again.  
  
  ### 5. Source code on GitHub: https://github.com/lumizila/TextAnalysisHw2B
  
