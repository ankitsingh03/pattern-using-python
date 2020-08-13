'''
* # # # # # # # # #
# # # # # # # # * *
* * * # # # # # # #
# # # # # # * * * *
* * * * * # # # # #
# # # # # * * * * *
* * * * # # # # # #
# # # # # # # * * *
* * # # # # # # # #
# # # # # # # # # *
'''

n = 5
lst = []
for j in range(n*2):
    lst.append('#')
    
#print first half of pattern    
for i in range(1,n+1):
    lst[i-1] = '*'
    if i % 2 != 0:
        print(*lst)
    else:
        print(*reversed(lst))

#print second half of pattern
for i in range(n,0,-1):
    lst[i] = '#'
    if i % 2 != 0 :
        print(*reversed(lst))
    else :
        print(*(lst))
