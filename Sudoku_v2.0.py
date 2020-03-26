from random import randint
from tkinter import *
from copy import copy, deepcopy
import array 

def fill_diagonal_box():
	global partial_board
	arr=array.array('i',[0,0,0,0,0,0,0,0,0,0]) 
	for i in range(3):
		for j in range(3):
			rand=randint(1,9)
			while(arr[rand-1]!=0):
				rand=randint(1,9)
			arr[rand-1]=1
			partial_board[i][j]=rand

	arr=array.array('i',[0,0,0,0,0,0,0,0,0,0])
	for i in range(3,6):
		for j in range(3,6):
			rand=randint(1,9)
			while(arr[rand-1]!=0):
				rand=randint(1,9)
			arr[rand-1]=1
			partial_board[i][j]=rand

	arr=array.array('i',[0,0,0,0,0,0,0,0,0,0])
	for i in range(6,9):
		for j in range(6,9):
			rand=randint(1,9)
			while(arr[rand-1]!=0):
				rand=randint(1,9)
			arr[rand-1]=1
			partial_board[i][j]=rand
	#print(partial_board)

def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# in the specified row matches the given number. 
def used_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# in the specified column matches the given number. 
def used_in_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 box matches the given number 
def used_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
  
# Checks whether it will be legal to assign num to the given row,col 
#  Returns a boolean which indicates whether it will be legal to assign 
#  num to the given row,col location. 
def check_location_is_safe(arr,row,col,num): 
      
    # Check if 'num' is not already placed in current row, 
    # current column and current 3x3 box 
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num) 
  
# Takes a partially filled-in grid and attempts to assign values to 
# all unassigned locations in such a way to meet the requirements 
# for Sudoku solution (non-duplication across rows, columns, and boxes) 
def solve_sudoku(arr): 
      
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
    l=[0,0] 
      
    # If there is no unassigned location, we are done     
    if(not find_empty_location(arr,l)): 
        return True
      
    # Assigning list values to row and col that we got from the above Function  
    row=l[0] 
    col=l[1] 
      
    # consider digits 1 to 9 
    for num in range(1,10): 
          
        # if looks promising 
        if(check_location_is_safe(arr,row,col,num)): 
              
            # make tentative assignment 
            arr[row][col]=num 
  
            # return, if success, ya! 
            if(solve_sudoku(arr)): 
                return True
  
            # failure, unmake & try again 
            arr[row][col] = 0
              
    # this triggers backtracking         
    return False 

def removeKelements(k):
	count=k;
	while(count):
		rand=randint(1,80)
		i=rand/9;
		j=rand%9;
		if(partial_board[int(i)][j]!=0):
			count-=1
			partial_board[int(i)][j]=0

def sudokuSolver():
	global partial_board
	global board
	partial_board = [[0 for x in range(9)] for y in range(9)]
	fill_diagonal_box()
	board=deepcopy(partial_board)
	solve_sudoku(board)
	partial_board=deepcopy(board)
	print(partial_board)
	removeKelements(40)

sudokuSolver()

rows=[]
for i in range(9):
    cols=[]
    for j in range(9):
        if partial_board[i][j]!=0:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.grid(row=i,column=j,sticky=NSEW)
            e.insert(0,str(partial_board[i][j]))
            e.configure(state=DISABLED)

        else:
            e=Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.grid(row=i,column=j,sticky=NSEW)
            e.insert(0,"")
            #e.configure(show='*')
       
        cols.append(e)
    rows.append(cols)


def onPress():
    r=0
    c=0
    global A
    for row in rows:
        c=0
        for col in row:
            if (c<9 and col.get()==str(board[r][c])):                   
                A=True             
                lbl=Label(relief=RIDGE,text="Correct")
                lbl.grid(row=14,column=1,columnspan=7,sticky=NSEW)
                #lbl.grid_forget()
            else:
                #print("else:"+col.get())
                lbl.grid_forget()
                if col.get()!="" and col.get()!=str(board[r][c]):
                    #if A==True:                    
                    A=False
                    lbl=Label(relief=RIDGE,text="Incorrect")
                    lbl.grid(row=14,column=1,columnspan=7,sticky=NSEW)
                    #lbl1.grid_forget()
                    break
                #lbl.grid_forget()
            #break
            c+=1
        #break
        if A==False:
            break
        r+=1

Button(text='Check', command=onPress).grid(row=12,column=0,columnspan=10)

mainloop()   


