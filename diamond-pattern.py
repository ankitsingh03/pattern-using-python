n = 6
s = []
for i in range(1, n+1, 2):
    s.append(["*"*i])
for i in range(len(s)):
    print(" "*(len(s)-1-i), end=" ")
    print(*s[i])
for i in range(len(s)-2, -1, -1):
    print(" " * (len(s) - 1 - i), end=" ")
    print(*s[i])

# output
'''
   *
  ***
 *****
  ***
   *
'''
