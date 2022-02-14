import os,re,sys,math,random



def countapplesAndoranges(s,t,a,b,apples,oranges):
  
  apples_count=oranges_count= 0 
  
  for i in range(len(apples)):
    apples[i] = a+apples[i]
  
  for j in range(len(oranges)):
    oranges[j] = b+oranges[j]
  
  for i in range(len(apples)):
    if (apples[i] >= s) and (apples[i] <=t):
      apples_count+=1 
      
  for j in range(len(oranges)):
    if (oranges[j] >= s)and (oranges[j]<=t):
      oranges_count+=1 
  
  print(f"{apples_count}\n{oranges_count}")
  O(n^2) + 
  
if __name__ == '__main__':
  fmi = input().rstrip().split()
  s,t = int(fmi[0]),int(fmi[1])
  smi = input().rstrip().split()
  a,b = int(smi[0]),int(smi[1])
  third_multiple_input=input().rstrip().split()
  m,n = int(third_multiple_input[0]),int(third_multiple_input[1])
  apples = list(map(int,input().rstrip().split()))
  oranges= list(map(int,input().rstrip().split()))
  countapplesAndoranges(s,t,a,b,apples,oranges)
