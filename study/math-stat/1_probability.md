# 확률의 성질
### 확률 Probability
여러 가능한 결과 중 일부분이 일어날 가능성을 0과 1 사이 값으로 나타낸 것

### 시행 Trial, 실험 Experiment
여러 가능한 결과 중 하나가 일어나도록 하는 행위

### 표본 공간 Sample space
시행에서 나타날 수 있느 모든 결과를 모아 놓은 집합

### 사건 Event
표본 공간의 부분집합

### 확률의 3요소
$$ \Omega$: 표본공간, A: 사건, P: 확률 $$
$$ (\Omega, A, P) $$

### 배반 Disjoint
서로 다른 i 와 j 에 대하여 ${A_i\cap}A_j = \varnothing$

### 확률의 공리
1. 모든 사건 A 에 대하여 $0 \leq P(A) \leq 1$ 이다.
2. 표본 공간 $\Omega$ 에 대하여 $P(\Omega) = 1$ 이다.
3. 사건 ${A_1, A_2, \cdots}$ 이 서로 배반일 때 다음이 성립한다.

$$ P(\bigcup_{i=1}^\infty A_i) = \sum_{i=1}^\infty P(A_i) $$


#### Proof $P(\varnothing) = 0$

$$A_1 = \Omega, A_2 = A_3 = \cdots = \varnothing \\ \implies$$
$$P(\Omega) = P(A_1) + \sum_{i=2}^\infty P(A_i) \\ = P(\Omega) + \sum_{i=2}^\infty P(\varnothing)$$
$$P(\Omega) = 1$$
$$\blacksquare$$

#### Proof $P(\bigcup\limits_{i=1}^n A_i) = \sum\limits_{i=1}^n P(A_i)$

$$A_{n+1} = A_{n+2} = \cdots = \varnothing \\ \implies$$
$$\bigcup_{i=1}^\infty A_i = (\bigcup_{i=1}^n A_i) \cup (\bigcup_{i=n+1}^\infty A_i) \\ = (\bigcup_{i=1}^n A_i) \cup (\bigcup_{i=n+1}^\infty \varnothing) \\ = \bigcup_{i=1}^n A_i$$
$$\sum_{i=1}^\infty P(A_i) = \sum_{i=1}^n P(A_i) + \sum_{i=n+1}^\infty P(A_i) \\ =  \sum_{i=1}^nP(A_i) + \sum_{i=n+1}^\infty P(\varnothing) \\ = \sum_{i=1}^n P(A_i) \because P(\varnothing) = 0$$
$$\blacksquare$$

### Theorem 1.1
#### (i) $P(A^c) = 1 - P(A)$
$$P(\Omega) = P(A \cup A^c) \because A \cup A^c = \Omega \\ = P(A) + P(A^c) \because A \cap A^c = \varnothing$$
$$\blacksquare$$

#### (2) $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
$$A \cup B = A \cup (A^c \cap B)$$
$$P(A \cup B) = P(A) + P(A^c \cap B) \because A \cap (A^c \cap B) = \varnothing$$
$$B = (A \cap B) \cup (A^c \cap B)$$
$$P(B) = P(A \cap B) + P(A^c \cap B) \because (A \cap B) \cap (A^c \cap B) = \varnothing$$
$$\blacksquare$$

#### (3) $A \subset B \implies P(A) \leq P(B)$
$$B = (A \cap B) \cup (A^c \cap B) \\ = A \cup (A^c \cap B) \because A \subset B$$
$$P(B) = P(A) + P(A^c \cap B)$$
$$P(A^c \cap B) \ge 0$$
$$\blacksquare$$
