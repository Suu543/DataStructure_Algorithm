# Introduction

1. What are Data Structures?
2. What is an algorithm?

4. Why are Data Structures and Algorithms important?
5. Types of Data Structures
6. Types of Algorithms

## What are Data Structures?

![img](https://cdn-images-1.medium.com/max/1000/1*ghaexfk3elgiVNOBvuUGYA.png)

왼쪽 사진 처럼 정리되지 않은 채 나열되어있는 나무조각 더미에서 빨간색 나무 조각을 찾는 것은 쉽지않다. 반면에, 오른쪽 사진 처럼 색깔별로 나무 조각을 분류해 정리하면 손쉽게 원하는 나무 조각을 찾을 수 있다.

이 나무 조각을 정리하는 논리를 컴퓨터를 사용하면서 발생하는 많은 양의 데이터에 적용해보면, 왼쪽 사진과 같이 특정한 기준 없이 무작위로 나열된 데이터를, 오른쪽 처럼 특정 규칙에 맞게 정리해 적절하고, 지연없이 사용할 수 있게 된다. 자료 구조는 말 그대로 자료를 구조화 하는 방식이다.

**실생활 예시를 통해 알아보자**

![img](https://cdn-images-1.medium.com/max/1000/1*NXz8voZfvqpuW6a2-fTtzQ.png)

이 사진은 컴퓨터 자료 구조에 존재하는 `Queue`라는 개념이다.

`Queue`는 `FIFO (First In First Out) ` 방식으로 동작한다. 왼쪽과 같이 순서없이 많은 사람들이, 오른쪽과 같이 줄을 서 어떤 장소에 들어가려 할 때, 줄 제일 앞에 위치한 사람이 제일 먼저 특정 장소로 들어갈 수 있음을 의미한다. 

![img](https://cdn-images-1.medium.com/max/1000/1*sZwLlXXRNoM98-FiYJV8cw.png)

이 사진은 컴퓨터 자료 구조에 존재하는 `Stack`라는 개념이다.

`Stack`은 `LIFO (Last In First Out)` 방식으로 동작한다. 왼쪽과 같이 책을 쌓지 않고, 어질러 놓으면 한 번에 여러 권의 책을 옮기기 힘들다. 하지만, 오른쪽 그림과 같이 책을 쌓으면 한 번에 여러 책을 운반할 수 있다. 여기서 주목 할 점은 제일 밑에 있는 책이 제일 처음에 집은 책이지만, 도서관에가서 반납할 때, 제일 마지막에 쌓은, 제일 위의 책을 가장 먼저 반납함을 의미한다.

현실 세계의 예시 처럼, 자료 구조는 컴퓨터 세계에서 데이터가 같은 시간안에 조금 더 효율적이고 빠르게 다뤄질 수 있도록 해주는 지혜와 같다 생각할 수 있다.

## What is an Algorithm?

![img](https://cdn-images-1.medium.com/max/1000/1*b_eYSdYqY46JNFaSRY3VuQ.png)

알고리즘은 한 문제를 해결하기 위한 논리 과정이라 생각할 수 있다.

현실 세계 예시를 조금 더 생각해보자

**출근**

1. 버스 정류장에 간다
2. 버스를 탄다
3. 사무실에 간다

**커피숍**

1. 커피숍에 간다
2. 커피를 선택한다
3. 커피 값을 지불한다
4. 커피를 받는다

![img](https://cdn-images-1.medium.com/max/1000/1*BE3yuGGVuK7BlBw5lOUL4Q.png)

#### Google, Facebook과 같은 회사는 어떤 알고리즘을 이용해 라이브 비디오를 전송할까?

![FireShot Capture 475 - The Complete Data Structures and Algorithms Course in Python - Udemy_ - www.udemy.com](C:\Users\jos50\Downloads\FireShot\FireShot Capture 475 - The Complete Data Structures and Algorithms Course in Python - Udemy_ - www.udemy.com.png)



![img](https://cdn-images-1.medium.com/max/1000/1*reldIevsA1_rd4DhfR7ufQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*HgTcPtZcsCaeqqVbl7tUdw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*md8U0rIjfXNqpqC3sqrhyw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*woPYtSNYv9qDRaq5IOGjkQ.png)

#### What makes a good algorithm?

1. Correctness
2. Efficiency

## Why are Data Structures and Algorithms important?

![img](https://cdn-images-1.medium.com/max/1000/1*H9gS9cqFscNg0DMrjIKzPg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*dStcXWRWYOhINb_SMRg4wQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*UXQ8ALDmtajVCcCNK46Bng.png)

#### Why are Data Structures and Algorithms in Interviews?

1. Problem Solving Skills
2. Fundamental concepts of programming in limited time

## Types of Data Structures

![img](https://cdn-images-1.medium.com/max/1000/1*83hqqHHie1V79USRJPYO6w.png)

## Types of Algorithms

- Simple Recursive algorithms
  - Fibonacci
- Divide and conquer algorithms
  - Divide the problem into smaller subproblems of the same type, and solve these subproblems recursively.
  - Combine the solutions to the subproblems into a solution to the original problem
  - Examples: Quick sort and merge sort
- Dynamic programming algorithms
  - They work based on memoization (remember past result)
  - To find the best solution
- Greedy algorithms
  - We take the best we can without worrying about future consequences
  - We hope that by choosing a local optimum solution at each step, we will end up at a global optimum solution
- Brute force algorithms
  - It simply tries all possibilities until a satisfactory solution is found
- Randomized algorithms
  - Use a random number at least once during the computation to make a decision

**Questions**

1. Why do we need data structures and algorithms?

- To develop memory and time efficient applications

2. What is primitive data structure?

- Built-in data structures in any given programming languages

















