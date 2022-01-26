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

#4.CREATE A CORPUS
corpus_sentiment <- VCorpus(VectorSource(data1$course_feedback)) 

#5.SENTIMENT ANALYSIS WITH 'ANALYZE-SENTIMENT'
# Within this function directly perform the pre-processing steps.
system.time(sentiment <- analyzeSentiment(corpus_sentiment, #the object of class corpus
                                          language = "english", 
                                          removeStopwords = TRUE, 
                                          stemming = TRUE, 
                                          removePunctuation = T,
                                          removeNumbers = T,
                                          tolower = T))
sentiment
head(sentiment) 

head(sentiment$SentimentGI)
head(sentiment$SentimentHE)
head(sentiment$SentimentLM)

#6.View sentiment direction
convertToDirection(sentiment$SentimentGI)