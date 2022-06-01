# Skills Used: split, join, defining a function

# TASK
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# HACKERRANK ACCEPTED SOLUTION
def split_and_join(line):
    split = line.split(" ")
    join = "-".join(split)
    return join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
