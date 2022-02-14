def char_find(char):
  chars =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  return chars.index(char)


def designerPdfViewer(h,string):
  lst =[h[char_find(i)] for i in string]
  return max(lst)*len(string)

h = list(map(int,input().rstrip().split()))
string = input().rstrip()
result = designerPdfViewer(h,string)
print(result)

  