def timeConversion(t):

  format = t[-2]+t[-1] 
  if t[:2] == "12" and format=="AM":
    return "00"+t[2:8]
    
  if t[:2] == "12" and format=="PM":
    return "12"+t[2:8]
  
  if format=="PM":
    s = int(t[:2])+12
    return f"{s}{t[2:8]}"
  else:
    return t[:8]
    
time = input()
result = timeConversion(time)
print(result)