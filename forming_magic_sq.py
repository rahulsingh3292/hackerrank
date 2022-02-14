""""
 8,1,6|6,7,2|4,3,8|2,9,4
 3,5,7|1,5,9|9,5,1|7,5,3
 4,9,2|8,3,4|2,7,6|6,1,8
 -----------------------
 8,3,4 |2,7,6|6,1,8|4,9,2
 1,5,9 |9,5,1|7,5,3|3,5,7
 6,7,2 |4,3,8|2,9,4|8,1, 6
 ------------------------
"""

def doSum(s,a,b,c,d,e,f,g,h,i):
  return abs(a-s[0][0])+abs(b-s[0][1])+abs(c-s[0][2])+abs(d-s[1][0])+abs(e-s[1][1])+abs(f-s[1][2])+abs(g-s[2][0])+abs(h-s[2][1])+abs(i-s[2][2])

def formingMagicSquare(s):
  lst = [0]*8
  
  lst[0] = doSum(s,8,1,6,3,5,7,4,9,2)
  lst[1] = doSum(s,6,7,2,1,5,9,8,3,4)
  lst[2] = doSum(s,4,3,8,9,5,1,2,7,6)
  lst[3] = doSum(s,2,9,4,7,5,3,6,1,8)
  lst[4] = doSum(s,8,3,4,1,5,9,6,7,2)
  lst[5] = doSum(s,2,7,6,9,5,1,4,3,8)
  lst[6] = doSum(s,6,1,8,7,5,3,2,9,4)
  lst[7] = doSum(s,4,9,2,3,5,7,8,1,6)
 
  min = lst[0]
  for i in range(1,8):
    if min > lst[i]:
      min = lst[i]
    
  return min 


s = []
for _ in range(3):
  lst = list(map(int,input().rstrip().split()))
  s.append(lst)
  
print(formingMagicSquare(s))
