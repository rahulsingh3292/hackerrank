
import os 

def divisibleSumPairs (n,arr,k):
  pairs = 0 
  for i in range (n-1):
    for j in range(i,n):
      if (i < j) and (arr[i]+arr[j])%k == 0:
        pairs+=1 
  return pairs 

if __name__ == '__main__':
  fptr = open(os.environ["OUTPUT_PATH"],"w")
  fmi = input().rstrip().split()
  n = int(fmi[0])
  k = int(fmi[1])
  ar = list(map(int ,input().rstrip().split()))
  
  result = divisibleSumPairs(n,ar,k)
  fptr.write(str(result)+"\n")
  fptr.close()