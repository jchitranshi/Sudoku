from tkinter import *


#Sudoku_solver_code
# Function to Find the entry in the Grid that is still  not used 
# Searches the grid to find an entry that is still unassigned. If 
# found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries 
# remain, false is returned. 
# 'l' is a list  variable that has been passed from the solve_sudoku function 
# to keep track of incrementation of Rows and Columns 
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
  
def sudokuSolver():
    #lbl=Label(root,text="Hello!!")
    n=9
    global board 
    board = [[0 for x in range(n)] for y in range(n)]
    board[0][0]=5
    board[0][1]=3
    board[0][4]=7

    board[1][0]=6
    board[1][3]=1
    board[1][4]=9
    board[1][5]=5

    board[2][1]=9
    board[2][2]=8
    board[2][7]=6

    board[3][0]=8
    board[3][4]=6
    board[3][8]=3

    board[4][0]=4
    board[4][3]=8
    board[4][5]=3
    board[4][8]=1

    board[5][0]=7
    board[5][4]=2
    board[5][8]=6

    board[6][1]=6
    board[6][6]=2
    board[6][7]=8

    board[7][3]=4
    board[7][4]=1
    board[7][5]=9
    board[7][8]=5

    board[8][4]=8
    board[8][7]=7
    board[8][8]=9
    
    solve_sudoku(board)
    #lbl=Label(root,text=board[0][0])

    #check if entered num is correct!
    #entered_num=e.get()
    #row=e.grid_info()['row']
    #column=e.grid_info()['column']
    #print(e.get())
    #print("Grid position of 'btn': {} {}".format(row, column))
    #lbl.grid(row=14,column=4)
    print(board)

   



sudokuSolver()



#test
rows=[]
for i in range(9):
    cols=[]
    for j in range(9):
        if i==0 and j==0:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.grid(row=i,column=j,sticky=NSEW)
            e.insert(0,"5")
            e.configure(state=DISABLED)

        elif i==0 and j==1:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.grid(row=i,column=j,sticky=NSEW)
            e.insert(0,"3")
            e.configure(state=DISABLED)

        elif i==0 and j==4:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"7")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        
        elif i==1 and j==0:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"6")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        
        elif i==1 and j==3:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"1")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        
        elif i==1 and j==4:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"9")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        
        elif i==1 and j==5:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"5")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        
        elif i==2 and j==1:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"9")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==2 and j==2:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"8")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==2 and j==7:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"6")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==3 and j==0:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"8")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==3 and j==4:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"6")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==3 and j==8:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"3")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==4 and j==0:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"4")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==4 and j==3:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"8")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==4 and j==5:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"3")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==4 and j==8:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"1")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==5 and j==0:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"7")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==5 and j==4:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"2")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==5 and j==8:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"6")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==6 and j==1:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"6")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==6 and j==6:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"2")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==6 and j==7:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"8")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==7 and j==3:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"4")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==7 and j==4:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"1")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==7 and j==5:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"9")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==7 and j==8:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"5")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==8 and j==4:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"8")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==8 and j==7:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"7")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        elif i==8 and j==8:
            e= Entry(relief=SUNKEN,width=5,borderwidth=1)
            e.insert(0,"9")
            e.configure(state=DISABLED)
            e.grid(row=i,column=j,sticky=NSEW)
        
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