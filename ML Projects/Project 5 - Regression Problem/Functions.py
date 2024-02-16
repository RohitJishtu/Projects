# %%
import os
import numpy as np
import pandas as pd
from scipy.stats import kurtosis
from scipy.stats import skew
import seaborn as sns
import matplotlib.pyplot as plt
import math

import os
import numpy as np
import pandas as pd
from scipy.stats import kurtosis
from scipy.stats import skew
import matplotlib.pyplot as plt

import seaborn as sns
import math
import altair as alt

# Matplot Libs 

from matplotlib.colors import LinearSegmentedColormap
# Ml Libs 
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.utils.class_weight import compute_sample_weight
#regression

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import confusion_matrix, accuracy_score,precision_score, recall_score


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
numericsflots = ['float16', 'float32', 'float64']
nonnumerics =['object']
date=['datetime64[ns]','datetime64']
nonnumericsAnddate=['object','datetime64[ns]']

def CalBasicStats(Source_DF,type):
    data = Source_DF
    newdf = pd.DataFrame()
    Resultdf= pd.DataFrame()

    if type=='numeric':
        Traversedf = data.select_dtypes(include=numerics)

        for i in Traversedf.columns:
            
        
        #newdf['DataSourceName']=[name]
            newdf['ColumnName']=[i]
            newdf['AllCounts'] = Traversedf[i].size
            newdf['NotNullCounts'] = Traversedf[i].count()
            newdf['UniqueCounts'] = Traversedf[i].nunique()
            
            newdf["%Zero"] = ((Traversedf[i] == 0).sum()/Traversedf[i].size)*100
            newdf["%Missing"]= 100-(Traversedf[i].count() / Traversedf[i].size)*100

            
            newdf['Min']=np.amin(Traversedf[i])
            newdf['Max']=np.amax(Traversedf[i])
            newdf['Mean']=np.mean(Traversedf[i])

            newdf['Average']=np.average(Traversedf[i])

            newdf['Median']=np.nanmedian(Traversedf[i],axis=0)
            newdf['StddDev']=np.std(Traversedf[i],axis=0)
            newdf['Var']=np.var(Traversedf[i],axis=0)

            newdf['Skewness']=skew(Traversedf[i].dropna())

            newdf['Kurtosis']=kurtosis(Traversedf[i].dropna())
    
            newdf['25Percentile'] = np.nanpercentile(Traversedf[i], 25,axis=0)
            newdf['50Percentile'] = np.nanpercentile(Traversedf[i], 50,axis=0)
            newdf['75Percentile'] = np.nanpercentile(Traversedf[i], 75,axis=0)
            
            
            # Resultdf=Resultdf.append(newdf)
            Resultdf=pd.concat((Resultdf, newdf), axis = 0)
        #newdf["UniueRecords"]=pd.count(Traversedf[i])
        return Resultdf

    else:
        Traversedf = data.select_dtypes(include=nonnumerics) 

        for i in Traversedf.columns:
                # print(i)
        #newdf['DataSourceName']=[name]
            newdf['ColumnName']=[i]
            newdf['AllCounts'] = Traversedf[i].size
            newdf['NotNullCounts'] = Traversedf[i].count()
            newdf['UniqueCounts'] = Traversedf[i].nunique()

            newdf["%Missing"]= 100-(Traversedf[i].count() / Traversedf[i].size)*100

            Resultdf=pd.concat((Resultdf, newdf), axis = 0)     

        return Resultdf

# outdf_numeric = CalBasicStats(Sourcedf,'numeric')
# outdf_nonnumeric = CalBasicStats(Sourcedf,'Non-numeric')

# %% [markdown]
# # Func 3: Handling Missing values and outliers 

# %%
# Distribution Plots for all variables 
def CustomPlots(data,plot='hist'):
    colslist=data.columns.to_list()
    # row=math.floor(len(colslist)/4)+1

    if plot=='hist':
        col=4
        row=len(colslist)//col  + math.ceil((len(colslist)%col)/col)
        fig,ax=plt.subplots(nrows=row, ncols=col,figsize=(15,row*(col*0.75)))
        axes = ax.flatten()
        for prog, ax in zip(colslist, axes):
            ax = sns.histplot(data[prog], kde=True, color='g',ax=ax)

               
    elif plot=='box':
        col=4
        row=len(colslist)//col  + math.ceil((len(colslist)%col)/col)
        fig,ax=plt.subplots(nrows=row, ncols=col,figsize=(12,row*(col*0.75)))
        axes = ax.flatten()
        for prog, ax in zip(colslist, axes):
            ax = sns.boxplot(data[prog], color='g',ax=ax).set(xlabel=prog)
    

    plt.tight_layout()

