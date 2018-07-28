# K-Means-Clustering

Built a K-Means clustering model and clustered redundant/repeated tweets into the same cluster by utilizing Jaccard Distance metric and K-means clustering algorithm. Also computed and reported the sum of squared errors(sse) value.

Instructions to run code:
1. Please ensure that you are running your code on Python 2.7 compiler.
2. Need to have the input files 'InitialSeeds.txt' and 'Tweets.json' present in the same folder

The libraries used were: json, csv

Run the program, kmeans-tweets.py as follows:
>>python kmeans-tweets.py<numberOfClusters> <initialSeedsFile> <TweetsDataFile> <outputFile>

For example,
>>>python kmeans-tweets.py 25 InitialSeeds.txt Tweets.json tweets-k-means-output.txt
