#setting WD
exWD <- ("/Users/ousmanesow/Desktop/RSP_Analysis")
setwd(exWD)
dir()
######################################################################################################################
# Part 1
# Install all required packages
install.packages(c("ggplot2", "e1071", "caret", "quanteda", 
                   "irlba", "randomForest"))
# read in data; using read.table outputs cleanest tabular format from .txt file

txt.raw <- read.table("dul.txt", header=F, sep = "\t", quote=""
                      , stringsAsFactors =F , encoding= "UTF-8")

# looking at raw data
View(txt.raw)
colnames(txt.raw)[1] <- "Text"
View(txt.raw)

#Check data to see if there are missing values
complete.cases(txt.raw) #complete cases
length(which(!complete.cases(txt.raw))) #not complete cases to showing missing cases

str(txt.raw) # display the data structure 

# distribution of text lengths
# store number of variables in new object called text length 
#txt.raw$CharLength <- nchar(txt.raw$Text)
summary(txt.raw$CharLength)

# Text Analysis
# install pakage Natural language processor and text mining
install.packages("NLP")
library(NLP)
install.packages("tm")
library(tm)
install.packages("SnowballC")
library(SnowballC) #word steaming

# Create the data to corpus for total dataset 

scorp <- VCorpus(VectorSource(txt.raw$Text))  # corpus for dataset

print(scorp) # to check the corpus document contains elements 


writeLines(as.character(scorp[[1]])) # examine a particular document in the corpus before cleaning

lapply(scorp[1:3], as.character) # inspect the three lines before cleaning



#################################################
#                                               #
#             Document cleaning                 #
#                                               #
################################################


#A . Cleaning all message document  

# scorp_c is storage for clean all  corpus document

scorp_c <- tm_map(scorp, content_transformer(tolower)) # convert text to lowercase
scorp_c <- tm_map(scorp_c, removeNumbers) # remove numbers
scorp_c <- tm_map(scorp_c, removeWords, stopwords("english")) # avoid stop words 
#scorp_c <- tm_map(scorp_c, removeWords, stopwords("SMART")) # avoid stop words 
scorp_c <- tm_map(scorp_c, removePunctuation) # remove punctuation
#scorp_c<- tm_map(scorp_c, stemDocument) # word steaming
scorp_c <- tm_map(scorp_c, stripWhitespace) # remove extra space


# Inspect the change

writeLines(as.character(scorp_c[[1]])) # inspect after cleaning 

lapply(scorp_c[1:4], as.character) # inspect the three lines After cleaning


#################################################
#                                               #
#     Text analysis of all  messages            #
#                                               #
################################################

# Term document matrix  of cleaned corpus "scorp_c" and store the result in variable "dtm"
#) the rows indicates the words and the columns indicates messages. 
dtm <- TermDocumentMatrix(scorp_c)

# Document term matrix  of cleaned corpus "scorp_c" and store the result in variable "dtm"
#the rows indicate sms messages and the column indicates the words.
s_dtm <- DocumentTermMatrix(scorp_c) 


# create  word matrix for Data visualizations 

dtm <- TermDocumentMatrix(scorp_c)
m <- as.matrix(dtm) # term document matrix is stored in variable dtm
v <- sort(rowSums(m),decreasing=TRUE) # sort the the matrix 

dfram <- data.frame(word = names(v),freq=v) # create dataframe (dfram)



###################################################
#                                                 #
#          Bar plot for most frequent words       #
#                                                 #
################################################### 

# the top  most frequent words 
head(dfram, 15) # top 10 words
tail(dfram,10) # least occurring words


# plot of top 10 frequently occured words 
barplot(dfram[1:15,]$freq, las = 2, names.arg = dfram[1:15,]$word,
        col ="tan", main ="Most frequent words",
        ylab = "Word frequencies")


# Inspecting frequent words with a given frequency in the document matrix dtm
findFreqTerms(dtm, lowfreq = 25)
findFreqTerms(dtm, lowfreq = 15)

# for terms frequency >150
library(ggplot2)

# most frequently occurred words (>150 times) 

p <- ggplot(subset(dfram,freq>=50), aes(word, freq)) #use dataframe created above "dfram"
p <- p + geom_bar(stat='identity', color = 'black', fill ='grey' )
p <- p + theme(axis.text.x=element_text(angle=45, hjust=1))
p

###################################################
#                                                 #
#          Word cloud analysis                    #
#                                                 #
###################################################   

install.packages("wordcloud") # for building wordcloud
install.packages("RColorBrewer") #Creates nice looking color palettes 
library(wordcloud)
library(RColorBrewer)
install.packages("wordcloud2")
library(wordcloud2)


#setting the same seed each time ensures consistent look across clouds
set.seed(123)
#limit words by specifying min frequency, and color 

#wordcloud(names(freq),freq,min.freq=50,colors=brewer.pal(6,"Dark2"))

#plot for more  than 100 most frequent words


# subset the data frame with minimum word frequency 5
df1 <- subset(dfram, freq >5) # subset of datafram  and store it in new datafram "df1" when frequency is specified

# create word cloud
wordcloud2(df1, color = "black", backgroundColor = "white")

wordcloud2(df1, minRotation = -pi/20,
           maxRotation = -pi/20, minSize = 10, rotateRatio = 1, color = "random-dark", backgroundColor = "white")







