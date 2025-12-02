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
