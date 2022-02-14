def countValley(n,string):
  x,count,flag = 0,0,False 
  for i in range(len(string)):
    if string[i] == "U":
      x+=1 
      
      if x>=0:
        flag = False 
        
    else:
      x-=1
      
      if x<0 and flag==False:
        count+=1 
        flag = True 
      
  return count 


n = int(input())
string = input().strip()
print(countValley(n,string))
        
  
  

    
  