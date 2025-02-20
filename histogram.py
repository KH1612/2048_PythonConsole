marks = input('Enter a space-separated list of marks:\n') #User inputs a string containing marks
marks = marks.split(' ') #Marks put in a list

results = {'fail':0, 'third':0,'second_minus':0,'second_plus':0,'first':0} #Dictionary of mark boundries

for i in marks: # List of marks looped through and dictionary value updated based on marks
    if int(i) < 50:
        results['fail'] += 1
    elif int(i) < 60:
        results['third'] += 1
    elif int(i) < 70:
        results['second_minus'] += 1
    elif int(i) < 75:
        results['second_plus'] += 1
    else:
        results['first'] += 1
#Output of histogram using dictionary
print('1 |' + 'X' * results['first'] )
print('2+|' + 'X' * results['second_plus'] )
print('2-|' + 'X' * results['second_minus'] )
print('3 |' + 'X' * results['third'] )
print('F |' + 'X' * results['fail'] )

    