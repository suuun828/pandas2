# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns

titanic =sns.load_dataset('titanic')
df=titanic.loc[:,['age','fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

addition=df+10
print(addition.head())
print('\n')
print(type(addition))
print('\n')

subtraction=addition-df
print(subtraction.tail())
print('\n')
print(type(subtraction))