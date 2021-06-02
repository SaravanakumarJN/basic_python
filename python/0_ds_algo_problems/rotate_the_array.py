tc = int(input())

for i in range(tc):
    n, k = map(int, input().strip().split(" "))
    array = list(map(int, input().strip().split(" ")))

    no_rotation = n - (k%n)
    head = array[0: no_rotation]
    tail = array[no_rotation:]
    result_array = tail + head
    print(*result_array)
