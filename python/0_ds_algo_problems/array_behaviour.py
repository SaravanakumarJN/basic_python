def cons_odd_check(array):
    assumption = False
    for i in range(1, len(array)):
        if array[i] % 2 != 0 and array[i-1] % 2 != 0:
            assumption = True 
    return assumption
    

tc = int(input())

for i in range(tc):
    n = int(input())
    array = list(map(int, input().strip().split(" ")))

    if cons_odd_check(array):
        print("Misbehave!")
    else:
        print("Behave!")
