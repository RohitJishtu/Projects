-- # Rank 6 (Score: 0.791311))

--V1 
ModelName: MeanAbsoluteError, RSquare ,AdjRSquare
Lasso : 321.382471 ,0.108067 ,0.098671
ElasticNet : 341.513789 ,0.062654 ,0.052779
DecisionTreeRegressor : 350.059272 ,-0.077135 ,-0.088483
KNeighborsRegressor : 358.353846 ,-0.070573 ,-0.081852
RandomForestRegressor : 343.398251 ,-0.006714 ,-0.017320
ExtraTreesRegressor : 354.171696 ,-0.100070 ,-0.111659
LinearRegression : 321.751102 ,0.107339 ,0.097935

RMSLE Error: 0.5739533259621563
Kaggle Score: 0.4260466740378437



-- V2 

Lasso : 313.566466 ,0.204761 ,0.193076
ElasticNet : 315.705164 ,0.173923 ,0.161785
DecisionTreeRegressor : 363.431421 ,-0.174808 ,-0.192070
KNeighborsRegressor : 341.623312 ,0.032428 ,0.018211
RandomForestRegressor : 321.338314 ,0.077180 ,0.063620
ExtraTreesRegressor : 332.652643 ,-0.025868 ,-0.040942
LinearRegression : 314.887022 ,0.205398 ,0.193722

RMSLE Error: 0.3604687667377105
Score: 0.6395312332622896



--V3


ModelName: MeanAbsoluteError, RSquare ,AdjRSquare
Lasso : 303.023483 ,0.225894 ,0.210054
ElasticNet : 303.665136 ,0.203213 ,0.186909
DecisionTreeRegressor : 276.634281 ,-0.069338 ,-0.091219
KNeighborsRegressor : 325.935876 ,0.016367 ,-0.003760
RandomForestRegressor : 245.141513 ,0.309702 ,0.295577
ExtraTreesRegressor : 240.740692 ,0.206441 ,0.190203
LinearRegression : 304.771132 ,0.224361 ,0.208490

RMSLE Error: 0.33062922597490135
Score: 0.6693707740250987

--v4 

['_NoOfReviews', 'Rating_Outof5', 'BookCategory_Action & Adventure', 'BookCategory_Arts, Film & Photography', 'BookCategory_Biographies, Diaries & True Accounts', 'BookCategory_Comics & Mangas', 'BookCategory_Computing, Internet & Digital Media', 'BookCategory_Crime, Thriller & Mystery', 'BookCategory_Humour', 'BookCategory_Language, Linguistics & Writing', 'BookCategory_Politics', 'BookCategory_Romance', 'BookCategory_Sports', 'Low_NoOfPeopleRated', 'Medium_NoOfPeopleRated', 'High_NoOfPeopleRated', 'CoverType_Hardcover', 'CoverType_Paperback', 'Year', 'Author_Min_OnlineReviews', 'Author_Avg_OnlineReviews', 'Author_max_OnlineReviews', 'BookCategory_Min_Price', 'BookCategory_Avg_Price', 'BookCategory_max_Price', 'Year_Category_AveragePrice', 'Bestseller_Score', 'Thriller_Mystery', 'Historic', 'Part_of_Series', 'Includes_Pictures']
Lasso : 306.887444 ,0.226597 ,0.214401
ElasticNet : 309.984071 ,0.193442 ,0.180724
DecisionTreeRegressor : 272.308016 ,-0.010895 ,-0.026835
KNeighborsRegressor : 324.502004 ,0.035089 ,0.019873
RandomForestRegressor : 232.924227 ,0.423134 ,0.414038
ExtraTreesRegressor : 234.877090 ,0.267600 ,0.256051
LinearRegression : 307.830045 ,0.225469 ,0.213256

RMSLE Error: 0.3263723764613953
Score: 0.6736276235386047



This book hopes to serve as a useful introduction to the literature of 
Britain especially for readers of English as a foreign language.

Logic is the backbone of Western civilization, holding together its systems of 
philosophy, science and law. Yet despite logic's widely acknowledged importance, 
it remains an unbroken seal for many, due to its heavy use of jargon and mathematical symbolism.
This book follows the historical development of logic, explains the symbols and methods involved 
and explores the philosophical issues surrounding the topic in an easy-to-follow and friendly manner. 
It will take you through the influence of logic on scientific method and the various sciences from physics to psychology, 
and will show you why computers and digital technology are just another case of logic in action.


An Outline History of English Literature takes a look at English literature, 
from the pre-Chaucerian period (500–1340 A.D.) down to the present age. 
It not only keeps a sequential account of various English Literature works but also 
of great writers such as Geoffrey Chaucer, William Shakespeare, John Milton, John Dryden, William Wordsworth, 
Alfred Tennyson and T.S. Eliot who were the backbone of English Literature.The biographical 
and historical interpretation of each work reflects the writer’s individuality along with the essence of the age and the history of the nation. 
It also traces the development of the English language and the evolution of different genres of English Literature.


--V5 


-- Lasso : 0.552958 ,0.211835 ,0.199407
-- ElasticNet : 0.552732 ,0.213423 ,0.201020
-- DecisionTreeRegressor : 0.449364 ,0.009854 ,-0.005759
-- KNeighborsRegressor : 0.541176 ,0.167232 ,0.154100
-- RandomForestRegressor : 0.412116 ,0.446385 ,0.437655
-- ExtraTreesRegressor : 0.387259 ,0.415292 ,0.406071
-- LinearRegression : 0.526351 ,0.268411 ,0.256875


-- RMSLE Error: 0.041649775812295994
-- Score: 0.958350224187704


Text=[
"FROM THE BESTSELLING AUTHOR OF RONALDO AND NEYMAR Prolific, cool-headed and unerringly consistent, Lionel Messi is one of the 
most revered footballers in history. But did you know that his transfer to Barcelona was first agreed on a 
paper napkin? Or that an x-ray of his hand was to thank for identifying his growth hormone deficiency? 
And do you know why he refused to collect his first ever Champions League winner's medal? Find out all this and more in Luca Caioli's 
classic portrait of a footballing icon, featuring exclusive interviews with those who know him best and even Messi himself. Includes all 
the action from the 2017/18 season and the 2018 World Cup"]


def get_bestseller_score(synopsis):
    # Perform sentiment analysis on the synopsis

    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(synopsis)['compound']
    # Map sentiment score to a scale of 1-100
    bestseller_score = int((sentiment_score + 1) * 50)

    return bestseller_score


What will be the score fromabove function 

