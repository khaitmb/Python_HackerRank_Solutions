# Without using any string methods, try to print the following: 123...n
# Print the list of intergers from 1 through n as a string, without spaces.

# HackRank Accepted Solution:
print(*range(1, n+1), sep ='')
