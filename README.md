# Sudoku Solver  

A console-based Sudoku solver that allows users to input and solve Sudoku puzzles.  
The algorithm is based on techniques I learned at university and online, but the implementation is entirely my own.  

## Features  
- Interactive console-based interface  
- Allows manual input of Sudoku puzzles  
- Provides an option to correct mistakes before solving  
- Outputs a valid solution after computation  

## Usage Instructions  

1. Run the program from the terminal.  
2. The program will prompt you to enter numbers for each cell, one by one.  
   - If a cell is empty, simply press **Enter** to move to the next one.  
3. Once all values are entered, the program will display the Sudoku grid.  
   - If you made a mistake, you will have the option to edit any cell.  
4. When the grid is correct, press **Enter** to start solving.  
5. After a short processing time, the program will display the solved Sudoku puzzle.  

## Requirements  
- Python 3.x  
- Numpy

## Installation  

Clone the repository:  
```sh
git clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver

