import math
no_tc = int(input())

for i in range(no_tc):
  num = int(input())
  
  if(math.floor(math.log2(num)) == math.log2(num)):
    print("YES")
  else:
    print("NO")