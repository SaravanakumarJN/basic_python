distance, time = list(map(int, input().split()))

speed = distance / time
if speed > 40:
    print("Apply Brake")
else:
    print("Keep Going")
