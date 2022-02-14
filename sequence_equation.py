
  
def sequenceEquation(p):
  n = len(p)
  result =[]
  for i in range(1,n+1):
    ind = p.index(p.index(i)+1)+1
    result.append(ind)
  return result 

n = int(input())
p = list(map(int,input().split()))
for i in sequenceEquation(p):
  print(i)