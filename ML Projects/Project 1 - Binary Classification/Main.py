import os
import numpy as np
import pandas as pd
from scipy.stats import kurtosis
from scipy.stats import skew
from MasterFunctions_V1 import *
# ML Libs 
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,precision_score, recall_score
# XGB Specific Libs 
from xgboost import XGBClassifier 
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score

#--------- Step1 : Source ------------------------------------------------------

Source=pd.read_csv('train.csv')
print('DataSize is ', Source.shape)
Source['index']=Source.index
SourceRaw=Source




#--------- Step 2 : Target Definition ------------------------------------------------------

Source["Target"]=  Source["defects"].apply(lambda x: 1 if x else 0)
Target=Source['Target']
Source['index']=Source.index
Key=Source['index']
Targetdf=Source.groupby(['Target'])['index'].count().reset_index()
Targetdf['Percentage'] = Targetdf.groupby(Target)['index'].transform(lambda x: x / x.sum() * 100)
print(Source['Target'].value_counts()/Source.shape[0])



#--------- Step 3 : Running the stats ------------------------------------------------------

outdf_numeric = CalBasicStats(Source,'numeric')
outdf_nonnumeric = CalBasicStats(Source,'Non-numeric')



#--------- Step 4 : Feature Selection ------------------------------------------------------

AllFeatures=SourceRaw.columns.to_list()
SelectedFeatures=AllFeatures


# Step 4.0: Remove PrimaryKey, sequence etc features 
cols0=['index']
for i in cols0:
    SelectedFeatures.remove(i)


# Step 4.1 : Removal very high missing values columns 

outdf_numeric=outdf_numeric[outdf_numeric['ColumnName'].isin(SelectedFeatures)]
SelectedFeatures= np.where((outdf_numeric["%Missing"]<40),outdf_numeric["ColumnName"],'Target')
SelectedFeatures=set(SelectedFeatures)

#Columns only with <50% Available values 

# Step 4.2 : Removal of very high zero values  

outdf_numeric=outdf_numeric[outdf_numeric['ColumnName'].isin(SelectedFeatures)]
SelectedFeatures= np.where((outdf_numeric["%Zero"]<40),outdf_numeric["ColumnName"],'Target')
SelectedFeatures=set(SelectedFeatures)
SelectedFeatures =SelectedFeatures 

print(SelectedFeatures)
Source=SourceRaw[SelectedFeatures]


#--------- Step 5 : Correlation  ------------------------------------------------------


spearman_corr = Source.corr(method='spearman')
CorrelationDF=pd.DataFrame()
CorrelatedList,CorrelationDF=CorrAttributesList(Source,'Target',0.02)
CorrelatedList=CorrelatedList.to_list()
SelectedFeatures=Source.columns
SelectedFeatures=CorrelatedList.to_list()



Resultdf1,model = DtreeCreator(Source,'loc','Target',2)
print(Resultdf1)


#--------- Step 6 : Model Build and Training ------------------------------------------------------

#Features removed as part of TargetLeakage
Targets = ['Target','index','defects']
FeatureList= [x for x in SelectedFeatures if x not in Targets]
X=Source[FeatureList]
Y=Source['Target']





# Random train test split And Model Build

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
Model='Dtree'
# Dtree_Model_clf = DecisionTreeClassifier(max_depth=5)
Dtree_Model_clf = DecisionTreeClassifier(criterion='entropy',
                                         max_depth=6,
                                         max_features=None,
                                         min_samples_split=5,
                                         min_samples_leaf=2,
                                         class_weight='balanced')


Model='RandomForest'
RF_Model_clf = RandomForestClassifier(
    n_estimators=100,      # Number of trees in the forest
    criterion='entropy',      # Split criterion: 'gini' or 'entropy'
    max_depth=6,        # Maximum depth of the trees (None means unlimited)
    min_samples_split=5,   # Minimum number of samples required to split an internal node
    min_samples_leaf=1,    # Minimum number of samples required to be at a leaf node
    max_features='auto',   # Number of features to consider for the best split ('auto' is sqrt(n_features))
    random_state=None  ,   # Seed for random number generator (None for random)
    class_weight='balanced'    
)

