n = int(input())
arrray = list(map(int, input().strip().split()))

string = ""
for ele in arrray:
    if ele < 0:
        string += "0"
    else:
        string += str(ele)

print(string)