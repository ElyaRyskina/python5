import re
content = []
with open("file6.txt", encoding='utf-8') as file:
    for line in file:
        content.append(line)
data = {}
for el in content:
    name_1 = el.split()
    name = name_1[0]
    name = name[:-1]
    nums = re.findall(r'\d+', str(name_1))
    nums = [int(i) for i in nums]
    data[name] = sum(nums)
print(data)

