#UNSUPERVISED SENTIMENT ANALYSIS
#1.LOAD THE LIBRARIES
library(tm)
library(SentimentAnalysis) 

#2.UPLOAD THE DATASET
data_sentiment <- read.csv('csvdataR.csv', sep=";", stringsAsFactors=FALSE)
View(data_sentiment)
data1<- data_sentiment[,c(7,13)]

#3.UPLOAD THE DICTIONARIES
data(DictionaryLM)  
str(DictionaryLM)

data(DictionaryHE)  
str(DictionaryHE) 

data(DictionaryGI)  
str(DictionaryGI)