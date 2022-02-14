

def catAndMouse(x,y,z):
  x ,y =  abs(x-z),abs(y-z)
  if x==y:
    return "Mouse C"
  
  if x < y:
    return "Cat A"
  else:
    return "Cat B"
  
if __name__ == '__main__':
  q = int(input())
  for _ in range(q):
    tmi = input().split()
    x,y,z = int(tmi[0]),int(tmi[1]),int(tmi[2])
    print(catAndMouse(x,y,z))