# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 00:17:21 2021

@author: Kor-MasterX
"""

import pandas as pd

tup_data=('영인','2010-05-01','여',True)
sr=pd.Series(tup_data,index=['이름','생년월일','성별','학생여부'])
print(sr)

#정수형 위치 인덱스와 인덱스 이름 이용하여 원소 반환 
print(sr[0])
print(sr['이름'])

#짝을 이루는 인덱스와 원소 모두 반환
print(sr[[1,2]])
print('\n')
print(sr[['생년월일','성별']])

#인덱스 범위 지정하여 원소 반환
#정수 위치 인덱스 이용 시 범위의 끝 포함x but 인덱스 이름은 끝 포함o
print(sr[1:2])
print('\n')
print(sr['생년월일':'성별'])