def earnings(heights, rupees):
    curr_height = 0
    buildings_covered = 0
    
    for ele in heights:
        if ele > curr_height:
            curr_height = ele
            buildings_covered += 1

    return buildings_covered * rupees 

tc = int(input())

for i in range(tc):
    N, R = map(int , input().strip().split(" "))
    heights = list(map(int, input().strip().split(" ")))

    print(earnings(heights, R))


    