'''
*
  * *
    * * *
      * * * *
        * * * * *
      * * * * 
    * * * 
  * * 
* 
'''

n = 5
#insert star in array
lst = []
for i in range(n):
    lst.append('*'*(i+1))
    
#print first half values
for i in range(n):
    print("  " * i,end= "")
    print(*lst[i])

#print second half values
for i in range(n-2,-1,-1):
    print("  " * i, end="")
    #here is second mathod to print star
    for j in lst[i]:
        print(j,end=" ")
    print()
