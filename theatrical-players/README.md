# Theatrical Players Refactoring Kata

From Martin Fowler's [Refactoring, 2ed](https://martinfowler.com/books/refactoring.html) chapter 1. The goal is to refactor `statement()` function so that it is easier to add new features like generating an html report or supporting new types of plays.

This is a slightly modified (without `approvaltests` dependency) Python version from [Emily Bache's github](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata/tree/main/python).


# Getting started

Assuming you have `pytest`, and `pytest-cov` installed in your virtual environment.

```
make test
make htmlcov
open htmlcov/index.html
```

