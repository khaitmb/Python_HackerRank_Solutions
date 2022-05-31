# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.

# INPUT FORMAT
# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

# OUTPUT FORMAT
# Print the runner-up score.

# HACKER-RANK ACCEPTED SOLUTION
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
score = []
for i in arr:
    if i not in score:
        score.append(i)
score.sort(reverse = True)
print(score[1])
