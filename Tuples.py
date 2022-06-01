# TASK
# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those  integers. Then compute and print the result of hash(t).

# HACKERRANK ACCEPTED SOLUTION
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
 
for i in range(n):
    t = tuple(integer_list)
print(hash(t))
