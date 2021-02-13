# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:55:39 2021

@author: Kor-MasterX
"""

#딕셔너리->시리즈 변환

#pandas 불러오기
import pandas as pd

dict_data={'a':1,'b':2,'c':3}

sr=pd.Series(dict_data)

print(type(sr))
print('\n')
print(sr)