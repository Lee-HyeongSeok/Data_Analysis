## **🧾 Python 자료구조와 순차 자료형**

***

<br>

### **목차**

1. **튜플**
2. **리스트**
3. **슬라이싱**
4. **내장 순차 자료형 함수**
   - enumerate
   - sorted
   - zip
   - reversed
5. **사전(dict)**
6. **집합**



<br> <br> 

### **1. 튜플**

- 1차원의 고정된 크기를 가지는 **변경 불가능한** 순차 자료형이다.

- 생성법은 쉽표로 구분된 값을 대입한다.

  ```python
  tup = 4, 5, 6
  tup
  # (4, 5, 6)
  ```

- 괄호를 사용해서 중첩된 튜플 정의 가능

- 모든 순차 자료형이나 iterator는 튜플 메서드를 호출해 튜플로 변환 가능

  ```python
  tup = ([4, 0, 2])
  # (4, 0, 2)
  tup = tuple('string')
  tup
  # ('s', 't', 'r', 'i', 'n', 'g')
  ```

- 순차 자료형의 색인은 0 부터 시작

- '+' 연산자를 통해서 튜플을 이어붙일 수 있다.
- 튜플에 정수를 곱하면 튜플의 복사본이 반복되어 늘어난다.

- 튜플과 같은 표현의 변수에 튜플을 대입하면 '=' 등호 오른쪽에 있는 변수에서 값을 분리한다.

  ```python
  tup = (4, 5, 6)
  a, b, c = tup # tup에서 값을 분리하여 a, b, c에 각각 대입한다.
  b
  # 5
  ```

- 값 분리를 이용한 두 변수의 값 바꾸기

  ```python
  a, b = 1, 2 # a에 1, b에 2 대입
  b, a = a, b # b에 오른쪽 a, a에 오른쪽 b를 대입한다.
  a
  # 2
  b
  # 1
  ```

  <br> 

### **2. 리스트**

- 튜플과 대조적으로 리스트는 **크기**나 **내용**의 변경이 가능하다.

- 1차원 순차 자료형

- 함수에서 교차적으로 사용할 수 있다.

- 대괄호 []나 list 함수를 사용해서 생성할 수 있다.

  ```python
  a_list = [2, 3, 7, None] # 대괄호를 사용해서 list 생성
  tup = ('foo', 'bar', 'baz') # 튜플 생성
  b_list = list(tup) # list 함수를 사용해서 튜플을 리스트로 변환
  
  b_list
  # ['foo', 'bar', 'baz']
  ```

- **append** 메서드를 통해 리스트의 끝에 새로운 값 추가 가능

  ```python
  b_list.append('dwarf')
  # ['foo', 'bar', 'baz', 'dwarf']
  ```

- **insert** 메서드를 통해 리스트의 특정 위치에 값 추가 가능

  - 추가된 위치 이후의 원소들은 내부적으로 자리를 옮겨야 하기 떄문에 연산 비용이 많이 든다.
  - 순차 자료형의 시작과 끝 지점에 원소를 추가하려면 양방향 큐인 **collections.deque** 사용 권장

  ```python
  b_list.insert(1, 'red')
  b_list
  # ['foo', 'red', 'baz', 'dwarf']
  ```

- **pop** 메서드는 특정 위치의 값을 반환하고 리스트에서 삭제한다.

- **remove** 메서드는 삭제가 리스트의 제일 앞 부분 부터 이루어진다.

- **sort** 메서드를 통해 리스트 정렬 가능

  - 문자열의 길이 순으로 정렬할 수 있다.

    ```python
    b = ['saw', 'small', 'He']
    b.sort(key=len)
    ```

- '+' 연산자를 통해 두 개의 리스트를 병합할 수 있다.

<br> 

### **3. 슬라이싱**

- 색인 연산자 [] 안에 start:stop을 지정해서 원하는 크기만큼 잘라낼 수 있다.

- 색인의 시작(start) 값이나 끝(stop) 값은 **생략 가능**

- 색인의 시작(start) 위치에 있는 값은 **포함**, 끝(stop) 위치에 있는 값은 **포함되지 않는다.** 

  - 슬라이싱 결과의 개수는 stop-start

  ```python
  seq = [7, 2, 3, 7, 5, 6, 0, 1]
  seq[1:5] # 인덱스 1부터 인덱스 5까지
  # [2, 3, 7, 5]
  ```

