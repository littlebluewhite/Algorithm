# ex10_1.py
data = []
while True:
    val = input("請輸入數值(Q或q代表輸入結束) : ")
    if val == "Q" or val == "q":
        break
    data.append(int(val))
            
min = data[0]
for num in data:
    if num < min:
        min = num
print("最小值 : ", min)












min_value = None
while True:
    value = input("請輸入數值(Q或q代表輸入結束) : ")
    if value == "q" or value == "Q":
        break
    if min_value is None:
        min_value = int(value)
    elif int(value) < min_value:
        min_value = int(value)

print(min_value)




































