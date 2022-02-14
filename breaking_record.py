import os 
def breakingRecords(scores):
  minimum=maximum = scores[0]
  min,max= 0,0
  for i in range(len(scores)):
   
   """
   s , min , max , mn , mx
   12 , 12 , 12 , 0 , 0 
   24 , 12 , 24 , 0 , 1 
   10 , 10 , 24 , 1 , 1 
   24 , 10 , 24 , 1 , 1 
   """
  
   score = scores[i]
   
   if score > maximum:
     max+=1 
   
   
   if score < minimum:
     min+=1 
   
   
   if (score <= minimum):
     minimum = score 
   
   if score > maximum:
     maximum  = score 
   
  return [max,min]

    
if __name__ == '__main__':
  fptr = open(os.environ["OUTPUT_PATH"],"w")
  n = int(input())
  scores = list(map(int,input().rstrip().split()))
  result = breakingRecords(scores)
  fptr.write(''.join(map(str,result)))
  fptr.write("\n")
  fptr.close()
  
  