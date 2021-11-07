from typing import List, Sized


sudoku=[]

with open("sudoku.txt","r") as File:
    for value in File:
        temp=[]
        value=value.split(" ")
        for i in range(0,9):
            temp.append(int(value[i]))
        
        sudoku.append(temp)



def issafe(i,j,value):
    for y in range(0,9):
        if sudoku[i][y]==value:
            return False
    for x in range(0,9):
        if sudoku[x][j]==value:
            return False

    x,y=int(i)//int(3),int(j)//int(3)
    x,y=x*3,y*3
    for X in range(0,3):
        for Y in range(0,3):
            if sudoku[x+X][y+Y]==value:
                return False
    

    return True


issafe(0,1,1)
def Sudoku(i,j):
    if(j==9):
        return Sudoku(i+1,0)
    if(i==9):
        return True

    for y in range(0,9):
        if sudoku[i][y]==-1:
            break


    if y==8 and sudoku[i][y]!=-1:
        return Sudoku(i+1,0)


    for value in range(1,10):
        if issafe(i,y,value):
            sudoku[i][y]=value
            if Sudoku(i,y+1):
                return True
            sudoku[i][y]=-1

    return False


Sudoku(0,0)
with open("solved.txt","w") as File:
    for x in sudoku:
        for i in x:
            File.write(str(i)+" ")
        File.write("\n")



    
    
    

    

