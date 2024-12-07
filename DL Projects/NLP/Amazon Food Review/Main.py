# Import Libs
import sys
sys.path.append('/Users/rohit.jishtu/Documents/My Projects/GIt Bkp/Projects/ML Projects/Project 5 - Regression Problem')
print(sys.path)
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from Functions import *


# # Creating connection to the database 
# you can find this data set at Kaggle serach with Amazon food review Database 
# https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews


conn=sqlite3.connect('/Users/rohit.jishtu/Documents/My Projects/GIt Bkp/Projects/Deep Learning/NLP/Amazon Food Review/amazon_reviews/database.sqlite')
SourceDf= pd.read_sql("select * from reviews",conn)
SourceDf.head(5)


# # Step1: Labeling and Target identification


plt.hist(SourceDf['Score'])
SourceDf['Score'].value_counts().sort_index()

# Remove neutral Score 3 from source 
SourceDf=SourceDf[SourceDf['Score']!=3]


SourceDf['Rating']=SourceDf['Score'].apply(lambda x: 'Positive' if x >=4 else 'Negative')
SourceDf['Rating'].value_counts()
# plt.hist(SourceDf['Rating'])


SourceDf[(SourceDf['Rating']=='Negative') & (SourceDf['ProfileName']=='Jeanne Tomassi')]



# # Step 2 : Data Cleaning




# [[ASIIN:B007PA32L2 Green Mountain Coffee, Pumpkin Spice K-Cup packs for Keurig Brewers, 
#   50 count]]<br />I am so very disappointed in the lack of flavor and aroma 
# in the new packaging of the Pumpkin spice K-cup packs.<br />The packaging is different and it says "light roast".  
# This is definately not the same coffee that I've enjoyed so much over the last 2 years. 
# I really hope they bring back the original flavor!!! What a shame!!!


# Finding the same review by a user and seeing of they are repeating 
Groupdata=SourceDf.groupby(['UserId','Text','ProductId'])['Text'].agg(['count']).reset_index().sort_values(by=['count'],ascending=False)
SourceDf = SourceDf.drop_duplicates(subset=['UserId','Text','ProductId'],keep='first')


# (525814, 11) Before RemovinG Duplicates 
# (524587, 11) After RemovinG Duplicates 


numeric_stats=CalBasicStats(SourceDf,'numeric')
NONnumeric_stats=CalBasicStats(SourceDf,'nonnumeric')

# The columns are high in variance skewed towards zero or 1 

# plt.hist(SourceDf['HelpfulnessNumerator'],bins=5)
# plt.hist(SourceDf['HelpfulnessDenominator'],bins=5)



Targetdf=SourceDf.groupby(['Rating'])['Id'].count().reset_index()
Targetdf['RatingPercentage'] = Targetdf['Id']/sum(Targetdf['Id'])
print(SourceDf['Rating'].value_counts()/SourceDf.shape[0])


# # Step 3: Text Preprocessing 


# Text Cleaning 
# Tokensisation 
# Stop word removal 
# Stemming  
# lemmetisation 



import nltk
import re 
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords 
from nltk.stem import SnowballStemmer , PorterStemmer 
from nltk.stem.wordnet import WordNetLemmatizer


text="""- Excellent cuts of meat with no tendons.<br />- Very tasty. Just the right mix of spices.<br />- No added MSG 
and no added sugar!<br />- Convenient small snack-size bags.<br /><br />The best jerky I've ever encountered.
"""


def Preprocessing(inputdata):

    # Activity 1 : Text Cleaning using regex 
    clean_data1 = re.sub(r'<br.\s*/?>|-|\n', '', inputdata)
    clean_text = re.sub(r'[^\w\s]', '', clean_data1)
    # print(f"{clean_text=}")
    # Activity 2 : Tokenise
    token_list=[]
    for word in str.split(clean_text,' '):
        if len(word)>0:
            word=word.lower()
            token_list.append(word)
        
    # print(f"{token_list=}")
    
    # Activity 3 : StopWords 
    stop_words_dict=stopwords.words("english")
    custome_stopwords =['abc','ahh','aahh']
    stop_words=stop_words_dict+custome_stopwords
    stop_word_list=[word for word in token_list if word not in stop_words]
    # print(f"{stop_word_list=}")
    
    # # Activity 4.1 : Stemmer
    # snow_stem=SnowballStemmer("english")
    # port_stem=PorterStemmer()

    # poststem_list=[]
    # for word in stop_word_list:
    #     newword=snow_stem.stem(word)
    #     # newword2=port_stem.stem(word)
    #     print(f"{word=}{newword=}")
    #     poststem_list.append(newword)

    # Activity 4.2 : lemmetizer (emphasis on language)

    word_lem = WordNetLemmatizer()
    postlem_list=[]
    for word in stop_word_list:
        newword=word_lem.lemmatize(word)
        # newword2=port_stem.stem(word)
        # print(f"{word=}{newword=}")
        postlem_list.append(newword)
    textreturn = ' '.join(postlem_list)
    return textreturn
    
    # stop_words=stopwrods.
 


# cleanedtext= Preprocessing(text)
# word_tokenize(clean_text_1)


# Applying All preprocess to All the text column in data frame

SourceDf['Processed_Text']=  SourceDf['Text'].apply(lambda x : Preprocessing(x))


# # Step 4 : Bag of Words 


from sklearn.feature_extraction.text import CountVectorizer


CountVec=CountVectorizer(max_features=1000)
dtm_sparse_matrix1 =CountVec.fit_transform(SourceDf['Processed_Text'])
CountVec.get_feature_names_out()[1:100]


# 


# # Step 5 :Additional Dimension using BI Grams and Tri Grams


CountVec=CountVectorizer(ngram_range=(1,3),min_df=0.1,max_df=0.99)
dtm_sparse_matrix2=CountVec.fit_transform(SourceDf['Processed_Text'])
# 1% rare words removed 
# 99% percent repetaing terms removed 
CountVec.get_feature_names_out()


# 


# # Step  6 : TF - IDF  Matrix 


# How is this Diefferent from BOQ

# TF = Occurance of terms in document  / Total terms in document 
# IDF : How rare is the word wrt to total Corpus 

# IDF = log(base10) (Total Documents in corpus / Occurance of the term in documents)
# IDf for more frequent term is zero , less frequnent have some values 

# TF-IDF= tf * idf  


from sklearn.feature_extraction.text import TfidfVectorizer


tfidf=TfidfVectorizer(ngram_range=(1,2),min_df=0.005)
tfidf_matrix = tfidf.fit_transform(SourceDf['Processed_Text'])
CountVec.get_feature_names_out()


# # Step 7 :Model Building  - SVM Classifier 


from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix



SourceDf['Target']=SourceDf['Rating'].map({'Positive':1,'Negative':0})
X=SourceDf['Processed_Text']
Y=SourceDf['Target']
X_train,X_test,Y_train,y_test=train_test_split(X,Y,test_size=0.30,random_state=12)
X_train.shape,
X_test.shape
Y_train.shape
y_test.shape


# We will use tfidf to transform data to tf IDF 
X_Train_tfidf=tfidf.fit_transform(X_train)
X_Test_tfidf= tfidf.transform(X_test)


SVM_classifier = LinearSVC(C=1,penalty='l1',dual=False,random_state=12)
SVM_classifier.fit(X_Train_tfidf,Y_train)
Preds=SVM_classifier.predict(X_Test_tfidf)
# pd.crosstab(y_test,Preds)


# # Step 8 :Model Matrix 


print(classification_report(y_test,Preds))





