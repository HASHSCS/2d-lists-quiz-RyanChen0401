# TODO: Implement a function that takes a two-dimensional list and returns the sum of each row
def sum_each_row(two_d_list):
    total = []
    for row in two_d_list:
        Sum = sum(row)
        total.append(Sum)
    return total

# TODO: Implement a function that counts the number of non-zero elements in a two-dimensional list
def count_non_zero(two_d_list):
    c = 0
    for row in two_d_list:
        for i in row:
            if i != 0:
                c += 1
    return c

# TODO: Implement a function that extracts and returns the last element of each row in a two-dimensional list
def last_elements(two_d_list):
    last = []
    for row in two_d_list:
        if row:
            last.append(row[len(row)-1])
    return last
# TODO: Implement a function that counts the number of times a given value appears in a two-dimensional list
def count_occurrences(two_d_list, value):
    c = 0
    for row in two_d_list:
        for i in row:
            if i==value:
                c+=1
    return c