Model='XGBoost'
XGBModel = XGBClassifier( 
 learning_rate =0.1,
 n_estimators=100,
 max_depth=7,
 min_child_weight=0.5,
 gamma=5,
 subsample=1,
 colsample_bytree=0.4,
 objective= 'binary:logistic',
 nthread=4 , 
 scale_pos_weight=1,
 seed=27,
 eval_metric='auc')





custom_threshold=0.25

#Model Predict

if Model=='Dtree':
    Dtree_Model_clf.fit(X_train, y_train)
    y_pred = Dtree_Model_clf.predict(X_test)
    y_pred_proba=Dtree_Model_clf.predict_proba(X_test)
    predicted_class1 = (y_pred_proba[:, 1] >= custom_threshold).astype(int)
elif Model=='RandomForest':
    RF_Model_clf.fit(X_train, y_train)
    y_pred = RF_Model_clf.predict(X_test)
    y_pred_proba=RF_Model_clf.predict_proba(X_test)
    predicted_class1 = (y_pred_proba[:, 1] >= custom_threshold).astype(int)
elif Model=='XGBoost':
    XGBModel.fit(X_train, y_train)
    y_pred = XGBModel.predict(X_test)
    y_pred_proba=XGBModel.predict_proba(X_test)
    predicted_class1 = (y_pred_proba[:, 1] >= custom_threshold).astype(int)



#Confusion matrix 
cm1 = confusion_matrix(y_test, predicted_class1)
#Feature Importance 
if Model=='Dtree':
    feature_importances = Dtree_Model_clf.feature_importances_
elif Model=='RandomForest':
    feature_importances = RF_Model_clf.feature_importances_
elif Model=='XGBoost':
    feature_importances = XGBModel.feature_importances_



#Step 8 : Model Matrix on Fist Test Set 
from sklearn.metrics import roc_curve, auc,f1_score,roc_auc_score

# Calculate accuracy [Built in function]
accuracy = accuracy_score(y_test, predicted_class1)
print("Accuracy:", accuracy)
# Calculate precision
precision = precision_score(y_test, predicted_class1)
print("Precision:", precision)
# Calculate recall
recall = recall_score(y_test, predicted_class1)
print("Recall:", recall)

f1 = f1_score(y_test, predicted_class1)
print("F1 Score:", f1)
# Calculate AUC

auc = roc_auc_score(y_test, predicted_class1)
print("AUC:", auc)



#--------- Step 7 : Model Matrix on Hidden Test Set ------------------------------------------------------


Targets = ['Target','defects']

Test=pd.read_csv('/Users/rohit.jishtu/Documents/My Projects/Project Personal/Kaggle/Project 1 Binary Classification/test.csv')
Test["Target"]= None
FeatureList= [x for x in SelectedFeatures if x not in Targets]
X=Test[FeatureList]





y_pred2 = XGBModel.predict(X)
y_pred2_proba=XGBModel.predict_proba(X)
predicted_class2 = (y_pred2_proba[:, 1] >= custom_threshold).astype(int)


# cm2 = confusion_matrix(Y, predicted_class2)

# # Calculate accuracy [Built in function]
# accuracy = accuracy_score(Y, predicted_class2)
# print("Accuracy:", accuracy)
# # Calculate precision
# precision = precision_score(Y, predicted_class2)
# print("Precision:", precision)
# # Calculate recall
# recall = recall_score(Y, predicted_class2)
# print("Recall:", recall)

# f1 = f1_score(Y, predicted_class2)
# print("F1 Score:", f1)
# # Calculate AUC

# auc = roc_auc_score(Y, predicted_class2)
# print("AUC:", auc)




#Step 8.3 : Finding the optimum threshhold
from plotnine import *
import plotnine


