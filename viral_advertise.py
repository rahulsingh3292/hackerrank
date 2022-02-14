
def viralAdvertising(n):
  if n==1:
    return 2 
  if n==2: 
    return 5 
  
  k =  5 
  ans = 2
  temp = 2 
  for i in range(2,n+1):
    n = (k//2)*3 
    
    for j in range(1):
      ans = (n//2)+temp 
     
    k = n 
    temp = ans 
  
  return ans 
    
  
 
   
   
    
n = int(input())    
print(viralAdvertising(n))