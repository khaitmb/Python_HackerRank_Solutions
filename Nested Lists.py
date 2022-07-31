# Skills Used: input, for loop, if statement, list generation, nested lists

# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) 
# having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# INPUT FORMAT
# The first line contains an integer, N , the number of students.
# The 2N subsequent lines describe each student over  lines.
# The first line contains a student's name.
# The second line contains their grade.

# OUTPUT FORMAT
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically 
# and print each one on a new line.

# HACKER-RANK ACCEPTED SOLUTION
records = []
grades = []
scores = []

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        
        grades.append(name)
        grades.append(score)
        
        scores.append(score)

        records.append(grades)
        grades = []

scores.sort()
scores = list(set(scores))

second_lowest = []
for list in records:
    if list[1] == scores[1]:
        second_lowest.append(list[0])

second_lowest.sort()
for i in second_lowest:
    print(i)
    
    
    
