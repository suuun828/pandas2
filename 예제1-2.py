# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 00:05:34 2021

@author: Kor-MasterX
"""

import pandas as pd

list_data=['2019-001-02',3.14,'ABC',100,True]
sr=pd.Series(list_data)
print(sr)

idx=sr.index
val=sr.values
print(idx)
print('\n')
print(val)