- 음수 색인은 순차 자료형의 끝에서부터의 위치를 나타낸다.

  ![Untitled Diagram](https://user-images.githubusercontent.com/55940552/108667597-eb2c1180-751c-11eb-9d57-f38ff16de751.png) 

<br> 

### **4. 내장 순차 자료형 함수**

1. **enumerate**

   - 순차 자료형에서 현재 아이템의 색인을 함께 처리하고자 할 때 흔히 사용

     ```python
     i=0
     # value를 사용하는 코드
     for value in collection:
         i += 1
         
     # enumerate를 사용하는 코드
     # (i, value) 튜플을 반환
     for i, value in enumerate(collection):
         i += 1
     ```

   - 순차 자료형에서의 값, 위치를 넘겨줄 때 사용<br> 

2. **sorted**

   - 정렬된 새로운 순차 자료형을 반환한다.

     ```python
     sorted([7, 1, 2, 6, 0, 3, 2])
     # [0, 1, 2, 2, 3, 6, 7]
     ```

     <br> 

3. **zip**

   - 여러 리스트나 튜플, 다른 순차 자료형을 서로 짝지어서 튜플의 리스트를 생성한다.

     ```python
     list1 = ['foo', 'bar', 'baz']
     list2 = ['one', 'two', 'three']
     zipped_list = zip(list1, list2)
     
     list(zipped_list)
     # [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
     ```

   - 여러 개의 순차 자료형을 동시에 순회하는 경우

     ```python
     for i, (a, b) in enumerate(zip(list1, list2)):
         print('{0}: {1}, {2}', format(i, a, b))
         
     # 0: foo, one
     # 1: bar, two
     # 2: baz, three
     ```

   - 리스트의 **Row**를 리스트의 **Col**로 변환 가능

     ```python
     Tup = [('name', 'Lee'), ('address', 'Seoul'), ('Sub', 'computer')]
     informations, person_info = zip(*Tup) # Tup 변수에서 각 key와 value 분리
     
     # Tup의 각 key 값들이 분리되어 informations 변수에 대입되었음
     informations
     # ('name', 'address', 'Sub')
     
     # Tup의 각 value 값들이 분리되어 person_info 변수에 대입되었음
     person_info
     # ('Lee', 'Seoul', 'computer')
     ```

4. **reversed**

   - 순차 자료형을 역순으로 순회한다.

   - reversed는 제너레이터다.

     ```python
     list(range(10))
     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
     
     list(reversed(range(10)))
     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
     ```

     <br>

### **5. 사전(dict)**

- 파이썬 내장 자료구조 중에서 **가장 중요**

- 일반적으로 **해시맵** 또는 **연관 배열**이라 알려져 있다.

- 유연한 크기를 가지는 **(key, value)** 쌍으로 키와 값은 모두 파이썬 객체

- 중괄호 {}를 사용, 콜론으로 키와 값을 구분

  ```python
  empty_dict = {}
  
  d1 = {'a' : 'value', 'b' : [1, 2, 3, 4]}
  
  d1
  # {'a' : 'value', 'b' : [1, 2, 3, 4]}
  ```

- 일정 기준으로 정렬되어 있지 않다.

- **update** 메서드를 통해 하나의 사전을 다른 사전과 합칠 수 있다.

  - 이미 존재하는 key에 대해 update를 호출하면 이전 value는 사라진다(덮어쓰기)

- **유효한 사전 키**

  - value는 어떤 파이썬 객체라도 가능
  - key는 스칼라형이나 튜플 처럼 값이 바뀌지 않는 객체만 가능(해시 가능해야 함)

<br> 

### **6. 집합**

- 유일한 원소만 담는 정렬되지 않은 자료형

- 사전과 유사, 값은 없고 키만 가지고 있다.

- 생성 방법

  1. set 함수를 이용하서 생성

  2. 중괄호를 이용해서 생성

     ```python
     set([2, 2, 2, 1, 3, 3])
     # {1, 2, 3}
     
     {2, 2, 2, 1, 3, 3}
     # {1, 2, 3}
     ```

- 합집합(union), 교집합(intersection), 차집합(difference_update), 대칭차집합(symmetric_difference) <br>같은 **산술 집합 연산**을 제공