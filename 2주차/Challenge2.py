data = ["조회수 : 1,500","조회수 : 1,002","조회수 : 300","조회수 : 251","조회수 : 13,432","조회수 : 998",]

#LV1.
for i in data:
    print(i)

#LV2.
for i in data:
    i = i.replace("조회수 : ","")
    i = i.replace(",","")
    print(i)

#LV2.
answer=0;
for i in data:
    i = i.replace("조회수 : ","")
    i = i.replace(",","")
    print(i)
    i = int(i)
    answer +=i
print("총 합:",answer)