# %%
def remove_outliers_iqr(data_frame, column_name):
    # Calculate the IQR for the specified column
    Q1 = data_frame[column_name].quantile(0.25)
    Q3 = data_frame[column_name].quantile(0.75)
    IQR = Q3 - Q1
    # Define the lower and upper bounds for valid data points
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Remove data points above the upper bound
    DF =  data_frame[(data_frame[column_name] >= lower_bound) & (data_frame[column_name] <= upper_bound)]


    return DF


def CorrAttributesList(data,Target,ThreshHold):
    EDA_df=data 
    correlation_values_P= EDA_df.corr(method='pearson')[Target]
    correlation_values_S= EDA_df.corr(method='spearman')[Target]
    EDA_concatenated_Correlation_df = pd.concat([correlation_values_P, correlation_values_S], axis=1,keys=['Pearson', 'Spearman'])

    for i in EDA_concatenated_Correlation_df.columns :
        j='Abs'+i
        EDA_concatenated_Correlation_df[j]=abs(EDA_concatenated_Correlation_df[i])
    Selected = EDA_concatenated_Correlation_df[(EDA_concatenated_Correlation_df["AbsPearson"]>ThreshHold) 
                                           | (EDA_concatenated_Correlation_df["AbsSpearman"]>ThreshHold)] 
                                  
    Selected_list=Selected.index

    return Selected_list,Selected



# # Need to write a better function 

def remove_highly_correlated_features(df, threshold):
    corr_matrix = df.corr().abs()  # Calculate the correlation matrix
    upper = corr_matrix.where(pd.np.triu(pd.np.ones(corr_matrix.shape), k=1).astype(bool))    
    # Find columns to drop
    drop_cols = [column for column in upper.columns if any(upper[column] > threshold)]
    print(drop_cols)
    # Remove highly correlated features
    df_filtered = df.drop(columns=drop_cols)
    return df_filtered




# %% [markdown]
# # Func5 : non Numeric Values Correaltion and (or label encoding)

# %% [markdown]
# # Func6 : Bi Variate using Decision Tree

# %%
def RangeCalc(min,max):
    if min==max:
            return min
    if np.isnan(min) ==True or np.isnan(max) ==True :
            return 'Missing'  
    else:
            min = float(min)
            max = float(max)
            suffixes = ['', 'K', 'M']
            magnitude_min = 0
            magnitude_max = 0
            while abs(min) >= 1000 and magnitude_min < len(suffixes)-1:
                min /= 1000
                magnitude_min += 1
            while abs(max) >= 1000 and magnitude_max < len(suffixes)-1:
                max /= 1000
                magnitude_max += 1
            min = '{:.1f}{}'.format(min, suffixes[magnitude_min])
            max = '{:.1f}{}'.format(max, suffixes[magnitude_max])
            min=str(min)
            max=str(max)
            return min +' to ' + max

