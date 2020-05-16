for a in range(1,10+1):
    if a <=5:
        print("小さいです")
    else:
        print("大きいです")

for a in range(1,10+1):
    print(a)
    if a%2==0:
        print("〇")
    if a%3==0:
        print("×")
    if (a%2==0) and ( a%3==0):
        print("△")