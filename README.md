# Puzzles

Solutions to various math and programming puzzles I find interesting — mostly
[The Fiddler on the Proof](https://thefiddler.substack.com/), Zach Wissner-Gross's weekly
puzzle column, the monthly [Jane Street Problem](https://www.janestreet.com/puzzles/current-puzzle/), or the monthly [IBM Ponder This Puzzle](https://research.ibm.com/labs/israel/ponder-this#current-challenge--solution). Each notebook works a puzzle end to end: the problem statement, the actual solution methodology
(usually with LaTeX, but sometimes a hurried screenshot of scratch work 😅), and sometimes code when an analytic solution escapes me. Some puzzles that I found particularly interesting can be seen on [my puzzle blog](https://ccolombe12.github.io).
> **NOTE**: This is a WIP from the scrappy folder on my device and I cannot guarantee all puzzles have a solution at the moment, or are the best quality. This will improve as time goes on! 




## Index

Newest first. Dates are roughly the puzzle's publication date.

| Date | Source | Puzzle | What's in it |
| --- | --- | --- | --- |
| 2026-09-14 | Fiddler | [Can you cheat on the quiz?](Fiddler/can_you_cheat_on_quiz.ipynb) | Propagating the distribution of correct answers along a chain of quiz questions as a Markov process; which question to reveal to maximize your score |
| 2026-04-17 | Fiddler | [Fizz buzz](Fiddler/2026-04-17-Fizz_buzz/fizz_buzz_puzzle.ipynb) | Counting the `n ≤ 100` that BUZZ (divisible by 7, or containing the digit 7) — 30 of them — with an inclusion–exclusion cross-check |
| 2026-04-10 | Fiddler | [Number cubes](Fiddler/2026_04_10-number_cubes/number_cubes.ipynb) | Digits on three dice (6 and 9 interchangeable): proving 776 is the best reachable target, then counting the 855 distinct die "types" that reach it |
| 2026-02-16 | Fiddler | [Circle cycle](Fiddler/circle_cycle.ipynb) | Walking three great-circle legs of equal length `s` on a sphere and returning to the start — equilateral spherical triangles |
| 2026-01-30 | Fiddler | [Hexagonal frog](Fiddler/hexagonal_frog.ipynb) | BFS on a hex lattice where each hop must increase the angle swept, then simulating how food spreads over time |
| 2026-01-23 | Fiddler | [Bingo](Fiddler/Bingo.ipynb) | Expected number of calls to reach BINGO on an `N × N` board when only tiles on your board are called |
| 2026-01-12 | Fiddler | [Coffee/tea mix](Fiddler/coffee_tea_mix.ipynb) | Minimizing the coffee remaining in one cup over a sequence of pours between two cups (including the harder variant where you can't pour down the sink) |
| 2025-12-26 | Fiddler | [Magic square](Fiddler/magic_square.ipynb) | Which sizes `N` admit a magic square of distinct primes summing to 2026 — only `N = 4, 6, 8` |
| 2025-12-15 | Fiddler | [Tower topple](Fiddler/tower_topple.ipynb) | The overhang length `L` at which a stacked tower tips, via its horizontal center of mass |
| 2025-12-07 | Fiddler | [Apollonian gasket](Fiddler/apolloian_gasket.ipynb) | Maximizing the total area of the circles you land inside within an Apollonian gasket |
| 2025-11-29 | Fiddler | [Minimal spanning triples](Fiddler/2025_11_29.ipynb) | Counting ordered triples whose subset sums cover every value in `[T]` — 8 tuples for `T = 10`, 1014 for `T = 100` |
| 2025-11-07 | Fiddler | [Randy Hall](Fiddler/Randy_hall.ipynb) | A Monty Hall variant solved as a Markov chain: first the aperiodic recurrent case, then a 6-state periodic one |
| 2025-11-03 | Fiddler | [Probability swing](Fiddler/probability_swing.ipynb) | DP for the probability of winning a best-of-`N` series, then the large-`N` limit (with a companion [Mathematica notebook](Fiddler/probability_swing.nb)) |
| 2025-10-20 | Fiddler | [Expected distance to edge](Fiddler/expected_dist_to_edge.ipynb) | Expected distance from the center to the boundary in a uniformly random direction, for a square and then a cube |
| 2025-10-10 | Fiddler | [Tic tac toe](Fiddler/Tic_tac_toe.ipynb) | Probability of completing three in a row given `N` rolls, using bitmask states and exact `Fraction` arithmetic |
| 2025-09-26 | Fiddler | [Fiddler risk](Fiddler/fiddler_risk.ipynb) | Risk-style card draws: expected number of cards needed for a matched set, with wildcards |
| 2025-09-20 | Fiddler | [Expected team score](Fiddler/expected_team_score.ipynb) | Expected length of the longest increasing subsequence of a random permutation, brute-forced over all `N!` orderings for `N ≤ 10` |
| 2025-08-24 | Fiddler | [How far can you run before sundown?](Fiddler/How_far_can_you_run_before_sundown.ipynb) | Maximizing distance covered in 65 minutes over 1- and 3-mile loops, with and without a mulligan |
| 2025-07-04 | Fiddler | [Flag triangles](Fiddler/2025_07_04.ipynb) | Counting equilateral triangles (126) and parallelograms (5918) among the star points of the American flag |
| 2025-06-27 | Fiddler | [Roman numeral combos](Fiddler/Roman_numeral_combos.ipynb) | DP counting the ways to write a Roman-numeral string as a concatenation of valid numerals |
| 2025-06-15 | Fiddler | [Race to zero](Fiddler/race_to_zero.ipynb) | A runner who speeds up by `α`% at each halfway point; deriving the continuous speed function and the finishing time |
| 2025-06-08 | Fiddler | [Bubble squeeze](Fiddler/Bubble_squeeze.ipynb) | Greedy circle packing on a hexagonal lattice: exact union area for `N = 7` (`2π + 3√3`), then the large-`N` limit |
| 2025-05-23 | Fiddler | [Fiddlerish rivers](Fiddler/2025_05_23.ipynb) | Probability that the `i`-th character of a line of Fiddlerish is a space via `P_i = ½P_{i−4} + ½P_{i−5}`, then the expected length of a vertical "river" of spaces |
| 2025-05-09 | Fiddler | [Sweep or Game 7](Fiddler/2025_05_09-sweep_or_game7/2025_05_09-fiddler.ipynb) | The range of `p` for which a 7-game series is most likely to end in exactly 5 games, then sweep-vs-Game-7 odds for `p ~ U[3/5, 3/4]` |


