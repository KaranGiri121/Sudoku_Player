import os,time
from selenium import webdriver


PATH=r"C:\chromedriver"
class Sudoku:
    def __init__(self):
        self.driver=webdriver.Chrome(PATH)

    #This Function WriteDown Sudoku Cell Value In sudoku.txt File
    #Because It Will Used By C++ Script 
    def __WriteDown(self,elements):  
        with open("sudoku.txt","w") as File:
            count=0
            for i in elements:
                File.write(i)
                count+=1
                if(count==9):           #To Decorate Sudoku.txt File 
                    File.write("\n")
                    count=0
    
    def __SolvedThis(self): 
        
        #This Function Used C++ Compiler To Solve Sudoku
        #Because It Fast 
        #I Will Update This Code With Python Solver 😁
        os.system("g++ SudokuSolver.cpp -o SudokuSolver && SudokuSolver") 
                

    
    def NYTime(self):
        __url="https://www.nytimes.com/puzzles/sudoku/easy" #Url Of NYTime Sudoku Puzzle With Easy Level
        self.driver.get(__url)                              #Opening NYTime Url In Broswer

        #Wait For 10Sec Till Browser Complety Loaded

        self.driver.implicitly_wait(10)
        element=self.driver.find_elements_by_class_name("su-cell")              #Fetching All Value Of Sudoku 
        button=self.driver.find_elements_by_class_name("su-keyboard__number")   #Fetching Inbuilt Number Pad For Input

                                                            #Update..........

        #   IN NYTime NumberPad Has Two Type Normal And Candidate
        #   Candidate Is Used When You Are Not Confirmed 
        #   Normal NumberPad Is Used When Your Sure!
        try:    #Checking NormalMode Is On/Off 
            self.driver.find_element_by_class_name("normalMode") #Do Noting If NormalMode Is On OtherWise Raise Exception Handle Below
        except Exception:
            self.driver.find_element_by_class_name("normal").click() #Finding Normal Button And Activate NormalPad Mode

        #Filtering element list of tag to Fetch Usefull Infomation And Append In elements List
        elements=[]
        for cell in element:
            info=cell.get_attribute("aria-label")  #Cell Value Saved In Aria-Label Attribute
            if info=="empty":                   # In NYTime Sudoku Empty Cell Represent By empty String 
                elements.append('-1 ')           # C++ Read Empty Space As -1
            else:
                elements.append(info+" ")           #WriteDown Non-Empty Value

        self.__WriteDown(elements)              #Write Down sudoku.txt File

        self.__SolvedThis()                     #Solving Sudoku

        #Solution List Contain Solved Sudoku Replacing -1 Value With Appropriate Value
        Solution=[]
        with open("solved.txt","r") as File:
            for value in File:
                temp=value.split(" ")           #Reading Row And Split By Space ['7','9','1','2','6','8','3','4','5','\n'] 
                for i in range(0,9):            #Alway Escape Element Is End Of List So Range(0,9)
                    Solution.append(int(temp[i]))

        #If Empty Place Is Already Is Select Then Raise Exception So Safe Play

        element[80].click()                       #For Safe Play Make Click In Last Cell Of The Sudoku
        for cell in element:
            cell_info=cell.get_attribute("aria-label")       #Status Non_Empty Or Empty 
            if cell_info=="empty":                           #Only Filling Empty Is Good Idea
                pos=int(cell.get_attribute("data-cell"))     #This Attribute As Information Of Position In Sudoku As Row Wise
                cell.click()                                 #Selecting That Empty Cell
                button[Solution[pos]-1].click()              #Button[0,8] So -1 And Solution Give Button Number And Click
        
        time.sleep(1000)
        self.driver.close()


a=Sudoku()
a.NYTime()
                



        











