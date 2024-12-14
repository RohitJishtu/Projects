import numpy as np
import logging
import pandas as pd
import sys
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import classification_report
from scipy.stats import chi2_contingency
import mlflow
import mlflow.pytorch
from sklearn.model_selection import train_test_split

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Custom imports (assuming these paths are correct and the scripts exist)
sys.path.append("/Users/rohit.jishtu/Documents/GitHub/NewMachine/Projects/MLOps/CompleteML/ModelBuild")
from LoadData import *
from Model import *


sys.path.append("/Users/rohit.jishtu/Documents/GitHub/NewMachine/Projects/StatsFunctions")
from Corr import *
from Stats import *




# Step 1: Load Data-------------------------------------------------------------------
file_path='../../ML Projects/Project 7 - Bank Marketing Data/bank/bank.csv'
def load_data(file_path):
    try:
        data = pd.read_csv(file_path, sep=';')
        if data is None:
            raise ValueError("Failed to load data.")
        logger.info(f"Data loaded successfully with shape: {data.shape}")
        return data
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        sys.exit(1)

# Load the data
data = load_data(file_path)

# Step 2: Define Target Column------------------------------------------------------------------------------------------------------------------------------------
data['Target'] = data['y'].apply(lambda x: 1 if x == 'yes' else 0)
logger.info(f"Target distribution:\n{data['Target'].value_counts() / data.shape[0]}")

# Step 3: Run Basic Statistics------------------------------------------------------------------------------------------------------------------------------------
def calculate_basic_stats(data, data_type):
    return CalBasicStats(data, data_type)

outdf_numeric = calculate_basic_stats(data, 'numeric')
outdf_nonnumeric = calculate_basic_stats(data, 'Non-numeric')


print(f'\n# Step 3: Run Basic Statistics COMPLETE\n')
# Step 4: Feature Selection------------------------------------------------------------------------------------------------------------------------------------

# Step 4: Feature Selection------------------------------------------------------------------------------------------------------------------------------------

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

print(f'\n# Step 4: Feature Selection COMPLETE\n')



# Step 5: Model Building and Training------------------------------------------------------------------------------------------------------------------------------------

# Prepare the features and target
Targets = ['Target','y','y_yes']
FeatureList= [x for x in TrainingData.columns if x not in Targets]
X=TrainingData[FeatureList] 
Y=data['Target'] 
X = X.fillna(0)
X = X.to_numpy(dtype=np.float32)  # Convert features to NumPy array
Y = Y.to_numpy(dtype=np.float32)


# Convert to PyTorch tensors
X_tensor = torch.tensor(X, dtype=torch.float32)
Y_tensor = torch.tensor(Y, dtype=torch.float32).view(-1, 1)

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_tensor, Y_tensor, test_size=0.3, random_state=42)

# Define a simple neural network model
class SimpleNN(nn.Module):
    def __init__(self, input_size):
        super(SimpleNN, self).__init__()
        self.layer1 = nn.Linear(input_size, 64)
        self.layer2 = nn.Linear(64, 32)
        self.layer3 = nn.Linear(32, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = self.sigmoid(self.layer3(x))
        return x

# Initialize the model
model = SimpleNN(input_size=X_train.shape[1])

# Loss function and optimizer
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training function
def train_model(model, X_train, Y_train, epochs=10):
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        
        # Forward pass
        output = model(X_train)
        loss = criterion(output, Y_train)
        
        # Backward pass and optimization
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 10 == 0:
            logger.info(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# Train the model
train_model(model, X_train, Y_train, epochs=100)

print(f'\n# Step 5: Model Training Complete\n')

# Step 6: Model Evaluation------------------------------------------------------------------------------------------------------------------------------------

# Evaluate the model
def evaluate_model(model, X_test, Y_test, threshold=0.5):
    model.eval()
    with torch.no_grad():
        y_pred_prob = model(X_test)
        y_pred = (y_pred_prob >= threshold).float()

    return y_pred, y_pred_prob

y_pred, y_pred_prob = evaluate_model(model, X_test, Y_test)

# Print Metrics
report = classification_report(Y_test, y_pred.numpy(), output_dict=True)
print(f"Classification Report:\n\n{report}")

print(f'\n# Step 6: Step 6: Model Evaluation-\n')
# Step 7: Feature Importances (Optional)------------------------------------------------------------------------------------------------------------------------------------

# PyTorch does not directly provide feature importances like tree-based models.
# However, you can use techniques like permutation importance for feature importance.

# Step 8: Log Model and Metrics with MLflow------------------------------------------------------------------------------------------------------------------------------------

# def log_to_mlflow(model, model_name, X_train, Y_train, report):
#     mlflow.set_tracking_uri("/Users/rohit.jishtu/Documents/My Projects/Project Personal/MLFlow/mlruns")
#     mlflow.set_experiment("BankMarketingData")

#     # Start MLflow run
#     with mlflow.start_run():
#         # Log the model to MLflow
#         mlflow.pytorch.log_model(model, "model", registered_model_name=model_name)

#         # Log metrics
#         mlflow.log_metrics({
#             'accuracy': report['accuracy'],
#             'recall_class_1': report['1.0']['recall'],
#             'recall_class_0': report['0.0']['recall'],
#             'f1_score_macro': report['macro avg']['f1-score']
#         })

#     logger.info("Model logged to MLflow.")

# log_to_mlflow(model, "BankMarketing_12Dec_NNModel", X_train, Y_train, report)


# Step 9: Export The Model------------------------------------------------------------------------------------------------------------------------------------

torch.save(model.state_dict(), 'BAnkData_NN_model.pth')
FeatureList_df=pd.DataFrame(FeatureList)
FeatureList_df.to_csv('FeatureList_df.csv')
print(f'\n# EOF \n')

