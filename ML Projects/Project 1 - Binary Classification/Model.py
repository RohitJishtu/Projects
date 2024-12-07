from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,precision_score, recall_score
from xgboost import XGBClassifier 
class MLModelBuild:


    def __init__(self,Modelname):
        ModelName=Modelname


    def Split(self,ModelName, X , Y , Size=0.2 , state=42):

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=Size, random_state=state)

        return X_train, X_test, Y_train, Y_test


    def Call_Model(self):

        if self.ModelName=='Dtree_Model_clf':

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

            return  XGBClassifier( 
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


        def Fit_Model(self,X_train,y_train,X_test,y_test,custom_threshold=0.25):


            if self.ModelName=='Dtree':

                Classifier = self.Call_Model()
                Classifier.fit(X_train, y_train)
                y_pred = Classifier.predict(X_test)
                y_pred_proba=Classifier.predict_proba(X_test)
                predicted_class1 = (y_pred_proba[:, 1] >= custom_threshold).astype(int)


            elif self.ModelName=='RandomForest':

                Classifier = self.Call_Model()
                Classifier.fit(X_train, y_train)
                y_pred = Classifier.predict(X_test)
                y_pred_proba=Classifier.predict_proba(X_test)
                predicted_class1 = (y_pred_proba[:, 1] >= custom_threshold).astype(int)

            elif self.ModelName=='XGBoost':

                Classifier = self.Call_Model()
                Classifier.fit(X_train, y_train)
                y_pred = Classifier.predict(X_test)
                y_pred_proba=Classifier.predict_proba(X_test)
                predicted_class1 = (y_pred_proba[:, 1] >= custom_threshold).astype(int)

#Confusion matrix 



#Feature Importance 
if Model=='Dtree':
    feature_importances = Dtree_Model_clf.feature_importances_
elif Model=='RandomForest':
    feature_importances = RF_Model_clf.feature_importances_
elif Model=='XGBoost':
    feature_importances = XGBModel.feature_importances_