# Step 1 :  Create the ROC curve

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:,1])
# Plot the ROC curve
df_fpr_tpr = pd.DataFrame({'FPR':fpr, 'TPR':tpr, 'Threshold':thresholds})
df_fpr_tpr
# Step 2 :  ROC Curve Plots 

# plotnine.options.figure_size = (8, 4.8)
# (
#     ggplot(data = df_fpr_tpr)+
#     geom_point(aes(x = 'FPR',
#                    y = 'TPR'),
#                size = 0.4)+
#     geom_line(aes(x = 'FPR',
#                   y = 'TPR'))+
#     labs(title = 'ROC Curve')+
#     xlab('False Positive Rate')+
#     ylab('True Positive Rate')+
#     theme_minimal()
# )

#Step 3 : G-mean= Geometric Mean of recall and Specificity 
gmean = np.sqrt(tpr * (1 - fpr))
print(gmean)

# Find the optimal threshold
index = np.argmax(gmean)
thresholdOpt = round(thresholds[index], ndigits = 4)
gmeanOpt = round(gmean[index], ndigits = 4)
fprOpt = round(fpr[index], ndigits = 4)
tprOpt = round(tpr[index], ndigits = 4)
print('Best Threshold: {} with G-Mean: {}'.format(thresholdOpt, gmeanOpt))
print('FPR: {}, TPR: {}'.format(fprOpt, tprOpt))



#Step 4 : G-mean= Geometric Mean of recall and Specificity 
gmean = np.sqrt(tpr * (1 - fpr))


# Find the optimal threshold
plotnine.options.figure_size = (8, 4.8)
(
    ggplot(data = df_fpr_tpr)+
    geom_point(aes(x = 'FPR',
                   y = 'TPR'),
               size = 0.4)+
    # Best threshold
    geom_point(aes(x = fprOpt,
                   y = tprOpt),
               color = '#981220',
               size = 4)+
    geom_line(aes(x = 'FPR',
                  y = 'TPR'))+
    geom_text(aes(x = fprOpt,
                  y = tprOpt),
              label = 'Optimal threshold \n for class: {}'.format(thresholdOpt),
              nudge_x = 0.14,
              nudge_y = -0.10,
              size = 10,
              fontstyle = 'italic')+
    labs(title = 'ROC Curve')+
    xlab('False Positive Rate (FPR)')+
    ylab('True Positive Rate (TPR)')+
    theme_minimal()
)





#--------- Step 8 : Tuning Hyperparameters  ------------------------------------------------------

# #Step 8.2 : Hyperparameter tuning of Decision Tree 

# from sklearn.model_selection import GridSearchCV

# param_grid = {
#     'criterion': ['gini', 'entropy'],
#     'max_depth': [None, 5, 6, 7],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4],
#     'max_features': [None, 'sqrt', 'log2']
# }

# grid_search = GridSearchCV(estimator=Dtree_Model_clf, param_grid=param_grid, cv=5, scoring='f1', verbose=1, n_jobs=-1)
# grid_search.fit(X_test, predicted_class1)
# best_params = grid_search.best_params_
# best_classifier = grid_search.best_estimator_



#--------- Step 9 : feature Importances and Results   ------------------------------------------------------

feature_names = X.columns
df_feature_importances = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
df_feature_importances=df_feature_importances[(abs(df_feature_importances["Importance"])>0)]
df_feature_importances
df_feature_importances






Modelresultdf=pd.DataFrame()
Modelresultdf['Index']=X.index 
Modelresultdf['Id']=X["id"] 
Modelresultdf['Model']='Random Forest'
Modelresultdf['PredictedValue']=XGBModel.predict_proba(X)[:, 1]
Finalresultdf = Modelresultdf.merge(Y, right_index=True, left_on='Index', how='inner')



Modelresultdf
Submission=pd.DataFrame()
Submission['id']=Modelresultdf['Id']
Submission['defects']=Modelresultdf['PredictedValue']
Submission.to_csv('Submission.csv')




#--------- Step 10 : Print Summary to Text Files   ------------------------------------------------------




