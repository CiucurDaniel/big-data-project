# Apriori

Simple Apriori implementation in python. This is the "basic" implementation using no `parallelization`.
Based on the following papper: [Fast algorithms for mining association rules](https://www.it.uu.se/edu/course/homepage/infoutv/ht08/vldb94_rj.pdf).

## Run

```bash
pip list # to ensure ou have libs, othwerwise install libs first
python apriori.py
```

## Example output

```
Frequent items sets on level:  1
[({1}, 0.25), ({2}, 0.65), ({3}, 0.35), ({4}, 0.3), ({5}, 0.2), ({6}, 0.1), ({7}, 0.25), ({8}, 0.35), ({9}, 0.4), ({10}, 0.15), ({11}, 0.3)]

Frequent items sets on level:  2
[({1, 2}, 0.2), ({1, 3}, 0.1), ({1, 4}, 0.1), ({1, 6}, 0.05), ({1, 7}, 0.05), ({8, 1}, 0.05), ({1, 9}, 0.05), ({2, 3}, 0.2), ({2, 4}, 0.05), ({2, 5}, 0.15), ({2, 6}, 
0.1), ({2, 7}, 0.15), ({8, 2}, 0.2), ({9, 2}, 0.15), ({2, 10}, 0.05), ({2, 11}, 0.2), ({3, 4}, 0.15), ({3, 7}, 0.1), ({8, 3}, 0.1), ({9, 3}, 0.1), ({10, 3}, 0.1), ({11, 3}, 0.05), ({4, 7}, 0.05), ({8, 4}, 0.1), ({9, 4}, 0.2), ({10, 4}, 0.1), ({11, 4}, 0.05), ({8, 5}, 0.1), ({9, 5}, 0.05), ({11, 5}, 0.1), ({6, 7}, 0.1), ({8, 6}, 0.05), ({8, 7}, 0.2), ({8, 9}, 0.05), ({9, 10}, 0.15), ({9, 11}, 0.2)]

Frequent items sets on level:  3
[({1, 2, 3}, 0.1), ({1, 2, 4}, 0.05), ({1, 2, 6}, 0.05), ({1, 2, 7}, 0.05), ({1, 3, 4}, 0.05), ({8, 1, 4}, 0.05), ({1, 4, 9}, 0.05), ({1, 6, 7}, 0.05), ({8, 1, 9}, 0.05), ({2, 3, 4}, 0.05), ({2, 3, 7}, 0.05), ({8, 2, 3}, 0.05), ({11, 2, 3}, 0.05), ({8, 2, 5}, 0.1), ({2, 11, 5}, 0.05), ({2, 6, 7}, 0.1), ({8, 2, 6}, 0.05), ({8, 2, 7}, 0.1), ({9, 2, 10}, 0.05), ({9, 2, 11}, 0.1), ({9, 3, 4}, 0.1), ({10, 3, 4}, 0.1), ({8, 3, 7}, 0.1), ({9, 10, 3}, 0.1), ({8, 4, 7}, 0.05), ({8, 9, 4}, 0.05), ({9, 10, 4}, 0.1), ({9, 11, 4}, 0.05), ({9, 11, 5}, 0.05), ({8, 6, 7}, 0.05)]

Frequent items sets on level:  4
[({1, 2, 3, 4}, 0.05), ({1, 2, 6, 7}, 0.05), ({1, 4, 8, 9}, 0.05), ({2, 3, 7, 8}, 0.05), ({2, 6, 7, 8}, 0.05), ({3, 4, 9, 10}, 0.1)]

Number of rules:  86

{'milk'} -> {'bread'} <confidence: 0.8>
{'bournvita'} -> {'bread'} <confidence: 0.7499999999999999>
{'jam'} -> {'bread'} <confidence: 1.0>
{'maggi'} -> {'bread'} <confidence: 0.6>
{'sugar'} -> {'bread'} <confidence: 0.6666666666666667>
{'apple'} -> {'biscuit'} <confidence: 0.6666666666666667>
{'cornflakes'} -> {'coffee'} <confidence: 0.6666666666666667>
{'apple'} -> {'cornflakes'} <confidence: 0.6666666666666667>
{'jam'} -> {'maggi'} <confidence: 1.0>
{'maggi'} -> {'tea'} <confidence: 0.8>
{'apple'} -> {'coffee'} <confidence: 1.0>
{'sugar'} -> {'coffee'} <confidence: 0.6666666666666667>
{'milk', 'biscuit'} -> {'bread'} <confidence: 1.0>
{'cornflakes', 'bread'} -> {'milk'} <confidence: 1.0>
{'milk', 'jam'} -> {'bread'} <confidence: 1.0>
{'milk', 'maggi'} -> {'bread'} <confidence: 1.0>
{'tea', 'milk'} -> {'cornflakes'} <confidence: 1.0>
{'milk', 'coffee'} -> {'cornflakes'} <confidence: 1.0>
{'milk', 'jam'} -> {'maggi'} <confidence: 1.0>
{'milk', 'maggi'} -> {'jam'} <confidence: 1.0>
{'tea', 'milk'} -> {'coffee'} <confidence: 1.0>
{'tea', 'coffee'} -> {'milk'} <confidence: 1.0>
{'milk', 'coffee'} -> {'tea'} <confidence: 1.0>
{'cornflakes', 'bread'} -> {'biscuit'} <confidence: 1.0>
{'sugar', 'biscuit'} -> {'bread'} <confidence: 1.0>
{'tea', 'bournvita'} -> {'bread'} <confidence: 1.0>
{'bournvita', 'bread'} -> {'tea'} <confidence: 0.6666666666666667>
{'jam'} -> {'maggi', 'bread'} <confidence: 1.0>
{'jam', 'maggi'} -> {'bread'} <confidence: 1.0>
{'jam', 'bread'} -> {'maggi'} <confidence: 1.0>
{'maggi', 'bread'} -> {'jam'} <confidence: 0.6666666666666667>
{'tea', 'jam'} -> {'bread'} <confidence: 1.0>
{'maggi', 'bread'} -> {'tea'} <confidence: 0.6666666666666667>
{'apple', 'bread'} -> {'coffee'} <confidence: 1.0>
{'coffee', 'bread'} -> {'sugar'} <confidence: 0.6666666666666667>
{'cornflakes', 'biscuit'} -> {'coffee'} <confidence: 0.6666666666666667>
{'coffee', 'biscuit'} -> {'cornflakes'} <confidence: 1.0>
{'apple'} -> {'cornflakes', 'biscuit'} <confidence: 0.6666666666666667>
{'cornflakes', 'biscuit'} -> {'apple'} <confidence: 0.6666666666666667>
{'cornflakes', 'apple'} -> {'biscuit'} <confidence: 1.0>
{'apple', 'biscuit'} -> {'cornflakes'} <confidence: 1.0>
{'tea', 'biscuit'} -> {'maggi'} <confidence: 1.0>
{'maggi', 'biscuit'} -> {'tea'} <confidence: 1.0>
{'apple'} -> {'coffee', 'biscuit'} <confidence: 0.6666666666666667>
{'coffee', 'biscuit'} -> {'apple'} <confidence: 1.0>
{'apple', 'biscuit'} -> {'coffee'} <confidence: 1.0>
{'coffee', 'apple'} -> {'biscuit'} <confidence: 0.6666666666666667>
{'cornflakes', 'maggi'} -> {'tea'} <confidence: 1.0>
{'tea', 'coffee'} -> {'cornflakes'} <confidence: 1.0>
{'apple'} -> {'cornflakes', 'coffee'} <confidence: 0.6666666666666667>
{'cornflakes', 'apple'} -> {'coffee'} <confidence: 1.0>
{'coffee', 'apple'} -> {'cornflakes'} <confidence: 0.6666666666666667>
{'cornflakes', 'sugar'} -> {'coffee'} <confidence: 1.0>
{'coffee', 'bournvita'} -> {'sugar'} <confidence: 1.0>
{'tea', 'jam'} -> {'maggi'} <confidence: 1.0>
{'cornflakes', 'bread'} -> {'milk', 'biscuit'} <confidence: 1.0>
{'cornflakes', 'milk', 'biscuit'} -> {'bread'} <confidence: 1.0>
{'cornflakes', 'milk', 'bread'} -> {'biscuit'} <confidence: 1.0>
{'cornflakes', 'biscuit', 'bread'} -> {'milk'} <confidence: 1.0>
{'milk', 'jam'} -> {'maggi', 'bread'} <confidence: 1.0>
{'milk', 'maggi'} -> {'jam', 'bread'} <confidence: 1.0>
{'milk', 'jam', 'maggi'} -> {'bread'} <confidence: 1.0>
{'milk', 'jam', 'bread'} -> {'maggi'} <confidence: 1.0>
{'milk', 'maggi', 'bread'} -> {'jam'} <confidence: 1.0>
{'tea', 'milk'} -> {'cornflakes', 'coffee'} <confidence: 1.0>
{'milk', 'coffee'} -> {'tea', 'cornflakes'} <confidence: 1.0>
{'tea', 'coffee'} -> {'cornflakes', 'milk'} <confidence: 1.0>
{'cornflakes', 'milk', 'tea'} -> {'coffee'} <confidence: 1.0>
{'cornflakes', 'milk', 'coffee'} -> {'tea'} <confidence: 1.0>
{'cornflakes', 'tea', 'coffee'} -> {'milk'} <confidence: 1.0>
{'tea', 'milk', 'coffee'} -> {'cornflakes'} <confidence: 1.0>
{'tea', 'biscuit', 'bread'} -> {'maggi'} <confidence: 1.0>
{'maggi', 'biscuit', 'bread'} -> {'tea'} <confidence: 1.0>
{'tea', 'jam'} -> {'maggi', 'bread'} <confidence: 1.0>
{'tea', 'jam', 'maggi'} -> {'bread'} <confidence: 1.0>
{'tea', 'jam', 'bread'} -> {'maggi'} <confidence: 1.0>
{'apple'} -> {'cornflakes', 'coffee', 'biscuit'} <confidence: 0.6666666666666667>
{'cornflakes', 'apple'} -> {'coffee', 'biscuit'} <confidence: 1.0>
{'cornflakes', 'biscuit'} -> {'coffee', 'apple'} <confidence: 0.6666666666666667>
{'coffee', 'apple'} -> {'cornflakes', 'biscuit'} <confidence: 0.6666666666666667>
{'biscuit', 'apple'} -> {'cornflakes', 'coffee'} <confidence: 1.0>
{'coffee', 'biscuit'} -> {'cornflakes', 'apple'} <confidence: 1.0>
{'cornflakes', 'coffee', 'apple'} -> {'biscuit'} <confidence: 1.0>
{'cornflakes', 'biscuit', 'apple'} -> {'coffee'} <confidence: 1.0>
{'cornflakes', 'coffee', 'biscuit'} -> {'apple'} <confidence: 1.0>
{'biscuit', 'coffee', 'apple'} -> {'cornflakes'} <confidence: 1.0>
```