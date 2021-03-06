## **🧾 Python Lib**

***

### **⚙ Numpy 란**

- 파이썬 산술 계산 라이브러리
- 자료구조, 알고리즘 산술 데이터를 다루는 과학 계산 애플리케이션에서 필요한 라이브러리 제공
- 데이터 분석 알고리즘에 사용할 데이터 컨테이너 역할 수행
- 저수준 언어로 작성한 라이브러리는 Numpy 배열에 저장된 데이터를 복사하지 않고 바로 사용 가능
- **import numpy as np** 로 NumPy 모듈을 임포트 한다.

<br>



### **⚙ Numpy가 제공하는 기능**

1. 빠르고 효율적인 다차원 배열 객체 **ndarray**
2. 배열 원소를 다루거나 배열 간의 수학 계산을 수행하는 함수
3. 디스크로부터 배열 기반의 데이터를 읽거나 쓸 수 있는 도구
4. 선형대수 계산, 푸리에 변환, 난수 생성기
5. 파이썬 확장과 C, C++ 코드에서 Numpy의 자료구조에 접근, 계산 기능을 사용 가능하게 해주는 C API
6. 브로드캐스팅 지원
   - 크기가 다른 배열 간의 연산을 의미
   - Numpy는 **벡터화**를 지원하기 때문에 for 문을 작성하지 않고 데이터를 일괄 처리할 수 있다.

<br> 

### **⚙ Numpy 제공 함수**

- shape : 각 차원의 크기를 알려준다.
- dtype : 객체의 자료형을 추론한다.
- zeros / ones : 주어진 길이나 모양에 각각 0 / 1이 들어있는 배열을 생성한다.
- empty : 초기화되지 않은 배열을 생성한다.
  - 0으로 초기화된 배열을 반환하지 않는다.
  - np.empty는 초기화되지 않은 가비지 값으로 채워진 배열을 반환한다.
- astype : 배열의 dtype을 다른 형으로 명시적으로 변환 또는 캐스팅이 가능하다.
  - NumPy에서 문자열 데이터는 고정 크기를 가지며 별다른 경고를 출력하지 않고<br> 입력을 임의로 잘라낼 수 있다.
  - **numpy.string**형을 이용할 때 주의
  - **pandas**는 숫자 형식이 아닌 경우에 좀 더 직관적인 사용성 제공

<br>

### **⚙ Pandas 란**

- 구조화된 데이터, 표 형식의 데이터를 빠르고 쉽고 표현적으로 다루도록 설계된 <br>자료구조와 함수 제공
- Pandas 주 자료구조
  - 표 형태의 Row, Column 이름을 가지는 DataFrame
  - 1차원 배열 객체인 Series
- Numpy의 고성능 배열 연산 아이디어 + 스프레드시트와 RDB의 유연한 데이터 처리 기능 결합
- **색인 기능 제공**
  - 데이터 변형
  - 데이터 자르기
  - 데이터 취합
  - 데이터 부분 집합 선택

<br>



### **⚙ Matplotlib 이란**

- **2차원 데이터** 시각화를 생성하는 라이브러리
- 그래프를 만드는데 맞춰 설계되었음
- 생태계 내 다른 라이브러리들과 잘 연동되어 있다.



<br>

### **⚙ Scikit-learn**

- 범용 머신러닝 도구
- Scikit-learn의 하위 모듈
  - 분류 : SVM, 최근접 이웃, 랜덤 포레스트, 로지스틱 회귀
  - 회귀 : 라소, 리지 회귀
  - 클러스터링 : k-평균, 스펙트럴 클러스터링
  - 차원 축소 : PCA, 특징 선택, 행렬 인수분해
  - 모델 선택 : 격자탐색, 교차검증, 행렬
  - 전처리 : 특징 추출, 정규화

<br>

***

<br> 

## **📌 Python Reference**

- [Data Analysis Python 문법](https://github.com/Lee-HyeongSeok/Data_Analysis/blob/master/DataAnalysisExampleCode/Python%EB%AC%B8%EB%B2%95.md)
- [Data Analysis Python 자료형](https://github.com/Lee-HyeongSeok/Data_Analysis/blob/master/DataAnalysisExampleCode/Python%EC%9E%90%EB%A3%8C%ED%98%95.md)

- [파이썬 라이브러리를 활용한 데이터 분석 2판]