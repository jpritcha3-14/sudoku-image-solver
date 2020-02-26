# Solve Sudoku from an Image
This project aims to take any extract the contents of any Sudoku puzzle using image processing techniques, solve the puzzle, and then overlay the solution on the original image.

## Software Used
This project uses OpenCV with bindings for Python 3.  
It can be installed on Ubuntu and it's derivatives [by following the instructions here](https://docs.opencv.org/3.4/d2/de6/tutorial_py_setup_in_ubuntu.html).  NOTE: if you have both Python 2 and Python 3 in your environment, make sure to include the following cmake flag: `-DPYTHON_DEFAULT_EXECUTABLE=$(which python3)`

## Goals and Progress
- **Parse individual squares from a Sudoku puzzle, accounting for skew in camera angle and warping in the paper.**
	- Complete!  User selects the 4 corners of the puzzle with mouse clicks. These points are then used to transform the puzzle to a square of a standard size.  Matching against a template square is used to find the location of all squares while accounting for slight curves in the paper.
- **Determine the numbers contained in parsed squares.**
	- Currently using template matching against a single set of digit images to classify numbers.  While it is a relatively effective strategy for this constrained of a problem, it has issues with similarly shaped 6s, 9s and 8s.
- **Solve the Sudoku puzzle**
	- To be implemented
- **Overlay the solution to the puzzle on the original image accounting for the original camera skew**
	- To be implemented

## Next Steps
- Create a script to ingest Sudoku images and create examples of each number using current functions for corner selection and square parsing.
- Train a supervised learning model to correctly identify numbers.
- Use the trained model to classify numbers from new puzzles.
