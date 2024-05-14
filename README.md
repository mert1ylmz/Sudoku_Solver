# Sudoku Solver
This is a sudoku solving program written in Python language.
In this program there is a 9x9 sudoku board given by the coder.
Program uses this board for upcoming parts.
First of all this board goes thru a subgrid function. This function creates a nice looking sudoku table. Not necessary but it looks nice.
But we must check the board and decide whether it is suitable. So there is a validation function for that. 
This function checks if the numbers in a row or a column is repeated. 
Of course this function will check for the empty spaces when time comes for the solving sudoku.
But before that we must determine the empty cells that visualized like "0".
Then the program solves the sudoku one by one with solveSudoku func and prints it.

*Board can be changed but program will not help the user for false boards. Only prints "NO SOLUTION FOR THIS SUDOKU TABLE".

