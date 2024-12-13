import pandas as pd
import logging
import math
import numpy as np 
from scipy.stats import kurtosis
from scipy.stats import skew

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