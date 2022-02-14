
def angryProfessor(arr,n):
  arr.sort()
  student=0 
  for i in range(len(arr)):
    if arr[i] > 0:
      break 
    student+=1 
    
  if student >= n:
    return "NO"
  return "YES"


t = int(input())
for _ in range(t):
  fmi = input().split()
  n,k= int(fmi[0]),int(fmi[1])
  arr = list(map(int,input().split()))
  result = angryProfessor(arr,k)
  print(result)