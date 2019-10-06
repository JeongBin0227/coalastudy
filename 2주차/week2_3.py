string1 = "브이넥 라이트 다운 베스트"
string2 = "      25,990원    "

print(string1)
print(string2)

# print(string1[0])
# print(string1[1])
# print(string1[2])
# print(string1[3])

# print(string1[0:3])

print(string1.replace("라이트", "해비"))
print(string2.strip())
string2 = string2.strip()
string2 =  string2.replace(",","")
string2 = string2[:-1]
string2 = int(string2)
print(string2)
