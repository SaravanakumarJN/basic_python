def tables(n):
    answer = ""
    for i in range(1, 11):
        answer += str(i * n) + " "
    print(answer.strip())

tc = int(input())

for i in range(tc):
    n = int(input())
    tables(n)