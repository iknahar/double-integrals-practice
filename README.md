# Double integrals and joint distributions, practice code

Runnable Python for learning double integrals through one example: where a dart lands.
A landing spot is two numbers, their crowding is a hill (the joint density), and a
probability is the volume under that hill over some region.

Every script is short, prints its answers, and matches a code block from the companion post on Medium.

| script | what it shows |
|---|---|
| `01_practice_board.py` | slicing a volume into an inner and outer integral, f(x, y) = x + y |
| `02_round_board_limits.py` | inner limits that depend on x, and what lazy square limits cost |
| `03_swap_the_order.py` | an integral that is stuck one way and one line the other way |
| `04_when_order_lies.py` | a function where swapping the order flips the answer |
| `05_marginal_conditional.py` | normalising a density, marginals, and a conditional slice |
| `06_expectation_covariance.py` | averages and covariance as double integrals |
| `07_polar_jacobian.py` | the Jacobian r, and why random darts favour the outer half |
| `08_numerical.py` | `scipy.integrate.dblquad` and Monte Carlo darts |
| `09_box_muller.py` | bonus: two flat random numbers become two bell-shaped ones |

## Setup

```bash
python -m pip install -r requirements.txt
```

```bash
python 01_practice_board.py
```

## Practice

Try the questions in [exercises.md](exercises.md). Answers are folded under each question.

## One trap worth remembering

`scipy.integrate.dblquad(func, a, b, gfun, hfun)` calls `func(y, x)`, with y first.
`a` and `b` are the limits for x, and `gfun`, `hfun` are the limits for y written as
functions of x. Swapping the argument order raises no error, it just gives a wrong number.
