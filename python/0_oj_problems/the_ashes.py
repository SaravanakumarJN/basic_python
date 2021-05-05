aus, eng = map(int, input().split())

if aus > eng:
    print("Australia")
elif eng > aus:
    print("England")
else:
    print("Tie")