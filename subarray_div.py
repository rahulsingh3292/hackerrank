import os ,math 

  
def birthday (arr,d,m):
  
  if len(arr) == 1 and s[0] == d :
    return 1 
  
  count = 0 
  for i in range((len(arr)-m)+1):
    sums = 0 
    for j in range(i,i+m):
      sums+=arr[j]
    
    if sums == d:
      count+=1 
    
  return count 
 



if __name__ == "__main__":
  fptr = open(os.environ["OUTPUT_PATH"],"w")
  n = int(input().strip())
  s = list(map(int,input().rstrip().split()))
  fmi = input().rstrip().split()
  d = int(fmi[0])
  m = int(fmi[1])
  result = birthday(s,d,m)
  fptr.write(str(result)+"\n")
  fptr.close()



