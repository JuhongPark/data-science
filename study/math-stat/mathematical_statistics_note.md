# Mathematical Statistics Note

# Probability Distribution

## 베르누이분포, Bernoulli

$X \sim Bernoulli(p) \\
p_X(x) = p^x{(1-p)}^{1-x}, x = 0, 1 \\
E(X) = p \\
Var(X) = p(1-p) \\
M(t) = 1-p+pe^t$

## 이항분포, Binomial

$X \sim B(n, p) \\
p_X(x) = \binom nx p^x{(1-p)}^{n-x}, x = 0, 1, \cdots, n \\
E(X) = np \\
Var(X) = np(1-p) \\
M(t) = {(1-p+pe^t)}^n$

## 기하분포, Geometric

확률 p로 반복 시행시, 첫번째 성공까지의 총 시행 횟수

$X \sim Geo(p) \\
p_X(x) = (1-p)^{x-1}p, x = 0, 1, \cdots \\
E(X) = \frac1p \\
Var(X) = \frac{1-p}{p^2} \\
M_X(t) =\frac{pe^t}{1-(1-p)e^t}$

- Properties

    $\frac1{1-p} = 1 + p + p^2 + \cdots$

## 음이항분포, Negative Binomial

확률 p 로 반복 시행시, r번째 성공까지의 총 시행 횟수

$X \sim NB(r, p) \\
p_X(x) = \binom{x-1}{r-1}p^r{(1-p)}^{x-r}, x=r, r+1, \cdots \\
E(X) = \frac rp \\
Var(X) = \frac{r(1-p)}{p^2} \\
M_X(t)= (\frac{pe^t}{1-e^t(1-p)})^r, t<-log(1-p)$

## 초기하분포, Hypergeometric

n(A) = N_1, n(B) = N_2 에서 n 개 선택시 A에서 선택되는 개수

$X \sim Hypergeometric(N_1 + N_2, N_1, n) \\
p(x) = \frac{\binom {N_1}x \binom{N_2}{n-x}}{\binom {N_1 + N_2}n}, x 
\in (0, 1, \cdots, n) \\
E(X) = n\frac{N_1}{N_1+N_2}$

- Properties

    $N_1+N_2 >> n \Rightarrow B(n, \frac {N_1}{N_1 + N_2})$

## 포아송분포, Poisson

$\lambda$만큼 단위당 평균 사건시, 사건 발생 횟수

$X \sim Pois(\lambda) \\
p_X(x) = \frac{\lambda^x e^{-\lambda}}{x!}, x = 0, 1, \cdots \\
E(X) = \lambda \\
Var(X) = \lambda \\
M(t) = e^{\lambda(e^t -1)}$

- 포아송 가정
    1. 아주 짧은 구간에서 사건 2회 발생 확률 = 0
    2. 아주 짧은 구간 h에서 사건 발생 확률 $\propto$ 구간 길이($\lambda h$)
    3. 서로 다른 구간 발생 사건 횟수는 독립
- Properties

    $Pois(\lambda_1) + Pois(\lambda_2) \sim Pois(\lambda_1 + \lambda_2) \\
    Pois(\lambda) \sim \lim\limits_{n\to\infty}B(n, \frac \lambda n) = \lim\limits_{n\to\infty}B(n, p =\frac \lambda n) \\
    \text{t 단위당 사건 횟수 }Pois(\lambda t) \\
    np = \lambda, n >> p \Rightarrow Pois(\lambda) = \frac{(np)^x e^{-np}}{x!} \approx {_n}C_xp^x(1-p)^{n-x} \sim B(n, p)$

    - $e^k = \sum\limits_{i=0}^\infty \frac{k^i}{i!}$

## 연속균등분포, Continuous Uniform

$X \sim U(a, b) \\
f_X(x) = \frac1{b-a}, a \le x \le b \\
F_X(x) = \frac{x-a}{b-a}, a \le x \le b \\
E(X) = \frac{a+b}2 \\
Var(X) = \frac{(b-a)^2}{12} \\
M(t) = \frac{e^{bt}-e^{at}}{(b-a)t}, t\ne 0$

## 지수분포, Exponential

첫번째 사건 혹은 사건 간의 대기시간

$X \sim \text{Exp}(\theta), \text{Exp}(\frac1\lambda) \\
f_X(x) = \frac1\theta {e^{-\frac x\theta}} = \lambda e^{-\lambda x}, 
\theta \gt 0, \lambda \gt 0, x \gt 0 \\
F_X(x) = 1 - e^{-\frac x\theta} = 1 - e^{-\lambda x} \\
E(X) = \theta = \frac1\lambda \\
Var(X) = \theta^2 = \frac1{\lambda^2} \\
M(t) = \frac 1{1-\theta t} = \frac\lambda{\lambda - t},  t \lt \frac1
\theta, t \lt \lambda$

- Memoryless Property, 비가역성

    $P(X \gt t + s \vert X \gt s) = P(X \gt t)$

## 감마분포, Gamma

$\alpha$번 사건까지의 대기 시간

$X \sim \Gamma(\alpha, \beta), \Gamma(\alpha, \frac1\lambda) \\
f(x) = \frac1{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1} e^{-\frac x{\beta}} = \frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1} e^{-\lambda x}, \alpha \gt 0, 
\beta \gt 0, \lambda \gt 0, x \gt 0 \\
E(X) = \alpha\beta = \frac\alpha\lambda \\
Var(X) = \alpha\beta^2 = \frac\alpha{\lambda^2} \\
M(t) = (\frac1{1- \beta t})^\alpha = (\frac\lambda{\lambda - t})^\alpha, t \lt \frac1\beta, t \lt \lambda$

