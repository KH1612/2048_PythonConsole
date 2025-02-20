def rotate (grid):
    '''Rotates the grid by swtiching x and y values'''
    for x in range(4):
        lst = []
        for y in range(4):
            lst.append(grid[y][x]) #Loops through all indexes and swaps x and y values
        grid.append(lst) #New lists added to grid
    for i in range(4): 
        grid.pop(0) #Original 4 grids are removed from grid
    

def push_up(grid):
    """merge grid values upwards"""
    rotate(grid) #Rotated grid
    push_left(grid) #Left push called 
    rotate(grid) #Grid rotated to original state    
    
def push_down (grid):
    """merge grid values downwards"""
    rotate(grid) #Rotated grid
    push_right(grid) #Right push called
    rotate(grid) #Grid is rotated to original state
    
def push_right (grid):
    """merge grid values right"""
    for y in range(4):
        zCount = grid[y].count(0) #Amount of zeros in each list in grid
        for x in range(zCount): 
            grid[y].remove(0) # Removes all zeros from the list
        for x in range(zCount):
            grid[y].insert(0,0) # Puts the zeros back in the list to the left

    for y in range(4):
        for x in range(3,0,-1):
            if grid[y][x] == grid[y][x-1]: #Checks if adjacent values are equal
                grid[y][x] *= 2 # Value to the right is doubled 
                grid[y].pop(x-1) #Value to left is removed 
                grid[y].insert(0,0) #Removed value is replaced with a zero in the first index of list
            
def push_left (grid):
    """merge grid values left"""
    for y in range(4):
        zCount = grid[y].count(0) #Amount of zeros in each list in grid
        for x in range(zCount):
            grid[y].remove(0) # Removes all zeros from the list
        for x in range(zCount):
            grid[y].append(0) #Puts the zeros back in the list to the right 
    
    for y in range(4):
        for x in range(3):
            if grid[y][x] == grid[y][x+1]: #Checks if adjacent values are equal
                grid[y][x] *= 2 #Value to the left is doubled 
                grid[y].pop(x+1) #Value to right is removed 
                grid[y].append(0) #Removed value is replaced with a zero in the last index of list


