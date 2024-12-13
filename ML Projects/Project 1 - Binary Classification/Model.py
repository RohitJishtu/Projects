from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,precision_score, recall_score
# from xgboost import XGBClassifier 
from sklearn import preprocessing
from sklearn.metrics import roc_curve, auc,f1_score,roc_auc_score



class MLModelBuild:


    def __init__(self,Modelname):
        self.ModelName=Modelname


    def Data_Split(self,X , Y , Size=0.2 , state=42):

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=Size, random_state=state)

        return X_train, X_test, Y_train, Y_test


    def Call_Model(self):

        if self.ModelName=='Dtree':

            return  DecisionTreeClassifier(criterion='entropy',
                                                max_depth=6,
                                                max_features=None,
                                                min_samples_split=5,
                                                min_samples_leaf=2,
                                                class_weight='balanced')
        elif self.ModelName=='RandomForest':

            return  RandomForestClassifier(
                n_estimators=100,      # Number of trees in the forest
                criterion='entropy',      # Split criterion: 'gini' or 'entropy'
                max_depth=6,        # Maximum depth of the trees (None means unlimited)
                min_samples_split=5,   # Minimum number of samples required to split an internal node
                min_samples_leaf=1,    # Minimum number of samples required to be at a leaf node
                max_features='auto',   # Number of features to consider for the best split ('auto' is sqrt(n_features))
                random_state=None  ,   # Seed for random number generator (None for random)
                class_weight='balanced'    
            )
        elif self.ModelName=='XGBoost':
            pass

            # return  XGBClassifier( 
            #     learning_rate =0.1,
            #     n_estimators=100,
            #     max_depth=7,
            #     min_child_weight=0.5,
            #     gamma=5,
            #     subsample=1,
            #     colsample_bytree=0.4,
            #     objective= 'binary:logistic',
            #     nthread=4 , 
            #     scale_pos_weight=1,
            #     seed=27,
            #     eval_metric='auc')


    def Call_Fit_Model(self,X , Y ,custom_threshold=0.25):
            Model=self.Call_Model()
            lab = preprocessing.LabelEncoder()
            Y = lab.fit_transform(Y)
            predicted_class1=None
            Model.fit(X, Y)
       

            return Model

        #Confusion matrix 
    def AllModel_Metrics(self,y_test,predicted_class):

                        # Calculate accuracy [Built in function]

            print(f'\n-------SPLIT SET PERFORMANCE ------\n')
            accuracy = accuracy_score(y_test, predicted_class)
            print("Accuracy:", accuracy)
            # Calculate precision
            precision = precision_score(y_test, predicted_class)
            print("Precision:", precision)
            # Calculate recall
            recall = recall_score(y_test, predicted_class)
            print("Recall:", recall)

            f1 = f1_score(y_test, predicted_class)
            print("F1 Score:", f1)
            # Calculate AUC
            auc = roc_auc_score(y_test, predicted_class)
            print("AUC:", auc)

            print(confusion_matrix(y_test, predicted_class))


    def Feature_Importance(self):
            #Feature Importance 
            return  self.Call_Model().feature_importances_