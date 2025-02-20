names = [] #Empty list that will hold the names
wordlen = 0 
word = '' 
print('Enter strings (end with DONE):')
while word != 'DONE': #While 'DONE' isn't inputted by user
    word = input('') #User inputs names
    if word != 'DONE': #Done not added to list
        names.append(word) #Names added to list
    if len(word) > wordlen: #Keeps track of how long the longest name is
        wordlen = len(word)
print('\nRight-aligned list:')
for i in names: #Each name is printed
    print("{0:>{rJust}}".format (i, rJust = wordlen)) #Aligned to the right using the longest name as the starting points
    