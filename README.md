# fubukiPuzzleSolverDash
This app helps user solve Fubuki Puzzles. 

## Instructions: 
Place the number 1 to 9 in the 3 by 3 grid so that each horizontal and vertical line adds up to the given sum. You can only use each number once. R and C values are already given. 

As seen in the picture: R and C values along with a position and its value are already given. User will be prompted to input these fields and the program will come up with solutions.

## How this works: 
I used Dash to create an appealing, user-friendly interface online. When all the input are recorded, the program places these values into a Numpy Array called `myPrefilledVals`at the same time it creates another list `myList` generating numbers from 1 to 9. It then deletes the given position and creates another list `newList`
The program goes onto create a list `permList` of all permutations of `newList` (now with 8 values because one value has been deleted) using the `permutations()` function from `itertools`. 
It then loops through all the permutations and in here it will re-add the pre-filled position and its value back into the list to find a match.
During this process, the program calculates and puts all the sums into a solution array `solution`, which then will be checked against the array of pre-filled values. 
If there's a match, the function will add the permutation to `myResults` array. 
If there are more than 1 solutions, the program returns a `DataFrame` of the solutions and will output as a HTML table.
If there is no solution, the program will display the message `There is no solution`

## Usage: 
* Python Dash
* NumPy arrays
* `permutations()` function from `itertools`
* HTML table
* `Pandas` `DataFrame`

## Improvements: 
This algorithm is brute-force, thus, run-time is slow. My goal is to come up with a more efficient algorithm
