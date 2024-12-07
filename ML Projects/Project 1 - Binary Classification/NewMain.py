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
print(f'Selected Features Before feature selection Module {len(SelectedFeatures)=} {SelectedFeatures=} ')

# Step 4.0: Remove PrimaryKey, sequence etc features , Removal very high missing values columns   Removal of very high zero values  

outdf_numeric = outdf_numeric[(outdf_numeric['%Zero'] > 40.0) | (outdf_numeric['%Missing'] > 50.0)]
cols0=list(outdf_numeric['ColumnName'])
cols0.append('index')
for columns in cols0:
    SelectedFeatures.remove(columns)


print(f'Selected Features After 4.1 {len(SelectedFeatures)=} {SelectedFeatures=} ')



#--------- Step 5 : Correlation  ------------------------------------------------------



CorrelatedList,CorrelationDF=CorrAttributesList(data,'Target',0.02)
CorrelatedList=CorrelatedList.to_list()


# remove all feature from Selected list which are not in Corelation list 
for column in SelectedFeatures:
    if column not in CorrelatedList:
        print(f'{column=} is not crossing correlation limit')
        SelectedFeatures.remove(column)


print(f'Selected Features Step 5 : Correlation {len(SelectedFeatures)=} {SelectedFeatures=} ')


#--------- Step 6 : Model Build and Training ------------------------------------------------------

Targets = ['Target','index','defects']
FeatureList= [x for x in SelectedFeatures if x not in Targets]
X=data[FeatureList]
Y=data['Target']

# Total Steps - 10 

# IMputation with median

X['TotalCharges'] = pd.to_numeric(X['TotalCharges'], errors='coerce', downcast='float')
X = X.fillna(X.median())


# Call THe Model 



# cm1 = confusion_matrix(predicted_class1)


#--------- Step 7 : Model Matrix on Hidden Test Set ------------------------------------------------------



#--------- Step 8 : Tuning Hyperparameters  ------------------------------------------------------


#--------- Step 9 : feature Importances and Results   ------------------------------------------------------




#--------- Step 10 : Export The Model amd Ready For Scoring   ------------------------------------------------------



