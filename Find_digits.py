def findDigits(n):
  k = n 
  digits = 0 
  while k>0:
    num = k%10
    if num !=  0:
      if n%num== 0:
        digits+=1 
    k=k//10 
  return digits 

t = int(input())
for _ in range(t):
  n = int(input())
  result = findDigits(n)
  print(result)