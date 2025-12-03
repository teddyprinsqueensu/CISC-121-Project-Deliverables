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

## Where AI Has Been Used:
### Debugging
#### Before (Buggy Version)
```python
import math
import random

numbers = [4,8,14,19,20,22,24,27,30,55]

target = list[random.randint(0,9)] # Bug: "list" should actually be "numbers[...]"
print("Target value is: ", target)

def jump(list,target):
    n = len(list)
    step = math.sqrt(n)
    previous = 0

    # jump phase
    while previous < n and list[math.floor(step)] < target: # Bug: "math.floor(step)" should actually be "min(step, n) -1," and math.floor doesn't need to be used
        previous = int(step)
        step += math.sqrt(n) # Bug: "math.sqrt(n)" needs an "int()" around it
        if previous >= n:
            return -1

    # linear search phase
    while previous < n and list[math.floor(step)] < target:
        previous += 1

    # check if found
    if list[previous] == target: # Bug: this whole if statement sucks, instead it should be "previous < n and list[previous] < target"
        return previous

    return -1

pos = jump(numbers, target)

if numbers != -1: # Bug: "numbers" should be "pos"
    print("Found at position: ", pos)
else:
    print("Number not found at any position.")
```
At this point I had finished my code, but there were bugs that I couldn't find. So, I used AI (ChatGPT) with the prompt: "Identify the bugs in this code and walk me through how to fix them, but don't explicity give away how to fix it, I still need to learn: (code)"

#### After (Fixed, Non-Buggy Version)
```python
import math
import random

numbers = [4,8,14,19,20,22,24,27,30,55]

target = numbers[random.randint(0,9)] # Fixed
print("Target value is: ", target)

def jump(list,target):
    n = len(list)
    step = int(math.sqrt(n))
    previous = 0

    # jump phase
    while previous < n and list[min(step,n)] < target: # Fixed
        previous = step
        step += int(math.sqrt(n)) # Fixed
        if previous >= n:
            return -1

    # linear search phase
    while previous < n and numbers[previous] < target:
        previous += 1

    # check if found
    if previous < n and numbers[previous] == target: # Fixed
        return previous

    return -1

pos = jump(numbers, target)

if pos != -1: # Fixed
    print("Found at position: ", pos + 1)
else:
    print("Number not found at any position.")
```
