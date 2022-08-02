# Skills Used: for loop, if statement, basic computation, input, format

# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the 
# average of the marks array for the student name provided, showing 2 places after the decimal.

# INPUT FORMAT
# The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, 
# each value separated by a space. The final line contains query_name, the name of a student to query.

# OUTPUT FORMAT
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
for i in student_marks:
    if i == query_name:
        tot = sum(student_marks[i])
        avg = tot / 3
        format_avg = "{:.2f}".format(avg)
        print(format_avg)
        
        
        
