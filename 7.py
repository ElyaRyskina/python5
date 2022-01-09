import json
sum_profit = 0
a = 0
data = {}
list = []
with open("file7.txt", encoding='utf-8') as file:
    for line in file:
        string = line.split()
        name = string[0]
        profit = int(string[2]) - int(string[3])
        data[name] = profit
        if profit > 0:
            sum_profit += profit
            a += 1
data_average = {" average_profit": sum_profit/a}
list.append(data)
list.append(data_average)
with open("my_file.json", "w") as new_file:
    json.dump(list, new_file)

