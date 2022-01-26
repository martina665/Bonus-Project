#CART-TREE MODEL
#1.LOAD THE LIBRARIES
require(readr)
library(caret)
library(e1071)
library (tm)
library(SnowballC)
library(caTools)

#2.LOAD THE DATASET
data<-read.csv('csvdataR.csv', sep=";", stringsAsFactors=FALSE)
data1<- data[,c(7,13)]
str(data1)

#3.CREATE NEW VARIABLE "NEGATIVE"
data1$Negative = as.factor(data1$programminglevel_after <= 4)
table(data1$Negative) #15 false, 11 true
prop.table(table(data1$Negative)) #57% false, 43% true

#4.DATA PREPROCESSING
corpus = VCorpus(VectorSource(data1$course_feedback))
# Review Corpus
corpus
#View the feedbacks from the corpus
corpus[[1]]$content
corpus[[5]]$content

#5.DATA CLEANING
#Convert corpus to lowercase
corpus = tm_map(corpus, content_transformer(tolower))
corpus[[1]]$content
corpus[[5]]$content
#Remove punctuation
corpus = tm_map(corpus, removePunctuation)
corpus[[1]]$content
#Stemming 
corpus = tm_map(corpus, stemDocument)
corpus[[1]]$content
#Remove stopwords
corpus = tm_map(corpus, removeWords, c(stopwords("english")))
corpus[[15]]$content
#Remove specific words
corpus= tm_map(corpus, removeWords, c("reach", "r", "felt", "new", "thing", "well", "truli", "way", "better", "mani", "much", "overal", "thing", "teach", "littl", "acquir", "odd", "requir", "regard", "due", "person", "everyth", "use", "far", "especi", "cours", "veri","quit", "need", "between", "semest", "could", "the", "and", "lesson", "but", "lot", "a", "of", "except", "think", "some", "was", "i", "enjoy", "learn", "sometim", "time", "despit", "on", "in", "about", "found", "bit", "to", "sum","up", "first"))

#6.INSPECT THE CORPUS
#DTM
frequencies = DocumentTermMatrix(corpus)
frequencies
#Look at terms frequency
findFreqTerms(frequencies, lowfreq=8)
#Remove sparse terms
sparse = removeSparseTerms(frequencies, 0.92)
sparse

#7.SPLIT THE DATA (TRAIN AND TEST)
#Create a Data Frame
feedbacksparse <- as.data.frame(as.matrix(sparse))
#Modify columns name
colnames(feedbacksparse) = make.names(colnames(feedbacksparse))
#Add dependent variable  
feedbacksparse$Negative = data1$Negative
#Split in train and test data (80% train, 20% test)
set.seed(123)
split = sample.split(feedbacksparse$Negative, SplitRatio = 0.8)
trainSparse = subset(feedbacksparse, split==TRUE)
testSparse = subset(feedbacksparse, split==FALSE)

#8.CART MODEL (DECISION TREE)
#Package rpart is required
library(rpart)
library(rpart.plot)
#Fit the model with train data
feedCART = rpart(Negative ~ ., data=trainSparse, method="class",control=rpart.control(minsplit=6, cp=0.02))
prp(feedCART,roundint = FALSE)
#Make predictions on test set
predictCART = predict(feedCART, newdata=testSparse, type="class")
#Accuracy
table(testSparse$Negative, predictCART)
