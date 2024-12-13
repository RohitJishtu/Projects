import pandas as pd
import logging
import math
import numpy as np 
from scipy.stats import kurtosis
from scipy.stats import skew

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data_operations.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()


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
