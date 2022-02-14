
def getMoneySpent(keyboards,drives,budget):
  keyboards.sort()
  drives.sort()
  ans = set()
  for i in keyboards:
    for j in drives:
      if i+j <= budget:
        ans.add(i+j)
  
  if len(ans) == 0:
    return -1 
    
  return max(list(ans))

# O(n^2)

if __name__ == '__main__':
  bnm = input().split()
  b = int(bnm[0])
  n = int(bnm[1])
  m = int(bnm[2])
  k = list(map(int,input().rstrip().split()))
  d = list(map(int,input().rstrip().split()))

  result = getMoneySpent(k,d,b)
  print(result)
  

    
  
    
  

