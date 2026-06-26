# 파이썬 리스트

## 리스트란?
파이썬 리스트는 여러 값을 순서대로 저장하는 자료형입니다. 여러 종류의 값을 한 번에 다룰 수 있고, 내용을 바꾸는 것도 가능합니다.

## 만들기
리스트는 대괄호 `[]`를 사용해 만듭니다.

```python
numbers = 
fruits = ['apple', 'banana', 'cherry']
mixed = [1, 'hello', 3.14, True]
```

## 특징
- 순서가 있습니다.
- 중복 값을 허용합니다.
- 값을 변경할 수 있습니다.
- 여러 자료형을 함께 넣을 수 있습니다.

## 인덱스 접근
리스트의 각 요소는 인덱스로 접근합니다. 인덱스는 0부터 시작합니다.

```python
items = ['a', 'b', 'c']
print(items)  # a
print(items)  # c
print(items[-1]) # c
```

## 슬라이싱
일부 구간만 잘라서 가져올 수 있습니다.

```python
items = 
print(items[1:4])
print(items[:3])
print(items[::2])
```

## 자주 쓰는 메서드
- `append()`: 마지막에 요소 추가
- `insert()`: 원하는 위치에 요소 추가
- `remove()`: 값으로 요소 삭제
- `pop()`: 인덱스로 요소 삭제 후 반환
- `sort()`: 정렬
- `reverse()`: 순서 뒤집기
- `clear()`: 모든 요소 삭제

```python
nums = 
nums.append(4)
nums.insert(1, 10)
nums.remove(2)
last = nums.pop()
nums.sort()
nums.reverse()
```

## 자주 쓰는 함수
- `len()`: 길이
- `max()`: 최댓값
- `min()`: 최솟값
- `sum()`: 합계

```python
nums = 
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
```

## 반복문과 함께 사용
리스트는 `for`문과 함께 자주 사용합니다.

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

## 리스트 컴프리헨션
짧고 간단하게 리스트를 만들 수 있습니다.

```python
squares = [x * x for x in range(5)]
```

## 예시
```python
students = ['철수', '영희', '민수']
students.append('지수')
print(students)
print(students)
```

## 주의할 점
- 인덱스를 잘못 쓰면 에러가 납니다.
- 리스트 안의 리스트도 만들 수 있습니다.
- `append()`는 새 리스트를 만드는 것이 아니라 기존 리스트를 바꿉니다.

## 정리
파이썬 리스트는 가장 많이 쓰이는 자료형 중 하나입니다. 순서가 있고 수정할 수 있어서 데이터를 모아 다루기에 편리합니다.
