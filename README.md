# CISC-121-Project-Deliverables
## Chosen Algorithm & Why: 
I have chosen Jump Search as my algorithm to visualize since I believe that it is a unique, yet not too complex algorithm. The jumping pattern ans final linear scan are pretty easy to represent visually, making the two phases of the algorithm simple to understand. This visualization will also help explain time complexity in a better way than just "the big O," by showing how Jump Search reduces the number of comparisons compared to linear search.

## Computational Thinking:
### Decomposition 
The algorithm is Divided into 3 main steps: determining the jump size based off of the array length, then jumping forward through the list in intervals, identifying the block where the target might exist, and then performing a linear search within that block to find the exact value.
### Pattern Recognition
The algorithm follows a repeating pattern of jumping forward by a fixed amount and then compares the values with the target. Once the jump passes the target value, it switches to checking each element one by one within the last block until the value is found or the block ends.
### Abstraction
The visualization will show only the important actions: the current position, the jump points, and the active search range. Compared values are highlighted, and the block being searched will be clearly marked. Calculations in the code such as the math inbetween indexes and the square root calculations are not going to be shown, I want to keep the display simple and more focused on the algorithms behavior, not the internal processes of the algorithm.
### Algorithm Design
The user will input a list of integers and a target value through the GUI. Then, it will process the input by running the jump search algorithm and visually displaying each jump and comparison step. The output will then show where the value was found and it's position, along with some visual feedback that highlights the search process.

![](Flowchart-JumpSearch.jpeg)

## BEFORE Adding Interactivity - Where AI Has Been Used:
### Debugging
#### Before (Buggy Version)
```python
import math
import random

numbers = [4,8,14,19,20,22,24,27,30,55]
target = list[random.randint(0,9)]  
# Bug: "list" is the built-in type, not my array
print("Target value is: ", target)

def jump(list,target):
    # Bug: parameter name "list" overwrites Python's built in list type
    # I should call it something like "lst" or "arr"
    n = len(list)
    step = math.sqrt(n)
    # Bug: step should be an integer (use int(math.sqrt(n)))
    previous = 0
    # jump phase
    while previous < n and list[math.floor(step)] < target:
        # Bug: Index can go out of range.
        # Bug: math.floor(step) is unnecessary if step is already an int
        previous = int(step)
        step += math.sqrt(n)
        # Bug: step must remain an integer.
        if previous >= n:
            return -1
    # linear search phase
    while previous < n and list[math.floor(step)] < target:
        # Bug: Should check list[previous], not list[math.floor(step)].
        # Linear search must move one-by-one from previous
        previous += 1
    # check if found
    if list[previous] == target:
        # Bug: No bounds check (previous may be out of range)
    return -1

pos = jump(numbers, target)
if numbers != -1:
    # Bug: This checks the entire list instead of the result
    print("Found at position: ", pos)
else:
    print("Number not found at any position.")

```
At this point I had finished my code, but there were bugs that I couldn't find. So, I used AI (ChatGPT) with the prompt: "Identify the bugs in this code and walk me through how to fix them, but don't explicity give away how to fix it, I still need to undetstand what's going on: (code)"

#### After (Fixed, Non-Buggy Version)
```python
import math
import random

numbers = [
    random.randint(1,10), 
    random.randint(11,20), 
    random.randint(21,30),
    random.randint(31,40), 
    random.randint(41,50), 
    random.randint(51,60),
    random.randint(61,70), 
    random.randint(71,80), 
    random.randint(81,90),
    random.randint(91,100)
]
# FIX: Numbers are generated in increasing ranges to help ensure order
numbers.sort()
# ADDED: Sorting to guarantee jump search always works
print("Given list is:", numbers)
target = int(input("Choose a number from the list to search for: "))
# FIX: User now selects a real value instead of random index guessing
while target not in numbers:
    # ADDED: Input validation to guarantee the number exists in the list
    target = int(input("Choose a number FROM THE LIST: "))
print("Target value is:", target)
def jump(lst, target):
    # FIX: Renamed parameter from "list" to "lst" to avoid overriding built-in name.
    n = len(lst)
    step = int(math.sqrt(n))
    # FIX: step is now an integer
    previous = 0
    # jump phase
    while previous < n and lst[min(step, n) - 1] < target:
        # FIX: Corrected index check formatting
        # FIX: Prevents index out of bounds
        # FIX: Now compares correct jump location
        previous = step
        step += int(math.sqrt(n))
        # FIX: step increases by integer jump size
        if previous >= n:
            return -1
    # linear search
    while previous < n and lst[previous] < target:
        # FIX: Proper linear scan forwards
        previous += 1
    # found
    if previous < n and lst[previous] == target:
        # FIX: Bound check added before comparison
        return previous
    return -1

pos = jump(numbers, target)
if pos != -1:
    # FIX: Correct check now uses the result index, not the list
    print("Found at position:", pos + 1)
else:
    print("Number not found.")

```