def DtreeCreator(Sourcedf,var1,Target,debth=2,M='Classifier'):

    TreeDf=pd.DataFrame()
    TreeDf_NA_P=pd.DataFrame()

    #Prepping the data For Dtree
    EDA_df=Sourcedf
    TreeDf=EDA_df[[var1,Target]]
    TreeDf_NA_P=EDA_df[[var1,Target]]
    TreeDf_NA=TreeDf_NA_P[TreeDf_NA_P[var1].isna()]
    TreeDf=TreeDf.dropna()
    TreeDf.rename(columns = {var1:'X',Target:'Y'}, inplace = True)
    TreeDf_NA.rename(columns = {var1:'X',Target:'Y'}, inplace = True)



    # Split the data into independent variables (X) and the target variable (y)
    X = TreeDf[['X']]
    y = TreeDf['Y']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create the decision tree regressor
    if M=='Regressor':
        model = DecisionTreeRegressor(max_depth=debth, ccp_alpha=0.0, max_features=None)
        model.fit(X_train, y_train)

    else :
        model = DecisionTreeClassifier(max_depth=debth,min_samples_leaf= int(0.015 *len(TreeDf))) #.015 
        model.fit(X_train, y_train)
        
    # Predict the target variable for the test data

    if M=='Regressor':
        y_pred = model.predict(X_test)
        TreeDf['Pred']= model.predict(TreeDf[['X']])
    else :
        y_pred = model.predict(X_test)
        TreeDf['Pred']= model.predict_proba(TreeDf[['X']])[:, 1]


    #Creating the Final result and bucket 

    Pred_Unique=TreeDf["Pred"].unique()
    newdf=pd.DataFrame()
    newdfnewdf2=pd.DataFrame()
    Resultdf=pd.DataFrame()


    for i in Pred_Unique:
        newdf['Pred']=[i]
        newdf['VariableName']=var1
        newdf['X_min']=np.amin(TreeDf["X"][TreeDf["Pred"]==i])
        newdf['X_max']=np.amax(TreeDf["X"][TreeDf["Pred"]==i])
        newdf['Counts']=np.size(TreeDf["X"][TreeDf["Pred"]==i])
        newdf['Counts%']=round(((np.size(TreeDf["X"][TreeDf["Pred"]==i])/len(EDA_df))*100),1)
        Resultdf=pd.concat((Resultdf, newdf), axis = 0)

    # TreeDf=TreeDf.dropna()

    newdf['Pred']=np.mean(TreeDf_NA["Y"])
    newdf['VariableName']=var1
    newdf['X_min']=np.amin(TreeDf_NA["X"])
    newdf['X_max']=np.amax(TreeDf_NA["X"])
    newdf['Counts']=np.size(TreeDf_NA["X"])
    newdf['Counts%']=round(((np.size(TreeDf_NA["X"])/len(EDA_df))*100),1)


    Resultdf=pd.concat((Resultdf, newdf), axis = 0)

    Resultdf = Resultdf[Resultdf['Counts%']>2]

    #Post processing and Close 

    Resultdf["X_min"]=Resultdf["X_min"].round(2)
    Resultdf["X_max"]=Resultdf["X_max"].round(2)
    Resultdf=Resultdf.sort_values("X_min")
    Resultdf["Pred"]=Resultdf["Pred"].round(2)
    Resultdf["Counts%"]=Resultdf["Counts%"].astype(str) + '% obs'
    # Resultdf["Pred"]= Resultdf['Pred'].apply(lambda x: '0' if x== 0.0 else x)

    Resultdf['Range'] = Resultdf.apply(lambda row: RangeCalc(row['X_min'], row['X_max']), axis=1)
    return Resultdf,model



# Dtree Creation   
def PlotDtreeGraph2(data,Prefix=''):

    Resultdf=data 
    Maxy=data['Pred'].max()+0.20
    
    # create a Dictionary for Order Calculation 
    order=[]
    for i in range(0, len(Resultdf)):
        order.append(i)

    # XOrder=data['Range'].tolist()
    Title=data['VariableName'].iloc[0] + ' ' + Prefix
    # Title=Prefix
    print(Title)

    bar_plot = alt.Chart(Resultdf).mark_bar(color='#006E7F',stroke='black').encode(
        x=alt.X('Range',axis=alt.Axis(labelAngle=0),sort=alt.EncodingSortField(field='yield', order='descending')),
        y=alt.Y('Pred',title='Downsell'),
        tooltip=['Range','Pred','Counts'],
    )
    pred_labels = bar_plot.mark_text(
        align='center',
        baseline='bottom',
        dy=-5,  # Offset the text labels slightly above the bars
    ).encode(
        text='Pred'
    )
    count_label = bar_plot.mark_text(
        align='center',
        baseline='bottom',
        color='#FFFFFF',
        dy=25,  # Offset the text labels slightly above the bars
    ).encode(
        text='Counts%'
       
    )
    chart = (bar_plot + pred_labels +count_label).properties(width=650, height=300)

    # Adjust the range of the y-axis to zoom out the bars
    chart = chart.configure_axis(
        grid=False).encode(y=alt.Y('Pred', scale=alt.Scale(domain=(0, Maxy))))

    chart = chart.properties(title=Title)
    return display(chart)


# %% [markdown]
# # Func7 : Bivariate using Bars (or scatter)

# %% [markdown]
# # Func 8 : Model Building 

# %%
def plot_ConfusionMatrix(cm):
    bright_green_colormap = LinearSegmentedColormap.from_list(
        'bright_green', [(0, '#E5F5E0'), (0.5, '#80B6A1'), (1, '#293E40')])


    # confusion matrix
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=bright_green_colormap)
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=[0, 1], yticks=[0, 1], xlabel="Predicted", ylabel="True")
    ax.xaxis.set_ticklabels(['Class 0', 'Class 1'])
    ax.yaxis.set_ticklabels(['Class 0', 'Class 1'])

    # confusion matrix cells with the counts
    thresh = cm.max() / 2
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'), ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")

    plt.show()
