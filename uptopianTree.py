


def utopianTree (n):
  if n == 0:
    return 1 
  if n== 1:
    return 2 
    
  height = 0 
  for i in range(n+1):
    if i%2 == 0:
      height+=1 
    else:
      height*=2 
  return height

t = int(input())
for _ in range(t):
  n = int(input())
  print(utopianTree(n))