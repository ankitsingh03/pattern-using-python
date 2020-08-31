        *
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************


n = 9
lst = []
for i in range(1, n*2, 2):
	lst.append(i * '*')
for i in range(len(lst)):
	print(" "*(n-i-1) + lst[i])

n = 9
k = 0
for i in range(0, n*2, 2):
	print(" "*(n-1-k)+'*'*(i+1))
	k += 1
