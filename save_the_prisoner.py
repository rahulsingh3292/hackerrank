def saveThePrisoner(n,m,s):
  m = m%n 
  s = m+s-1 
  if s>n:
    s = s%n 
  if s==0:
    return n 
  return s 
  #O(1)
t = int(input())
for _ in range(t):
  
  fmi = input().split()
  n,m,s = int(fmi[0]),int(fmi[1]),int(fmi[2])
  print(saveThePrisoner(n,m,s))

