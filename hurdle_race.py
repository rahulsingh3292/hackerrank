

def hurdleRace(k,height):
  height = list(set(height))
  result = max(height) - k 
  if result >= 1:
    return result
  return 0 


fmi = input().split()
n,k =int(fmi[0]),int(fmi[1])
height=list(map(int,input().rstrip().split()))
print(hurdleRace(k,height))
