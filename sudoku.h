#pragma once
#include<stdio.h>
#include<string.h>
class sudoku
{
    // pointer to pointer 2d Array
    int** arr;


//---------------Main Code Of Solving Sudoku--------------
// Issafe Function Check Condition For Placing value in i,j Place
    bool Issafe(int** arr,int i,int j,int value)
    {
        // Check All Block In i'th Row If value Is Already Present
        for(int x=0;x<9;x++)
        {
            if(arr[i][x]==value)
                return false; // When value Already Present
        }
        // Check All Row In Same j'th Block If Found value return false
        // Because It Not Safe
        for(int y=0;y<9;y++)
        {
            if(arr[y][j]==value)
                return false;
        }
        int X=i/3;
        int Y=j/3;
        X*=3;
        Y*=3;
        //Checking 3X3 Block
        for(int x=0;x<3;x++)
        {
            for(int y=0;y<3;y++)
            {
                if(arr[X+x][Y+y]==value)
                    return false;
            }
        }
        //After Checking All Sodulu Rule That Mean value in i,j Is Full Fill Requirement
        return true;
    }


//__solve function edit arr and return boolen value if false that mean it impossible to solve 

    bool __solve(int** arr,int i,int j)
    {
        //Base Case When i==9 That Mean Soduku Row Is Finish
        if(i==9)
            return true;
        int x;  //It Store Empty Or Blank Index of column in i'th row
        //for loop To Find Empty Or Blank Spot
        for(x=j;x<9;x++)//x=j Because Before j'th index Already Filled Or Filled By Code 
        {
            if(arr[i][x]==-1)
            {
                break;
            }
        }
        //If Any Row Those Not Have Any Blank Value Then x become x==9
        //So Jump To Next Row(i+1) and Start With 0 Block
        if(x==9)
            return __solve(arr,i+1,0);
        
        //for loop to check all 1-9 value by placing
        for(int value=1;value<10;value++)
        {
            if(Issafe(arr,i,x,value))
            {
                arr[i][x]=value;    //If It Safe Then Allocate Value;
                if(__solve(arr,i,x))    //If Base Case Hit All If Throw true
                    return true;
                arr[i][x]=-1;        //If Base Case Doesn't Hit Then Place -1 And Check For Another Value
            }
        }
        return false;
    }
    public:
    sudoku(const char* __url)
    {
    // Allocation Of Dynamic 2D Array Size Of 9 Block Or Row
    arr=new int*[9];


    // Allocation Of All Row With 9 Block Which Act Like Column
    for(int i=0;i<9;i++)
        arr[i]=new int[9];
    #ifndef SOLVING
        //freopen_s(__url,"r", stdin);
        freopen( __url, "r", stdin);
        freopen("solved.txt","w",stdout);
    #endif
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                scanf("%d",&arr[i][j]);
            }
        }
    }
    bool solve()
    {
        //This Function Solve Sudoku
       return __solve(arr,0,0);
    }
    void getSudoku()
    {
        //This Function Print Element Of Sudoku
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                printf("%d ",arr[i][j]);
            }
            printf("\n");
        }
    }
    ~sudoku()
    {
        //Releasing All Allocated Memory
        for(int i=0;i<9;i++)
            delete[] arr[i];
    }
};