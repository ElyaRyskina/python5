summ = 0
a = 0
with open("file3.txt", encoding='utf-8') as file:
    text = file.readlines()
    for i in text:
        string = i.split()
        salary = int(string[1])

        if salary < 20000:
            print(string[0])
            summ += salary
            a+=1
print(summ/a)





