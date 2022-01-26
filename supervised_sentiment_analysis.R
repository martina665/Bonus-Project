#SUPERVISED SENTIMENT ANALYSIS
#1.LOAD THE LIBRARIES
library(SentimentAnalysis)
library(readr)
library(tm)
library(caret)
library(e1071)

#2.LOAD THE DATASET
data<-read.csv('dataset2S.csv', sep=";", stringsAsFactors=FALSE)
set.seed(123)
data <- data[sample(nrow(data)),]

#3.CLEAN THE DATA
feedback<- VCorpus(VectorSource(data$course_feedback)) 

clean_corpus <- function(CORPUS){
  CORPUS <- tm_map(CORPUS, content_transformer(tolower))
  CORPUS <- tm_map(CORPUS, content_transformer(removeWords), stopwords("en"))
  CORPUS <- tm_map(CORPUS, content_transformer(removePunctuation))
  CORPUS <- tm_map(CORPUS, content_transformer(removeNumbers))
  CORPUS <- tm_map(CORPUS, content_transformer(stripWhitespace))
  return(CORPUS)
}


cleaned_feedbacks <- clean_corpus(feedback)

#4.CREATE A DTM
dtm <- DocumentTermMatrix(cleaned_feedbacks)
#Check for empty docs
rowTotals <- apply(dtm , 1, sum)  
any(rowTotals == 0)

#5.SPLIT IN TRAIN AND TEST SET
set.seed(123)
sentiment <- data$sentiment
train_idx <- createDataPartition(sentiment,
                                 p = 0.8, # proportion of training data (80%)
                                 list = FALSE)#list equals to FALSE because otherwise it would set the output in a dataframe
train_idx 

# Split the vector form of the feedbacks into train and test 
X_train <- dtm[train_idx,] #split the matrices of features (dtm) and then the target variable
X_test <- dtm[-train_idx,]

sentiment_train <- sentiment[train_idx]
sentiment_test <- sentiment[-train_idx]

#6.PROPORTIONS
check_proportions <- function(x) {
  round(100*prop.table(table(x)), 1) #relative frequency
}

original <- check_proportions(data$sentiment)
original 

prop_train <- check_proportions(sentiment_train)
prop_train

prop_test <- check_proportions(sentiment_test)
prop_test

#7.CONVERT THE MATRIX OF FEATURES INTO DATAFRAME 
X_train <- as.data.frame(as.matrix(X_train))
X_test <- as.data.frame(as.matrix(X_test))

#8.CONVERT THE FEATUERS "FALSE" AND "TRUE" IN 'sentiment_train' AND 'sentiment_test' INTO NUMBERS (0-1)

sentiment_train[sentiment_train == "happy"] <- 1
sentiment_train[sentiment_train == "sad"] <- 0 

head(sentiment_train)
#9.TRANSFORM THEM AS NUMERIC VALUES
sentiment_train  <- as.numeric(sentiment_train)
head(sentiment_train)

sentiment_test[sentiment_test == "happy"] <- 1
sentiment_test[sentiment_test == "sad"] <- 0
sentiment_test  <- as.numeric(sentiment_test)

#10.FIT THE CLASSIFIER USING TRAIN DATA
# Function "svm" to fit the hyperplane 

system.time(fit <- svm(sentiment_train ~., # as target all the  features of the training data
                       type = "C-classification", #because a classification is being performed 
                       data = X_train,    # X_train is the DTM associated to the training data
                       kernel = "linear",  # linear equals to the optimal separating hyperplane
                       scale = FALSE)) # By default each variable is scaled to have unit variance; however when a variable is constant it cannot be scaled. This is why scale = F.

fit

#11. MAKE REDICTIONS USING THE TEST SET.

system.time(sentiment_predicted <- predict(fit, # the previous fitted model with training data
                                           newdata = X_test)) # test data as new data
#12. COMPUTE THE CONFUSION MATRIX

confusion_matrix <- table(sentiment_test,   # original target for the test data
                          sentiment_predicted, # predicted values
                          dnn=c("Actual", "Predicted"))
confusion_matrix
#13. COMPUTE THE ACCURACY
acc <- (confusion_matrix[1,1] + confusion_matrix[2,2])/sum(confusion_matrix)
acc

confusion_matrix_train <- table(sentiment_train, fit$fitted, dnn=c("Actual", "Predicted"))
acc_train <- (confusion_matrix_train[1,1] + confusion_matrix_train[2,2])/sum(confusion_matrix_train)
acc_train
