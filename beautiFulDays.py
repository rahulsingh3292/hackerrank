def reverse(n):
  n = n 
  rev = 0
  while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
  return rev 
  
def beautifulDays(i,j,k):
  count = 0 
  for n in range(i,j+1):
    num = (n - reverse(n))/k
    if num.is_integer():
      count+=1 
  return count 

fmi = input().split()
i,j,k = int(fmi[0]),int(fmi[1]),int(fmi[2])
result = beautifulDays(i,j,k)
print(result)
  