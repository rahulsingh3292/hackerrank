import os 
def kangaroo(x1,v1,x2,v2):
  if v1 > v2:
    r = (x1-x2)%(v2-v1)
    if r == 0:
      return "YES"
    return "NO"
  return "NO"


if __name__ == '__main__':
  fptr = open(os.environ["OUTPUT_PATH"],"w")
  i = input().rstrip().split()
  x1,v1,x2,v2 = int(i[0]),int(i[1]),int(i[2]),int(i[3])
  
  result = kangaroo(x1,v1,x2,v2)
  fptr.write(result+"\n")
  fptr.close()