def even_sum_possibility(array):
  for ele in array:
    if (ele % 2) == 0:
      print("YES")
      return
  if (len(array) % 2) == 0:
    print("YES")
  else:
    print("NO")

no_tc = int(input())

for i in range(no_tc):
  n = int(input())
  array = list(map(int, input().strip().split(" ")))
  even_sum_possibility(array)
  