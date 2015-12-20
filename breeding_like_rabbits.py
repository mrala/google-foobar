#!/usr/bin/env python
"""
Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits! But
instead of following the Fibonacci sequence like all good rabbits do,
the zombit population changes according to this bizarre formula, where
R(n) is the number of zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program with only
one zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman, a bunch of
Professor Boolean's minions passed the time by playing a guessing game:
when will the zombit population be equal to a certain amount? Then, some
clever minion objected that this was too easy, and proposed a slightly
different game: when is the last time that the zombit population will
be equal to a certain amount? And thus, much fun was had, and much
merry was made.

(Not in this story: Professor Boolean later downsizes his operation,
and you can guess what happens to these minions.)

Write a function answer(str_S) which, given the base-10 string
representation of an integer S, returns the largest n such
that R(n) = S. Return the answer as a string in base-10 representation.
If there is no such n, return "None". S will be a positive integer no
greater than 10^25.

Test cases
==========

Inputs:
    (string) str_S = "7"
Output:
    (string) "4"

Inputs:
    (string) str_S = "100"
Output:
    (string) "None"
"""
r = dict(enumerate([1, 1, 2]))

def R(n):
    if n not in r:
        t = n // 2
        if n == 2 * t:
            r[n] = R(t) + R(t + 1) + t
        else:
            r[n] = R(t - 1) + R(t) + 1
    return r[n]

def search(dist, S):
    start, end = 0, S
    while start <= end:
        mid = (start + end) // 2
        value = R(dist(mid))
        if value == S:
            return mid
        if value < S:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def answer(str_S):
    S = int(str_S)
    odd = search(lambda x: x * 2 + 1, S) * 2 + 1
    even = search(lambda x: x * 2, S) * 2
    if even < 0:
        a = None if odd < 0 else odd
    elif odd < 0:
        a = even
    else:
        a = max(even, odd)
    return str(a)
