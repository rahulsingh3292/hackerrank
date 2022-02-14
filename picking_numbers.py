
def pickingNumbers(arr):
  b = [0]*101
  for i in range(len(arr)):
    b[arr[i]]+=1
  c = []
  for i in range(len(b)-1):
    c.append(abs(b[i] + b[i+1]))
  return max(c)
  
n = int(input())
lst = list(map(int,input().rstrip().split()))

print(pickingNumbers(lst))