players = ["황의조","황희찬","구자철","이재성","기성용"]

print("현재 경기 중인 선수:")
for i in players:
    print(i)

print("-------------------------------------")
num = input("OUT 시킬 선수 번호 : ")
name = input("IN 할 선수 이름 : ")

del players[int(num)]
players.append(name)

print("교체 결과:")
for i in players:
    print(i)