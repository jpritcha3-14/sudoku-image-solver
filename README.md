# Solve Sudoku from an Image
This project aims to take any picture of a sudoku puzzle, extract its contents using image processing techniques, solve the puzzle, and then overlay the solution on the original image.

## Software Used
anaconda / conda - Used to set up isolated environments with specific packages. Can be [downloaded here](https://www.anaconda.com/distribution/). 
scikit Learn - Included in the base conda environment.
openCV - Can be installed from within the conda environment using `pip install opencv-python`

## Goals and Progress
- **Parse individual squares from a Sudoku puzzle, accounting for skew in camera angle and warping in the paper.**
	- Complete!  User selects the 4 corners of the puzzle with mouse clicks. These points are then used to transform the puzzle to a square of a standard size.  Matching against a template square is used to find the location of all squares while accounting for slight curves in the paper.

- **Determine the numbers contained in parsed squares.**
	- ~~Currently using template matching against a single set of digit images to classify numbers.  While it is a relatively effective strategy for this constrained of a problem, it has issues with similarly shaped 6s, 9s and 8s.~~
    - Classifier (random forest) has been trained on ~900 numbers parsed from images gathered from the internet.  Cross validated accuracy for digit recogintion is around 98%.  Will continue to gather images to improve classifier.

- **Solve the Sudoku puzzle**
	- Complete! The solvePuzzle.py script solves a Sudoku puzzle represented as numpy ndarray.

- **Overlay the solution to the puzzle on the original image accounting for the original camera skew**
	- To be implemented.

## Next Steps
- ~~Create a script to ingest Sudoku images and create examples of each number using current functions for corner selection and square parsing.~~
- ~~Find, ingest, and classify digit images to train a learning model.~~
- ~~Train a supervised learning model to correctly identify numbers.~~
- ~~Use the trained model to classify numbers from new puzzles.~~
- Overlay the results of solving the sudoku puzzle on the original image.
- Clean up and comment code, run a linter. 
- Continue to gather and ingest sudoku images to improve the classifier.
