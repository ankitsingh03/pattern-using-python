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
        if j == 0 or j == i:
            inner_lst.append(1)
        else:
            inner_lst.append(lst[i-1][j-1] + lst[i-1][j])
    lst.append(inner_lst)

for i in range(n):
    print(" " * (n-i-1), end="")
    print(*lst[i])
