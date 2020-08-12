'''
    1--------------0
   1 1------------1
  1 2 1----------2
 1 3 3 1--------3
1 4 6 4 1------4
'''

n = 5
lst = []
# use for number of row
for i in range(n):
    inner_lst = []
    # use for number of column
    for j in range(i+1):
        #insert 1 on first and last position
        if j == 0 or j == i:
            inner_lst.append(1)
        #insert middle values
        else:
            inner_lst.append(lst[i-1][j-1] + lst[i-1][j])
    lst.append(inner_lst)

for i in range(n):
    #use for space print
    print(" " * (n-i-1), end="")
    #unpack the list
    print(*lst[i])
