new_zealand = list(map(int, input().strip().split(" ")))
england = list(map(int, input().strip().split(" ")))

if new_zealand[0] > england[0]:
    print("New Zealand")
elif england[0] > new_zealand[0]:
    print("England")
else:
    if new_zealand[1] > england[1]:
        print("New Zealand")
    elif england[1] > new_zealand[1]:
        print("England")
    else:
        if new_zealand[2] > england[2]:
            print("New Zealand")
        elif england[2] > new_zealand[2]:
            print("England")