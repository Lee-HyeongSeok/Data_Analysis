#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


get_ipython().run_line_magic('precision', '3')
# 쥬피터 노트북의 출력을 소수점 이하 3자리로 제한


# In[5]:


pd.set_option('precision', 3)
# DataFrame의 출력을 소수점 이하 3자리로 제한


# In[7]:


df = pd.read_csv("D:\python_data\data\ch2_scores_em.csv",
                index_col = "student number")


# In[8]:


df.head()
# df의 처음 5행을 표시


# In[9]:


df


# In[11]:


df.head(3)
# df의 처음 3행을 표시


# In[52]:


scores = np.array(df['english'])[:10]
english_scores = np.array(df['english'])
scores
# 학번 순서대로 10명의 영어 점수를 array 데이터 구조 scores에 저장


# In[13]:


# 데이터 프레임 scores_df 작성
# index는 10개
scores_df = pd.DataFrame({'score' : scores},
                        index = pd.Index(['A', 'B', 'C', 'D', 'E',
                                         'F', 'G', 'H', 'I', 'J'],
                                        name = 'student'))
scores_df


# In[14]:


# 평균값 도출
sum(scores) / len(scores)


# In[15]:


# 평균값 도출
np.mean(scores)


# In[16]:


# 평균값 도출
scores_df.mean()


# In[17]:


# 중앙값 : 데이터 크기 순일 때 가운데 값
# 점수 정렬, 오름차순
sorted_scores = np.sort(scores)
sorted_scores


# In[18]:


# numpy, DataFrame, Series의 median 메서드
n = len(sorted_scores)
if n%2 == 0: 
    m0 = sorted_scores[n//2-1]
    m1 = sorted_scores[n//2]
    median = (m0 + m1)/2
    
else:
    median = sorted_scores[(n+1)//2-1]
    
median

# 짝수일 경우, 가운데 값 두개를 더해서 2로 나누어야 함
# 홀수일 경우, (n+1)/2 번째 데이터가 중앙값, 인덱스 기준이므로 -1 연산 필요


# In[22]:


# 최빈값, 데이터에서 가장 많이 나타나는 값
# DataFrame, Series의 mode() 메서드
pd.Series([1, 1, 1, 2, 2, 3]).mode()


# In[23]:


# 편차
# 각 데이터가 평균으로부터 얼마나 멀리 떨어져 있는지의 척도
# 각 학생의 성적 편차
# 편차 평균은 0
mean = np.mean(scores)
deviation = scores-mean
deviation


# In[25]:


# 분산
# 편차 제곱의 평균
# deviation은 편차
np.mean(deviation**2)

# Numpy의 var 함수
np.var(scores)


# In[26]:


# 표본분산 
# Series의 var 메서드는 불편분산
# Pandas의 표본분산은 var 메서드의 인수 ddof=0
scores_df.var()


# In[30]:


# 표준편차
# 분산에 제곱근을 취한 것
# sqrt 함수로 제곱근 취함
np.sqrt(np.var(scores, ddof=0))


# In[31]:


# 표준편차
# std함수 사용
np.std(scores, ddof=0)


# In[32]:


# 범위
# 데이터 전체가 아닌 최대, 최소값으로 산포도 표현
np.max(scores)-np.min(scores)


# In[33]:


# 사분위 범위
# 25, 50, 75% 위치 값
# 사분위 범위 = IQR = Q3-Q1
scores_Q1 = np.percentile(scores, 25)
scores_Q3 = np.percentile(scores, 75)
scores_IQR = scores_Q3-scores_Q1
scores_IQR


# In[34]:


# 데이터의 지표 정리
pd.Series(scores).describe()


# In[36]:


# 표준화
# 상대적 결과 다름 -> 통일된 지표로 변환
# 데이터에서 평균 빼고 표준편차로 나누는 작업(정규화)
# 표준화된 데이터는 변량, z 점수
z = (scores-np.mean(scores))/np.std(scores)
z


# In[37]:


# 표준화된 데이터의 평균이 0, 표준편차가 1인지 알아봄
np.mean(z), np.std(z, ddof=0)


# In[38]:


# 편차값
# 평균이 50, 표준편차가 10이 되도록 정규화한 값

z = 50 + 10 * (scores-np.mean(scores))/np.std(scores)
z


# In[39]:


# 편차값을 데이터프레임에 씌움
scores_df['deviation value'] = z
scores_df


# In[47]:


# 도수분포표
# 데이터의 분포 상태를 세부적으로 알려줌
# 분할된 구간과 데이터의 개수를 정리
# 계급값 : 각 계급을 대표하는 값, 계급의 중앙값을 이용
class_value= [(i+(i+10))//2 for i in range(0, 100, 10)]
class_value


# In[49]:


# 히스토그램
# 도수분포표를 막대그래프로 나타냄
# 데이터의 분포상태를 더 시각적으로 파악 가능
# 그래프 그리는데 필요한 Matplotlib 라이브러리 임포트
import matplotlib.pyplot as plt

# 그래프가 주피터 노트북 위에 표시
get_ipython().run_line_magic('matplotlib', 'inline')


# In[53]:


# 캔버스 생성
# figsize로 가로, 세로 크기 지정
fig = plt.figure(figsize=(10, 6))

# 캔버스 위에 그래프를 그리기 위한 영역 지정
# 인수는 영역을 1x1개 지정, 하나의 영역에 그린다는 것을 의미
ax = fig.add_subplot(111)

# 계급수를 10으로 해서 히스토그램 그림
freq, _, _=ax.hist(english_scores, bins=10, range=(0, 100))

# x축에 레이블 부여
ax.set_xlabel('score')

# y축에 레이블 부여
ax.set_ylabel('person number')

# x 축을 0, 10, 20, ,,100 눈금으로 구분
ax.set_xticks(np.linspace(0, 100, 10+1))

# y 축을 0, 1, 2, 의 눈금으로 구분
ax.set_yticks(np.arange(0, freq.max()+1))

# 그래프 표시
plt.show()


# In[55]:


# 히스토그램
# 계급수를 25, 계급폭을 4점으로 하는 꺾은선 그래프

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)

# y축의 스케일이 다른 그래프를 ax1과 동일한 영역에 생성
ax2 = ax1.twinx()

# 상대도수의 히스토그램으로 하기 위해서는 도수를 데이터의수로 나눌 필요가 있음
# hist의 인수 weight을 지정하면 가능
weights = np.ones_like(english_scores)/len(english_scores)
rel_freq, _, _ = ax1.hist(english_scores, bins=25,
                         range=(0, 100), weights=weights)

cum_rel_freq = np.cumsum(rel_freq)
class_value = [(i+(i+4))//2 for i in range(0, 100, 4)]

# 꺾은선 그래프를 그림
# 인수 ls를 --로 하면 점선이 그려짐
# 인수 marker를 o로 하면 데이터 점을 그림
# 인수 color를 gray로 하면 회색으로 지정

ax2.plot(class_value, cum_rel_freq,
        ls = '--', marker='o', color='gray')

# 꺾은선 그래프의 눈금선 제거
ax2.grid(visible=false)

ax1.set_xlabel('score')
ax1.set_ylabel('relative frequency')
ax2.set_ylabel('cumulative relative frequency')
ax1.set_xticks(np.linspace(0, 100, 25+1))

plt.show()


# In[ ]:




