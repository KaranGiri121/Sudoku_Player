#include<iostream>
#include"sudoku.h"
using namespace std;
int main()
{
	sudoku temp("sudoku.txt");
	temp.solve();
	temp.getSudoku();
}
