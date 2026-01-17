#!/usr/bin/python3
"""
Additional test cases for minOperations
"""

minOperations = __import__('0-minoperations').minOperations

# Test cases
test_cases = [
    (1, 0),      # n = 1, already have 1 H
    (2, 2),      # n = 2, Copy + Paste
    (3, 3),      # n = 3, Copy + Paste + Paste
    (4, 4),      # n = 4 = 2*2, operations: 2+2
    (5, 5),      # n = 5 (prime), Copy + Paste * 4
    (6, 5),      # n = 6 = 2*3, operations: 2+3
    (9, 6),      # n = 9 = 3*3, operations: 3+3
    (12, 7),     # n = 12 = 2*2*3, operations: 2+2+3
    (15, 8),     # n = 15 = 3*5, operations: 3+5
    (21, 10),    # n = 21 = 3*7, operations: 3+7
    (100, 14),   # n = 100 = 2*2*5*5, operations: 2+2+5+5
]

print("Running test cases...")
all_passed = True

for n, expected in test_cases:
    result = minOperations(n)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    print(f"{status}: n={n}, expected={expected}, got={result}")
    if result != expected:
        all_passed = False

print()
if all_passed:
    print("🎉 All tests passed!")
else:
    print("❌ Some tests failed!")
