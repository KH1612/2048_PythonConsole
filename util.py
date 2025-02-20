import copy
def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    for i in range(4): # Adds 4 rows of 4 zeros to grid
        grid.append([0,0,0,0])
        
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box""" 
    close = '+--------------------+' #Top and bottom of box
    fgrid ='' #Middle part of box
    for y in range(4):
        line = '|' # Line is reset
        for x in range(4):
            if grid[y][x]==0: #Zero is shown as blank space in grid
                line = line + '{0:<5}'.format('')
            else: # Number is formated to 5 spaces and added to line    
                line = line + '{0:<5}'.format(grid[y][x]) 
        fgrid = fgrid + line +'|' +'\n' 
    final = close + '\n'+ fgrid + close #Box is formed
    print(final)

def check_lost (grid):    
    """return True if there are no 0 values and there are no
    adjacent values that are equal; otherwise False""" 
    for y in range(4): #Looping through grid horizontaly
        for x in range(3):
            if (grid[y][x] == 0) or (grid[y][x+1] == 0) or (grid[y][x] == grid[y][x+1]): # Checks for zeros and adjacent values
                return False #False returned as soon as 0 or adjacent equal numbers found
    for x in range(4): #Looping through grid verticaly
        for y in range(3):
            if (grid[y][x] == 0) or (grid[y+1][x] == 0) or (grid[y][x] == grid[y+1][x]): #Checks for zeros and adjacent values
                return False #False returned as soon as 0 or adjacent equal numbers found             
    return True #All indexes checked and no 0 values or adjacent equal numbers
        
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for y in range(4):
        for x in range(4):
            if grid[y][x] >= 32:
                return True # True returned as soon as an index is > than 32 
    return False #False returned after all indexes are checked an no number > 32 is found

def copy_grid (grid):
    """return a copy of the given grid"""
    return copy.deepcopy(grid) #Deep copy of grid is created

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value""" 
    if grid1 == grid2: #Checks if both inputted grids are the same
        return True
    else:
        return False