- Properties

    $\alpha: 형상모수, shape parameter \\
    \beta, \frac1\lambda: 척도모수, scale parameter \\
    \Gamma(1, \theta) \sim \text{Exp}(\theta), \Gamma(1, \frac1\lambda) \sim \text{Exp}(\frac1\lambda) \\
    \Gamma(\alpha_1, \theta) + \Gamma(\alpha_2, \theta) \sim \Gamma(\alpha_1 + \alpha_2, \theta), \Gamma(\alpha_1, \frac1\lambda) + \Gamma(\alpha_2, \frac1\lambda) \sim \Gamma(\alpha_1 + \alpha_2, \frac1\lambda) \\
    \Gamma(n, \theta) \sim \text{Pois}(\frac1\theta), \Gamma(n, \frac1\lambda) \sim \text{Pois}(\lambda)\text{에서 n번째 사건까지의 대기 시간}$

- 감마 함수

    $\alpha \gt 0, n \in \N \\
    \Gamma(\alpha) = \int\limits_0^\infty y^{\alpha-1}e^{-y}dy \\
    \Gamma(\alpha + 1) = \alpha\Gamma(\alpha) \\
    \Gamma(n) = (n-1)! \\
    \Gamma(1) = 1, \Gamma(\frac12) = \sqrt{\pi}$

## 카이제곱분포, Chi Square

$X \sim \chi^2(n), n \in N \\
f(x) = \frac1{\Gamma(\frac n2)2^\frac n2}x^{\frac n2-1} e^{-\frac x2}, x \gt 0 \\
E(X) = n \\
Var(X) = 2n \\
M(t) = {(\frac1{1 - 2t})}^{\frac n2}, t \lt \frac 12$

- Properties

    $자유도 n \\
    \chi^2(n) \sim \Gamma(\frac n2, 2) \\
    \chi^2(n_1) + \chi^2(n_2) \sim \chi^2(n_1 + n_2) \\
    X \sim N(\mu, \sigma^2) \Rightarrow \frac{(n-1)s^2}{\sigma^2} \sim \chi^2(n-1)$

## 정규분포, Normal

$X \sim N(\mu, \sigma^2) \\
f(x) = \frac1{\sqrt{2\pi\sigma^2}}e^{-\frac {(x-\mu)^2}{2\sigma^2}}, -\infty \le \mu \le \infty, \sigma^2 \gt 0, -\infty \lt x \lt \infty \\
E(X) = \mu \\
Var(X) = \sigma^2 \\
M(t) = e^{\mu t + \frac12 \sigma^2 t^2} \\
skew(X) = 0 \\
kurt(X) = 0$

- Properties

    $N(\mu_1, \sigma^2_1) + N(\mu_2, \sigma^2_2) \sim N(\mu_1 + \mu_2, \sigma^2_1 + \sigma^2_2)\text{ if independent }\bar X \sim N(\mu , \frac{\sigma^2}n) \\
    X \sim N(\mu, \sigma^2), \sigma\text{를 아는 경우 }\Rightarrow \frac{\bar X - \mu}{\alpha / \sqrt n} \sim N(0, 1) \\
    X \sim N(\mu, \sigma^2), \sigma\text{를 모르는 경우 }\Rightarrow \frac{\bar X - \mu}{s / \sqrt n} \sim t(n-1)$

## 표준정규분포, Standard Normal

$X \sim N(0, 1) \\
E(X) = 0 \\
Var(X) = 1 = E(X^2) \\
E(X^3) = 0 \\
E(X^4) = 3 \\
M(t) = e^{\frac12 t^2} \\
skew(X) = 0 \\
kurt(X) = 0 \\
\Phi(z) = \int_{-\infty}^z \frac1{\sqrt{2\pi}}e^{-\frac12 x^2}dx \\
Z^2 \sim \chi^2(1)$

## t 분포

$T(n) \sim \frac Z{\sqrt{\chi^2(n)/n}}$

- Properties

    $자유도 n \\
    {t(n)}^2 \sim F(1, n)$

- t Test

    $\text{분산이 같은 정규분포를 따르는 두집단의 모평균 비교} \\
    t_{\frac\alpha2}(n_1 + n_2 - 2) = \frac{\vert\bar X-\bar Y \vert}{s_p\sqrt{\frac1{n_1}+\frac1{n_2}}}, S_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2}$

## F 분포

$F = \frac{\chi^2(m)/m}{\chi^2(n)/n} \sim F(m, n)$

- Properties

    $자유도 (m, n) \\
    {F(m, n)}^{-1} \sim F(n, m) \\
    X_1 \sim N(\mu_1, \sigma_1^2), X_2 \sim N(\mu_2, \sigma_2^2) \Rightarrow \frac{s_1^2/\sigma_1^2}{s_2^2/\sigma_2^2} \sim F(n_1-1, n_2-1)$

# Useful Equation

## Taylor Series

$e^x = \sum\limits_{n=0}^\infty \frac{x^n}{n!} \\
\frac1{1-x} = \sum\limits_{n=0}^\infty x^n \\
\frac1{(1-x)^2} = \sum\limits_{n=1}^\infty nx^{n-1}$