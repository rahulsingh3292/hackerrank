import os 


def pageCount(n,p):
  mx = 0 
  mn = 0 
  
  if n >= 1 :
    if p==1:
      return 0 
  
  if n%2==0:
    if p==n-1:
      return 1 
  
  for i in range(2,n,2):
    if i==p or i+1 == p:
      mx+=1 
      break 
    mx+=1 
  
  for j in range(n,1,-2):
    if j==p or j-1 == p:
      break 
    mn+=1 
  
  return min([mx,mn])
 
n,p = int(input()) ,int(input())
print(pageCount(n,p))


