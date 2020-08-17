n = 5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,i+i):
        print(j,end="")
    for k in range(j-1,i-1,-1):
        print(k,end='')
    print()


'''
    1
   232
  34543
 4567654
567898765
'''
