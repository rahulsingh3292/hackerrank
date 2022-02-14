import os 

def sockMerchant(n,arr):
  m_arr = set(arr)
  count = 0
  for i in m_arr:
    count+= arr.count(i)//2 
  return count 

if __name__ == '__main__':
   fptr = open(os.environ["OUTPUT_PATH"],"w") 
   n = int(input())
   arr = list(map(int,input().rstrip().split()))
   result = sockMerchant(n,arr)
   fptr.write(str(result)+"\n")
   fptr.close()