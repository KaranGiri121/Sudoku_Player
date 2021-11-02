import os,time
from selenium import webdriver


PATH=r"C:\chromedriver"
driver=webdriver.Chrome(PATH)
driver.get("https://www.nytimes.com/puzzles/sudoku/hard")
# time.sleep(10)
element=driver.find_elements_by_class_name("su-cell")
try:
    driver.find_element_by_class_name("normalMode")
except Exception:
    driver.find_element_by_class_name("normal").click()
with open('sudoku.txt',"w") as f:
    start=0
    till=9
    while(till<=81):
        for i in element[start:till]:
            value=i.get_attribute("aria-label")
            if(value!='empty'):
                f.write(value+" ")
            else:
                f.write('-1 ')
        f.write('\n')
        start,till=till,till+9

os.system("g++ SudokuSolver.cpp -o SudokuSolver && SudokuSolver")
value=[]
with open("solved.txt","r") as f:
    for i in f:
        x=i.split(" ")
        for j in range(0,9):
            value.append(int(x[j]))

def putting():
    button=driver.find_elements_by_class_name("su-keyboard__number")
    for i in element:
        info=i.get_attribute("aria-label")
        if(info=="empty"):
            pos=int(i.get_attribute("data-cell"))
            i.click()
            button[value[pos]-1].click()

putting()




time.sleep(1000)
driver.close()

