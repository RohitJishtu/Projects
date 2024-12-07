import numpy as np
import logging 
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

###### Custom Imports 

from LoadData import * 
from Stats import *

data = load_data('train.csv')
if data is None:
    print("Failed to load data.")
outdf_numeric = CalBasicStats(data,'numeric')
outdf_nonnumeric = CalBasicStats(data,'Non-numeric')


# We need Data whose %Zero and %Missing

FilterConditions =['%Missing','%Zero']
SelectedCols=[]


print(f'Outdooutdf_numeric COLUMNS ' ,outdf_numeric.columns)

# print(outdf_numeric['ColumnName','%Missing','%Zero'])
# print(outdf_numeric.dtypes)
# for Record in x.itertuples():
#     print(Record[0])
# print(SelectedCols)
