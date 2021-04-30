string = "LLRDDR"

x_coord = 0
y_coord = 0
for i in string:
    if i == "L":
        x_coord -= 1
    elif i == "R":
        x_coord += 1
    elif i == "U":
        y_coord += 1
    else:
        y_coord -= 1

print(x_coord, y_coord)