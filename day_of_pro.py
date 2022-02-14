import os


def dayOfProgrammer(year):
  if year == 1918:
    return "26.09.1918"
  if year < 1918:
    if (year%4 == 0):
      return f"12.09.{year}"
    else:
      return f"13.09.{year}"
  
  else:
    if (year%400)==0:
      return f"12.09.{year}"
    else:
      if (year%4 == 0) and (year%100 != 0):
        return f"12.09.{year}"
      else:
        return f"13.09.{year}"
    

if __name__ == '__main__':
  fptr = open(os.environ["OUTPUT_PATH"],"w")
  year = int(input().strip())
  result = dayOfProgrammer(year)
  fptr.write(str(result)+"\n")
  fptr.close()

