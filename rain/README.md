# Rain Project

This project implements an algorithm to calculate how much rainwater can be retained between walls.

## Algorithm Explanation

The solution uses a two-pointer approach:
1. Calculate the maximum wall height to the left of each position
2. Calculate the maximum wall height to the right of each position
3. For each position, water level = min(left_max, right_max) - wall_height

## Files

- `0-rain.py`: Main function implementation
- `0_main.py`: Test file

## Usage


bash
./0_main.py
```

Press `Esc`, type `:wq`, and press `Enter`.

## Step 7: Check PEP 8 Style

Install pep8 if you haven't:


bash
sudo apt-get update
sudo apt-get install python3-pep8

Check your code:


bash
pep8 0-rain.py

If there are no errors, you're good!

## Step 8: Initialize Git and Push to Repository


bash
cd ~/alu-interview
git init
git add rain/
git commit -m "Add Rain project solution"
git remote add origin https://github.com/YOUR_USERNAME/alu-interview.git
git push -u origin main

## How the Algorithm Works

**For walls = [0, 1, 0, 2, 0, 3, 0, 4]:**

- At index 2 (wall=0): water = min(1,4) - 0 = 1
- At index 4 (wall=0): water = min(2,4) - 0 = 2
- At index 6 (wall=0): water = min(3,4) - 0 = 3
- **Total = 6 units**

The key insight is that water at any position is determined by the minimum of the tallest walls on both sides minus the current wall height.

## Testing Additional Cases

You can test edge cases:


bash
python3 -c "from rain import rain; print(rain([]))"  # Should print 0
python3 -c "from rain import rain; print(rain([1, 2, 3]))"  # Should print 0
python3 -c "from rain import rain; print(rain([3, 0, 2, 0, 4]))"  # Should print 7
