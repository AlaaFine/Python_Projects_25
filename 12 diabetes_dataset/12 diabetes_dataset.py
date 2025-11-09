#   TASK 12 : 

import numpy as np
import pandas as pd
data = pd.read_csv('/content/diabetes_dataset.csv')
data.head()
pd.DataFrame(data)
pd.DataFrame(data.columns)
data.shape
data.info()
data.describe()
data.isnull().sum()
print(data.isnull().sum())
   
