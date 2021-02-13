# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

student1=pd.Series({'국어':np.nan,'영어':80,'수학':90})
student2=pd.Series({'수학':80,'국어':90})

print(student1)
print('\n')
print(student2)
print('\n')

addition=student1+student2
subtranction=student1-student2
multiplication=student1*student2
division=student1/student2
print(type(division))
print('\n')

result=pd.DataFrame([addition, subtranction,multiplication,division],index=['덧셈','뺄셈','곱셈','나눗셈'])

print(result)