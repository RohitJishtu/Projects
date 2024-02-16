# %%
import os
import numpy as np
import pandas as pd
from scipy.stats import kurtosis
from scipy.stats import skew

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