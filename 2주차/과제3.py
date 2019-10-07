#1부터 10까지 별찍기
for i in range(1,11):
    for j in range(i):
        print("*",end='')
    print("")
#1부터 10까지 2단위로 별찍기
for i in range(1,11,2):
    for j in range(i):
        print("*",end='')
    print("")
#10부터 1까지 별찍기
for i in range(10,0,-1):
    for j in range(i):
        print("*",end='')
    print("")