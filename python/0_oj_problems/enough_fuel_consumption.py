fuel_eff, distance_to_travel = list(map(int, input().split()))

fuel_consumed = fuel_eff * distance_to_travel
if fuel_consumed > 50:
    print("Enough")
else:
    print("Go On")


