def twoStrings(s1,s2):
  for i in s1:
    if i in s2:
      return "YES"
        
  return "NO"

#O(n)

t = int(input())
for _ in range(t):
  s1,s2=input(),input()
  print(twoStrings(s1,s2))
