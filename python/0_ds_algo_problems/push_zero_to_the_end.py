def transform_array(array):
    zero_array = []
    non_zero_array = []
    for i in array:
        if i == "0":
            zero_array.append(i)
        else:
            non_zero_array.append(i)
    result_array = non_zero_array + zero_array
    print(*result_array)

tc = int(input())

for i in range(tc):
    n = int(input())
    array = list(input().strip().split())
    transform_array(array)
    