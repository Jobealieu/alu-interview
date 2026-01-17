# Minimum Operations

## Description
This project contains a solution to calculate the minimum number of operations needed to result in exactly `n` `H` characters in a file, using only two operations: **Copy All** and **Paste**.

## Problem
Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

### Operations Available:
- **Copy All**: Copy all characters currently in the file
- **Paste**: Paste the copied characters

## Algorithm
The solution uses prime factorization:
- The minimum number of operations equals the sum of all prime factors of `n`
- If `n` is impossible to achieve (n ≤ 1), return 0

## Example
```
n = 9
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Operations: 6 (3 + 3, since 9 = 3 × 3)
```

## Usage
```python
minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# Output: Min # of operations to reach 4 char: 4

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# Output: Min # of operations to reach 12 char: 7
```

## Requirements
- Python 3.4.3
- Ubuntu 14.04 LTS
- PEP 8 style (version 1.7.x)

## Author
Alieu Jobe
