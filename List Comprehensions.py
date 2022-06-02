# TASK
# You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by  on a 
# 3D grid where the sum of i+j+k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. Use list comprehensions rather than multiple loops.

# HACKERRANK ACCEPTED SOLUTION
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i+j+k != n])
