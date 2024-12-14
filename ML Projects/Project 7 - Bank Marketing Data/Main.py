import numpy as np
import logging 
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
from scipy.stats import chi2_contingency


###### Custom Imports 
import sys
sys.path.append("/Users/rohit.jishtu/Documents/GitHub/NewMachine/Projects/MLOps/CompleteML/ModelBuild")
from Stats import *
from LoadData import * 
from Model import *

#--------- Step1 : Source ------------------------------------------------------
sys.path.append("/Users/rohit.jishtu/Documents/GitHub/NewMachine/Projects/ML Projects/Project 7 - Bank Marketing Data")
# print(sys.path)
data = pd.read_csv('bank/bank-full.csv',sep=';')
if data is None:
    print("Failed to load data.")

print(data.columns)

#--------- Step 2 : Target Definition ------------------------------------------------------

data['Target'] = data['y'].apply(lambda x : 1 if x=='yes' else 0)
print(data['Target'].value_counts()/data.shape[0])

#--------- Step 3 : Running the stats ------------------------------------------------------

outdf_numeric = CalBasicStats(data,'numeric')
outdf_nonnumeric = CalBasicStats(data,'Non-numeric')




#--------- Step 4 : Feature Selection ------------------------------------------------------

keys=['y']
Selected =[]


outdf_nonnumeric=outdf_nonnumeric[(outdf_nonnumeric['UniqueCounts']>1)]
Columns2=outdf_nonnumeric['ColumnName'].to_list()


# 1. categorical Feature Selction Stratergy 
selected_cat_features = []
for feature in Columns2:
    contingency_table = pd.crosstab(data[feature], data['y'])
    chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)
    if p_value < 0.05:
        selected_cat_features.append(feature)


# 2 . Numerical Feature Selection Category 

outdf_numeric=outdf_numeric[(outdf_numeric['%Zero']<40) & (outdf_numeric['%Missing'] < 30)]
Selected.extend(outdf_numeric['ColumnName'].to_list())

#  Correlation 
sys.path.append("/Users/rohit.jishtu/Documents/GitHub/NewMachine/Projects/StatsFunctions/")
from Corr import * 

Selected.append('Target')
CorrelatedList,CorrelationDF=CorrAttributesList(data[Selected],'Target',0.02)
CorrelatedList=CorrelatedList.to_list()


# remove all feature from Selected list which are not in Corelation list 
for column in Selected:
    if column not in CorrelatedList:
        print(f'{column=} is not crossing correlation limit')
        Selected.remove(column)


# print(data.columns)
# print(Selected)

# Modifying data based on selected.
TrainingData=data[Selected]
for column in selected_cat_features:
    dummy_variables = pd.get_dummies(data[column], drop_first=True)
    prefix = str(column+'_')
    dummy_variables = dummy_variables.astype(int)
    dummy_variables = dummy_variables.add_prefix(prefix)
    TrainingData = pd.concat([TrainingData , dummy_variables], axis=1)


print(TrainingData.columns)  # Verify the merged data



#--------- Step 5 : Model Build and Training ------------------------------------------------------

Targets = ['Target','y','y_yes']
FeatureList= [x for x in TrainingData.columns if x not in Targets]
X=TrainingData[FeatureList]
Y=data['Target']



# Imputation with median
X = X.fillna(X.median())


# # # Call THe Model and Fit the Model
sys.path.append("/Users/rohit.jishtu/Documents/GitHub/NewMachine/Projects/MLOps/CompleteML/ModelBuild")
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

# Classification report 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,precision_score, recall_score
report = classification_report(Y_test, y_pred,output_dict=True)
print("\n\nClassification Report:\n\n\n", report)




#--------- Step 6 : feature Importances and Results   ------------------------------------------------------


Feature_Importance = ModelObject.feature_importances_
df_feature_importances = pd.DataFrame({'Feature': FeatureList, 'Importance': Feature_Importance})

print(f' \n----feature Importance -----{df_feature_importances=}\n')




#--------- Step 7 : Experiment Logged in the Ml Flow   ------------------------------------------------------
import mlflow
import mlflow.sklearn  # Adjust according to your model's framework, e.g., mlflow.pytorch, mlflow.tensorflow
import joblib


mlflow.set_tracking_uri("/Users/rohit.jishtu/Documents/My Projects/Project Personal/MLFlow/mlruns")
print(mlflow.get_tracking_uri())

mlflow.set_experiment("BankMarketingData")
model = ModelObject

model_params = model.get_params()
print("Model Parameters:", model_params)

# Start a new MLflow run
# with mlflow.start_run():
#     # Log the model to MLflow
#     mlflow.sklearn.log_model(sk_model=model, artifact_path="model", registered_model_name="BankMarketing_12Dec_DtreeModel")
    
#     # Optionally log other parameters and metrics
#     mlflow.log_param("max_depth", model_params)
#     mlflow.log_metrics({
#             'accuracy': report['accuracy'],
#             'recall_class_1': report['1']['recall'],
#             'recall_class_0': report['0']['recall'],
#             'f1_score_macro': report['macro avg']['f1-score']
#         })  
#     mlflow.sklearn.log_model(model, "Decision Tree Based Model") 
# print("Model logged to MLflow.")


#--------- Step 8 : Export The Model   ------------------------------------------------------
from joblib import dump
dump(ModelObject, "BankDtreeModel.joblib")
FeatureList_df=pd.DataFrame(FeatureList)
FeatureList_df.to_csv('MLFeatureList.csv')