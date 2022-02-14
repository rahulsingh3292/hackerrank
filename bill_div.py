

def bonAppetit(bill,k,b):
  total = 0 
  for i in range(len(bill)):
    if i != k:
      total+=bill[i]
  bactual = total//2 
  bcharged = b 
  if bcharged == bactual:
    print("Bon Appetit")
  else:
    print(bcharged - bactual)


if __name__ == '__main__':
  fmi = input().rstrip().split()
  n , k= int(fmi[0]),int(fmi[1])
  bill = list(map(int,input().rstrip().split()))
  b = int(input().strip())
  bonAppetit(bill,k,b)
  