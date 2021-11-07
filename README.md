# Sudoku_Player
 Using WebAutomation Sudoku Bot Solve Given Sudoku Of Given WebSite Like 
 **1. NYTime 
 2. WebSudoku 
 3. Livesudoku
 And Many More Will Be Added**
 ### Requirement
 **1)WebDriver**

 To Work With First You Have To Download WebDriver For Chrome Of Your Chrome Version And Copy To Driver Folder
[Find WebDrivers](https://chromedriver.storage.googleapis.com/index.html)

**2)Selenium**

To Install Selenium  `pip install selenium` or `pip3 install selenium`

---
##Information

I Have Written Sudoku Solving Part In C++ **(Comment Out The C++ Part in main.py def __solveThis)**
But Because Of All Major Code Include In Python
So sudoku.py Is Used To Solve Sudoku And Write All Solution In solved.txt

And Used By main.py

___

##Working

As User Input One Of Listed Website
It Will Open In WebDriver And That Url Get Loaded

And main.py Find All Cell Of Sudoku And Write In sudoku.txt
The Value Of Cell And Replace Empty Place With -1

And Using `os.system(python sudoku.py)` or Before `os.system("g++ SudokuSolver.cpp -o SudokuSolver && SudokuSolver")`

Above Code Solve sudoku.txt And Save Solution In solved.txt File
Using This File Web Bot Enter Value In Remaining Cell Of UnSolved Sudoku