# -*- coding: utf-8 -*-

import pandas as pd

df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
                index=['준서','예은'],
                columns=['나이','성별','학교'])

print(df)
print('\n')

#rename() 메소드 사용하여 행 인덱스, 열 이름 수정
df.rename(columns={'나이':'연령','성별':'남녀'},inplace=True)

print(df)