# Practice Sessions

Coding questions asked by Claude in interactive practice sessions, separate
from the main LeetCode solutions in the repo root.

## Structure

One directory per question, numbered in the order asked:

```
q<n>_<slug>/
    problem.md   # question, examples, expected output
    main.py      # function stub + inline test cases (print calls with
                 # expected output in comments)
```

## Conventions

- Functions `return` their result — never `print` inside the function
  itself; `print()` is only used at the bottom to call the function against
  test cases.
- Solutions are written by the user; Claude reviews and gives hints rather
  than writing the fix directly.
- The full list of questions asked (and ideas for future ones) is tracked
  in [`solutions/Practice Questions.md`](../solutions/Practice%20Questions.md)
  — check it before asking a new question so nothing repeats.

## Topics covered so far

Basic string/array manipulation (Q1–Q11), then recursion (Q12 Fibonacci,
Q13 Factorial — each solved recursively, with Q13 also solved iteratively
for comparison).
