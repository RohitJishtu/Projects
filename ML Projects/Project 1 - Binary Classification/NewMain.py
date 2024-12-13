import numpy as np
import logging 
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

###### Custom Imports 

from LoadData import * 
from Stats import * 
from Model import *

#--------- Step1 : Source ------------------------------------------------------


data = load_data('train.csv')
if data is None:
    print("Failed to load data.")

#--------- Step 2 : Target Definition ------------------------------------------------------

data['Target'] = data['defects'].apply(lambda x :1 if x else 0)
print(data['Target'].value_counts()/data.shape[0])



#--------- Step 3 : Running the stats ------------------------------------------------------

outdf_numeric = CalBasicStats(data,'numeric')
outdf_nonnumeric = CalBasicStats(data,'Non-numeric')



#--------- Step 4 : Feature Selection ------------------------------------------------------

AllFeatures=data.columns.to_list()
SelectedFeatures=AllFeatures
print(f'Selected Features Before feature selection Module {len(SelectedFeatures)=}')

# Step 4.0: Remove PrimaryKey, sequence etc features , Removal very high missing values columns   Removal of very high zero values  

outdf_numeric = outdf_numeric[(outdf_numeric['%Zero'] > 40.0) | (outdf_numeric['%Missing'] > 50.0)]
cols0=list(outdf_numeric['ColumnName'])
cols0.append('index')
for columns in cols0:
    SelectedFeatures.remove(columns)


print(f'Selected Features After 4.1 {len(SelectedFeatures)=}')



#--------- Step 5 : Correlation  ------------------------------------------------------



CorrelatedList,CorrelationDF=CorrAttributesList(data,'Target',0.02)
CorrelatedList=CorrelatedList.to_list()


# remove all feature from Selected list which are not in Corelation list 
for column in SelectedFeatures:
    if column not in CorrelatedList:
        print(f'{column=} is not crossing correlation limit')
        SelectedFeatures.remove(column)


print(f'\n Selected Features Step 5 : Correlation {len(SelectedFeatures)=}\n')


#--------- Step 6 : Model Build and Training ------------------------------------------------------

Targets = ['Target','index','defects']
FeatureList= [x for x in SelectedFeatures if x not in Targets]
X=data[FeatureList]
Y=data['Target']



# Imputation with median
# X = X.fillna(X.median())


# # # Call THe Model and Fit the Model

NewModel= MLModelBuild('Dtree')
X_train, X_test, Y_train, Y_test= NewModel.Data_Split(X,Y)
ModelObject= NewModel.Call_Fit_Model(X_train,Y_train)
print(ModelObject)

# Predict 
custom_threshold=0.50
y_pred = ModelObject.predict(X_test)
y_pred_proba=ModelObject.predict_proba(X_test)
predicted_class = (y_pred_proba[:, 1] >= custom_threshold).astype(int)


# Print Metrics 
NewModel.AllModel_Metrics(Y_test,predicted_class)

#--------- Step 7 : Model Matrix on Hidden Test Set ------------------------------------------------------



Test=pd.read_csv('test.csv')
X_Hideout=Test[FeatureList]

custom_threshold=0.50
y_Hideout_pred = ModelObject.predict(X_Hideout)
y_Hideout_pred_proba=ModelObject.predict_proba(X_test)
predicted_class_hideout = (y_Hideout_pred_proba[:, 1] >= custom_threshold).astype(int)

# Print Results distribution  
from collections import Counter
print(f' \n----UNSeeen Set Prediction performance -----{Counter(predicted_class_hideout)}\n')


#--------- Step 8 : Tuning Hyperparameters  ------------------------------------------------------


from HyperParameter import * 
TuneNow=False 
if TuneNow:
    best_classifier= GridSerach(ModelObject,X_test,predicted_class)
    print(f' ----Tuning Hyperparameters -----{best_classifier=}')
else:
    print(f'\n ----Skipping Hyperparameters Tunings -----\n')

#--------- Step 9 : feature Importances and Results   ------------------------------------------------------


Feature_Importance = ModelObject.feature_importances_
df_feature_importances = pd.DataFrame({'Feature': FeatureList, 'Importance': Feature_Importance})

print(f' \n----feature Importance -----{df_feature_importances=}\n')


#--------- Step 10 : Export The Model amd Ready For Scoring   ------------------------------------------------------
from joblib import dump
dump(ModelObject, "DtreeModel.joblib")


print(f'\n ----Model Exported to Location - LCose of File \n')
