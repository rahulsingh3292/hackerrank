import os
def climbingLeaderboard(ranked,player):
  scores = list(set(ranked))
  scores.sort()
  n = len(scores)
  result =[]
  i = 0
  for alscore in player:
    while (i < n) and (scores[i] <= alscore):
      i+=1
    result.append(n-i+1)
  
  return result
r = int(input())
ranked = list(map(int,input().rstrip().split()))
p = int(input())
player = list(map(int,input().rstrip().split()))

for i in climbingLeaderboard(ranked,player):
  print(i)

