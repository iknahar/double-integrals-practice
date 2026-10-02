# Double integrals and joint distributions, practice code

Runnable Python for learning double integrals through one everyday question: if two friends
arrive at a station at random times within the same hour and each waits 15 minutes, how often
do they meet? Two random numbers make a square (or a hill), and a probability is the volume
over a region of it.

Every script is short, prints its answers, and matches a code block from the companion post on Medium.

| script | what it shows |
|---|---|
| `01_running_late_slices.py` | slicing a volume into an inside and outside integral, f(x, y) = x + y |
| `02_station_corners.py` | meeting a friend within 15 minutes: 7/16, from two corner triangles |
| `03_round_board_limits.py` | inner limits that depend on x, and what lazy square limits cost |
| `04_swap_the_order.py` | an integral that is stuck one way and one line the other way |
| `05_when_order_lies.py` | a function where swapping the order flips the answer |
| `06_marginal_conditional.py` | normalising a density, marginals, and a conditional slice |
| `07_expectation_covariance.py` | averages and covariance as double integrals |
| `08_polar_jacobian.py` | the Jacobian r, and why random darts favour the outer half |
| `09_wait_for_a_coin_flip.py` | how long two people must wait for a 50/50 chance of meeting |
| `10_numerical.py` | `scipy.integrate.dblquad` and a Monte Carlo simulation of the station |

## Setup

```bash
python -m pip install -r requirements.txt
```

```bash
python 02_station_corners.py
```

## Practice

Try the questions in [exercises.md](exercises.md). Answers are folded under each question.

## One trap worth remembering

`scipy.integrate.dblquad(func, a, b, gfun, hfun)` calls `func(y, x)`, with y first.
`a` and `b` are the limits for x, and `gfun`, `hfun` are the limits for y written as
functions of x. Swapping the argument order raises no error, it just gives a wrong number.
