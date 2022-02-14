
def cloudJump(c,k):
  i = 0 
  n = len(c)
  energy = 100
  while True:
    energy = (energy-1)-2*c[i]
    i = (i+k)%n
    if i == 0:
      break 
  return energy 

fmi = input().split()
n = int(fmi[0])
k= int(fmi[1])
c = list(map(int,input().split()))
result = cloudJump(c,k)
print(result)