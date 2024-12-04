'''
Meagan, Grade 8, Computer Science
This program demonstrates nested loops to 
create a times table
'''

num = 10
# For every row number, print colums number
for i in range (1, num+1):  # rows
    for j in range (1, i + 1):  # columns
        print('.', end= '')
    print()

