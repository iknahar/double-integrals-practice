# Exercises

Draw the region before you write any limits. Check every answer in SymPy.

### 0. The station, with different waits

You wait 10 minutes and your friend waits 20 (whoever arrives first waits their own time).
Both arrive at random between 5:00 and 6:00. What is the chance you meet?

<details><summary>Answer</summary>

You meet if your friend arrives no more than 10 minutes after you, or you arrive no more than
20 minutes after your friend. The two missed corners are triangles with legs 50 and 40
minutes: (50² + 40²) / 2 / 60² = 4100 / 7200. So you meet with chance 1 − 0.569 = 0.431.

```python
import numpy as np
rng = np.random.default_rng(0)
you, friend = rng.uniform(0, 60, size=(2, 1_000_000))
gap = friend - you
print(np.mean((gap <= 10) & (gap >= -20)))   # about 0.43
```
</details>

### 1. The running-late hill again

For f(x, y) = x + y on the unit square, find P(X < Y).

<details><summary>Answer</summary>

The region is the triangle above the diagonal. With x outside: x from 0 to 1, y from x to 1.
The integral is 1/2. By symmetry of x + y in x and y this had to be the case.

```python
import sympy as sp
x, y = sp.symbols("x y", real=True)
print(sp.integrate(x + y, (y, x, 1), (x, 0, 1)))   # 1/2
```
</details>

### 2. Between two curves

Integrate f(x, y) = 1 over the region between y = x² and y = x for 0 < x < 1.
Then write the same integral with y on the outside.

<details><summary>Answer</summary>

x outside: y runs from x² to x, area 1/6.
y outside: y runs from 0 to 1, and x runs from y to √y. Same answer, 1/6.
</details>

### 3. Find the constant

f(x, y) = c(x + 2y) on the unit square. Find c.

<details><summary>Answer</summary>

The volume is c · 3/2, so c = 2/3.
</details>

### 4. A marginal on a triangle

For f(x, y) = 2 on 0 < x < y < 1, find f_X(x) and f_Y(y). Are X and Y independent?

<details><summary>Answer</summary>

f_X(x) = 2(1 − x), f_Y(y) = 2y. Their product is 4y(1 − x), not 2, and the region is a
triangle, so they are dependent. (This density describes the smaller and larger of two
random numbers between 0 and 1.)
</details>

### 5. Swap to escape

Evaluate the double integral of sin(y²) over the triangle 0 < x < y < √π. Try it first with
x on the outside (x from 0 to √π, y from x to √π), then swap.

<details><summary>Answer</summary>

Stuck as written. Swap: y from 0 to √π, x from 0 to y. The inner integral gives y·sin(y²),
and the outer one gives (1 − cos π)/2 = 1.
</details>

### 6. Polar

A dart lands uniformly on a disk of radius 1. What is the chance its distance from the
centre is less than 0.9? Less than 0.1?

<details><summary>Answer</summary>

The distance has density 2r, so P(R < a) = a². That gives 0.81 and 0.01.
</details>

### 7. Numerical check

Use `dblquad` to integrate x · y² over x from 0 to 1 and y from 0 to 2. Then pass a function
written as `lambda x, y: x * y**2` instead and compare.

<details><summary>Answer</summary>

The right order gives 4/3 ≈ 1.3333. The swapped one silently gives 2/3 ≈ 0.6667.
</details>
