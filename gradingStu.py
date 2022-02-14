import math,os,random,sys,re 

def gradingStudents(arr):
  for i in range(len(arr)):
    n = arr[i] 
    multiple = n+(5-n%5)
    if n >= 40 or multiple >= 40:
      if (multiple - n) < 3:
        arr[i] = multiple 
        
  return arr 

if __name__ == "__main__":
  fptr = open(os.environ["OUTPUT_PATH"],"w")
  grades_count = int(input().strip())
  grades =[]
  for _ in range(grades_count):
    item = int(input().strip()) 
    grades.append(item)
        
  result = gradingStudents(grades)
  fptr.write("\n".join(map(str,result)))
  fptr.write("\n")
