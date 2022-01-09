from random import randrange
a = randrange(1, 15)
b = 0
while a != b:
  with open("file5.txt", "a") as file:
    num = randrange(1, 200)
    file.write(str(num) + " ")
    b +=1

s = 0
with open("file5.txt", "r") as file:
  text = file.readlines()
  for i in text:
    string = i.split()
    print(string)
    for el in string:
      s += int(el)
print(s)