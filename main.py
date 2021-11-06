import os,time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


PATH=r"C:\chromedriver"
class Sudoku:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--ignore-certificate-errors-spki-list')
        self.driver = webdriver.Chrome(PATH,options=options)

    # This Function WriteDown Sudoku Cell Value In sudoku.txt File
    # Because It Will Used By C++ Script 
    def __WriteDown(self,elements):  
        with open("sudoku.txt","w") as File:
            count=0
            for i in elements:
                File.write(i)
                count+=1
                if(count==9):           # To Decorate Sudoku.txt File 
                    File.write("\n")
                    count=0
    
    def __SolvedThis(self): 
        
        # This Function Used C++ Compiler To Solve Sudoku
        # Because It Fast 
        # I Will Update This Code With Python Solver 😁
        os.system("g++ SudokuSolver.cpp -o SudokuSolver && SudokuSolver") 
                

    
    def NYTime(self):
        __url="https://www.nytimes.com/puzzles/sudoku/easy" # Url Of NYTime Sudoku Puzzle With Easy Level
        self.driver.get(__url)                              # Opening NYTime Url In Broswer

        # Wait For 10Sec Till Browser Complety Loaded

        self.driver.implicitly_wait(10)
        element=self.driver.find_elements_by_class_name("su-cell")              # Fetching All Value Of Sudoku 
        button=self.driver.find_elements_by_class_name("su-keyboard__number")   # Fetching Inbuilt Number Pad For Input

                                                            # Update..........

        #    IN NYTime NumberPad Has Two Type Normal And Candidate
        #    Candidate Is Used When You Are Not Confirmed 
        #    Normal NumberPad Is Used When Your Sure!
        try:    # Checking NormalMode Is On/Off 
            self.driver.find_element_by_class_name("normalMode") # Do Noting If NormalMode Is On OtherWise Raise Exception Handle Below
        except Exception:
            self.driver.find_element_by_class_name("normal").click() # Finding Normal Button And Activate NormalPad Mode

        # Filtering element list of tag to Fetch Usefull Infomation And Append In elements List
        elements=[]
        for cell in element:
            info=cell.get_attribute("aria-label")  # Cell Value Saved In Aria-Label Attribute
            if info=="empty":                   #  In NYTime Sudoku Empty Cell Represent By empty String 
                elements.append('-1 ')           #  C++ Read Empty Space As -1
            else:
                elements.append(info+" ")           # WriteDown Non-Empty Value

        self.__WriteDown(elements)              # Write Down sudoku.txt File

        self.__SolvedThis()                     # Solving Sudoku

        # Solution List Contain Solved Sudoku Replacing -1 Value With Appropriate Value
        Solution=[]
        with open("solved.txt","r") as File:
            for value in File:
                temp=value.split(" ")           # Reading Row And Split By Space ['7','9','1','2','6','8','3','4','5','\n'] 
                for i in range(0,9):            # Alway Escape Element Is End Of List So Range(0,9)
                    Solution.append(int(temp[i]))

        # If Empty Place Is Already Is Select Then Raise Exception So Safe Play

        element[80].click()                       # For Safe Play Make Click In Last Cell Of The Sudoku
        for cell in element:
            cell_info=cell.get_attribute("aria-label")       # Status Non_Empty Or Empty 
            if cell_info=="empty":                           # Only Filling Empty Is Good Idea
                pos=int(cell.get_attribute("data-cell"))     # This Attribute As Information Of Position In Sudoku As Row Wise
                cell.click()                                 # Selecting That Empty Cell
                button[Solution[pos]-1].click()              # Button[0,8] So -1 And Solution Give Button Number And Click
        
        time.sleep(1000)
        self.driver.close()

    def LiveSudoku(self):
        __url="https://www.livesudoku.com/en/sudoku/easy/"      # Url Of LiveSudoku Game
        self.driver.get(__url)                                  # Loading Window For Url

        element=self.driver.find_elements_by_class_name("cellnormal")   # All The Cell In LiveSudoku Is Written In cellnormal Class
        elements=[]                                             # Used To Store All Cell Value And InPlace Of Empty -1 Will Store
        for cell in element:
            try:                    # Checking If Cell Is Empty Or Not
                tag=cell.find_element_by_tag_name("span")       # If Cell Have Value Then Span Is Present
                data=tag.text                                   # Extract Span Text Or Cell Value

            except Exception:       # If Span Is Not Find Then Cell Is Empty
                data="-1"           # So The Data Is -1                        
            
            elements.append(data+" ")       # Append In List The Data

        self.__WriteDown(elements)          # Write Down The Value In sudoku.txt

        self.__SolvedThis()                 # Solved sudoku.txt And Create solved.txt

        Solution=[]                         # Solution List Is Used To Store solved.txt value
        with open("solved.txt","r") as File:
            for value in File:
                temp=value.split(" ")
                for i in range(0,9):
                    Solution.append(int(temp[i]))

        for cell in range(0,81):            # All Cell Value Is Inserted
            action=ActionChains(self.driver)        # ActionChains Is Used To Send Key Because Cell Is Not Input Type.
            action.click(on_element=element[cell])  # Selection Cell
            action.send_keys(Solution[cell])        # Sending Solution Of Corresponding Selected Cell
            action.perform()                        # ActionChains To Perform 


        time.sleep(1000)
        self.driver.close()

            





